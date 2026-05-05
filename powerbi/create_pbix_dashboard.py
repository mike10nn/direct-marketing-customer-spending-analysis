from pathlib import Path

import pandas as pd
from pbix_mcp.builder import PBIXBuilder


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "powerbi" / "data" / "DirectMarketing_Clean.csv"
OUTPUT = ROOT / "powerbi" / "DirectMarketing_Dashboard.pbix"


def rows_for_powerbi(df: pd.DataFrame) -> list[dict]:
    """Convert pandas rows into plain Python values for the PBIX builder."""
    rows = []
    for row in df.to_dict(orient="records"):
        rows.append(
            {
                key: (None if pd.isna(value) else value.item() if hasattr(value, "item") else value)
                for key, value in row.items()
            }
        )
    return rows


def main() -> None:
    df = pd.read_csv(SOURCE)

    columns = [
        {"name": "CustomerID", "data_type": "Int64"},
        {"name": "Age", "data_type": "String"},
        {"name": "Gender", "data_type": "String"},
        {"name": "OwnHome", "data_type": "String"},
        {"name": "Married", "data_type": "String"},
        {"name": "Location", "data_type": "String"},
        {"name": "Salary", "data_type": "Int64"},
        {"name": "Children", "data_type": "Int64"},
        {"name": "History", "data_type": "String"},
        {"name": "Catalogs", "data_type": "Int64"},
        {"name": "AmountSpent", "data_type": "Int64"},
        {"name": "SalaryBand", "data_type": "String"},
        {"name": "SpendingBand", "data_type": "String"},
    ]

    b = PBIXBuilder()
    b.add_table(
        "DirectMarketing",
        columns,
        rows=rows_for_powerbi(df),
        source_csv=str(SOURCE),
    )

    measures = {
        "Total Customers": "DISTINCTCOUNT(DirectMarketing[CustomerID])",
        "Total Amount Spent": "SUM(DirectMarketing[AmountSpent])",
        "Average Amount Spent": "AVERAGE(DirectMarketing[AmountSpent])",
        "Median Amount Spent": "MEDIAN(DirectMarketing[AmountSpent])",
        "Average Salary": "AVERAGE(DirectMarketing[Salary])",
        "Average Catalogues Sent": "AVERAGE(DirectMarketing[Catalogs])",
        "Total Catalogues Sent": "SUM(DirectMarketing[Catalogs])",
        "Spend per Catalogue": "DIVIDE([Total Amount Spent], [Total Catalogues Sent])",
        "High Value Customers": "CALCULATE([Total Customers], DirectMarketing[AmountSpent] >= 2000)",
        "High Value Customer Share": "DIVIDE([High Value Customers], [Total Customers])",
    }
    for name, expression in measures.items():
        b.add_measure("DirectMarketing", name, expression)

    b.add_page(
        "Customer Spending Overview",
        visuals=[
            {"type": "card", "name": "total_customers", "x": 20, "y": 20, "width": 280, "height": 120, "config": {"measure": "Total Customers"}},
            {"type": "card", "name": "total_spend", "x": 320, "y": 20, "width": 280, "height": 120, "config": {"measure": "Total Amount Spent"}},
            {"type": "card", "name": "average_spend", "x": 620, "y": 20, "width": 280, "height": 120, "config": {"measure": "Average Amount Spent"}},
            {"type": "card", "name": "average_salary", "x": 920, "y": 20, "width": 280, "height": 120, "config": {"measure": "Average Salary"}},
            {"type": "clusteredBarChart", "name": "spend_by_history", "x": 20, "y": 170, "width": 380, "height": 260, "config": {"category": {"table": "DirectMarketing", "column": "History"}, "measure": "Average Amount Spent"}},
            {"type": "clusteredColumnChart", "name": "spend_by_salary_band", "x": 430, "y": 170, "width": 380, "height": 260, "config": {"category": {"table": "DirectMarketing", "column": "SalaryBand"}, "measure": "Total Amount Spent"}},
            {"type": "lineChart", "name": "spend_by_catalogues", "x": 840, "y": 170, "width": 380, "height": 260, "config": {"category": {"table": "DirectMarketing", "column": "Catalogs"}, "measure": "Average Amount Spent"}},
            {"type": "clusteredColumnChart", "name": "spend_by_age", "x": 20, "y": 460, "width": 380, "height": 220, "config": {"category": {"table": "DirectMarketing", "column": "Age"}, "measure": "Average Amount Spent"}},
            {"type": "matrix", "name": "history_catalogue_matrix", "x": 430, "y": 460, "width": 380, "height": 220, "config": {"columns": [{"table": "DirectMarketing", "column": "History"}, {"table": "DirectMarketing", "column": "Catalogs"}, {"measure": "Average Amount Spent"}]}},
            {"type": "slicer", "name": "history_slicer", "x": 840, "y": 460, "width": 180, "height": 220, "config": {"column": {"table": "DirectMarketing", "column": "History"}}},
            {"type": "slicer", "name": "location_slicer", "x": 1040, "y": 460, "width": 180, "height": 220, "config": {"column": {"table": "DirectMarketing", "column": "Location"}}},
        ],
    )

    b.add_page(
        "Customer Segments",
        visuals=[
            {"type": "card", "name": "high_value_customers", "x": 20, "y": 20, "width": 300, "height": 120, "config": {"measure": "High Value Customers"}},
            {"type": "card", "name": "high_value_share", "x": 340, "y": 20, "width": 300, "height": 120, "config": {"measure": "High Value Customer Share"}},
            {"type": "clusteredBarChart", "name": "spend_by_children", "x": 20, "y": 170, "width": 380, "height": 260, "config": {"category": {"table": "DirectMarketing", "column": "Children"}, "measure": "Average Amount Spent"}},
            {"type": "clusteredColumnChart", "name": "spend_by_gender", "x": 430, "y": 170, "width": 380, "height": 260, "config": {"category": {"table": "DirectMarketing", "column": "Gender"}, "measure": "Average Amount Spent"}},
            {"type": "clusteredColumnChart", "name": "spend_by_home", "x": 840, "y": 170, "width": 380, "height": 260, "config": {"category": {"table": "DirectMarketing", "column": "OwnHome"}, "measure": "Average Amount Spent"}},
            {"type": "tableEx", "name": "segment_table", "x": 20, "y": 460, "width": 760, "height": 220, "config": {"columns": [{"table": "DirectMarketing", "column": "Age"}, {"table": "DirectMarketing", "column": "Gender"}, {"table": "DirectMarketing", "column": "History"}, {"measure": "Average Amount Spent"}, {"measure": "Total Customers"}]}},
            {"type": "slicer", "name": "age_slicer", "x": 820, "y": 460, "width": 180, "height": 220, "config": {"column": {"table": "DirectMarketing", "column": "Age"}}},
            {"type": "slicer", "name": "married_slicer", "x": 1020, "y": 460, "width": 180, "height": 220, "config": {"column": {"table": "DirectMarketing", "column": "Married"}}},
        ],
    )

    issues = b.validate()
    if issues:
        raise RuntimeError("\n".join(issues))

    path = b.save(str(OUTPUT))
    print(path)


if __name__ == "__main__":
    main()
