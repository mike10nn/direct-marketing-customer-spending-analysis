# Power BI Dashboard Build Guide

## Dashboard Goal

This dashboard should explain which customer characteristics are linked to higher spending after a direct marketing campaign. The report is designed as a one-page executive dashboard, so the main message is clear without needing too many visuals.

## Data To Import

Import this file into Power BI:

`powerbi/data/DirectMarketing_Clean.csv`

This cleaned version keeps the original dataset but adds:

- `CustomerID` for counting customers correctly
- `SalaryBand` for easier income-based analysis
- `SpendingBand` for customer segmentation
- `History` values where missing records are shown as `None`

## Recommended Page Setup

Use a 16:9 canvas.

Suggested report title:

`Direct Marketing Customer Spending Dashboard`

Suggested subtitle:

`Customer spend patterns by income, purchase history, catalogues, and demographics`

Import the theme file:

`powerbi/direct_marketing_theme.json`

In Power BI Desktop, go to:

`View > Browse for themes`

## Measures To Create

Create the measures from:

`powerbi/measures.dax`

The most important measures for the dashboard are:

- `Total Customers`
- `Total Amount Spent`
- `Average Amount Spent`
- `Average Salary`
- `Average Catalogues Sent`
- `Spend per Catalogue`
- `High Value Customers`
- `High Value Customer Share`

## Dashboard Layout

### Top Row: KPI Cards

Create four card visuals:

- `Total Customers`
- `Total Amount Spent`
- `Average Amount Spent`
- `Average Salary`

These cards give a quick overview of the customer base and total campaign value.

### Middle Row: Main Analysis

Create a bar chart:

- Axis: `History`
- Values: `Average Amount Spent`
- Sort: descending by `Average Amount Spent`
- Title: `Average Spend by Purchase History`

Create a scatter chart:

- X-axis: `Salary`
- Y-axis: `AmountSpent`
- Legend: `History`
- Size: `Catalogs`
- Title: `Salary vs Amount Spent`

Create a line chart:

- X-axis: `Catalogs`
- Y-axis: `Average Amount Spent`
- Title: `Average Spend by Catalogues Sent`

### Bottom Row: Customer Segments

Create a column chart:

- X-axis: `SalaryBand`
- Y-axis: `Total Amount Spent`
- Title: `Total Spend by Salary Band`

Create a column chart:

- X-axis: `Age`
- Y-axis: `Average Amount Spent`
- Title: `Average Spend by Age Group`

Create a matrix:

- Rows: `History`
- Columns: `Catalogs`
- Values: `Average Amount Spent`
- Title: `Spend by History and Catalogue Volume`

## Filters / Slicers

Add slicers on the left side or at the top of the page:

- `Age`
- `Gender`
- `OwnHome`
- `Married`
- `Location`
- `History`

These slicers make the dashboard interactive and help compare customer groups.

## Key Insights To Mention

The dashboard should support these main points:

- customers with higher salaries usually spend more
- customers who receive more catalogues tend to spend more
- purchase history is one of the strongest indicators of spending
- customers with low purchase history spend much less
- customers with more children generally spend less

## Suggested Final Look

Use a clean business style with a warm background, white visual cards, and teal or bronze accent colours. Keep the page simple and avoid adding too many visuals, because the dataset is small and the main story is already clear.
