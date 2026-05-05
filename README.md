# Direct Marketing Customer Spending Analysis

This project analyses a direct marketing dataset to understand what influences how much customers spend after receiving catalogues. The goal was to clean the data, explore the main patterns, and build a regression model that explains customer spending using demographic and marketing-related variables.

## Dataset

The dataset contains 1,000 customer records with information such as:

- age group
- gender
- home ownership
- marital status
- location
- salary
- number of children
- purchase history
- number of catalogues sent
- amount spent

The main target variable is `AmountSpent`.

## What I Did

I started by loading the dataset and checking the general structure of the data. I looked for missing values and duplicate rows, then cleaned the `History` column by replacing missing values with `None`. I also made sure the numerical columns were stored correctly and converted the categorical columns into a suitable format for analysis.

After the cleaning step, I explored the data using summary statistics and visualisations. I looked at the distribution of customer spending, the relationship between salary and spending, the effect of the number of catalogues sent, and differences in spending based on purchase history.

Finally, I prepared the data for modelling by converting categorical variables into dummy variables. I then used multiple linear regression to estimate how each variable is related to `AmountSpent`. I also checked the model again with robust standard errors to make the results more reliable.

## Main Findings

The regression model explained a large part of the variation in customer spending, with an R-squared value of about 0.75.

Some of the clearest findings were:

- customers with higher salaries tend to spend more
- sending more catalogues is linked with higher spending
- customers living farther away spent more in this dataset
- customers with low or medium purchase history spent less than the baseline group
- customers with more children tended to spend less

The analysis also showed that purchase history is an important variable, but missing history values needed to be handled carefully before modelling.

## Files

- `DirectMarketing.csv` contains the dataset used for the analysis.
- `mainn.ipynb` contains the full notebook with the cleaning, exploration, visualisations, and regression model.
- `powerbi/` contains the Power BI dashboard file, cleaned dataset, dashboard measures, theme, preview, and build guide.
- `requirements.txt` lists the main Python libraries used.

## How To Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Then open `mainn.ipynb` in Jupyter Notebook, JupyterLab, or VS Code and run the cells from top to bottom.

The Power BI dashboard can be opened directly from:

`powerbi/DirectMarketing_Dashboard.pbix`

## Tools Used

- Python
- pandas
- matplotlib
- statsmodels
- Jupyter Notebook
