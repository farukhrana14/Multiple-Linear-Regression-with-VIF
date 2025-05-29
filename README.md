# Multiple-Linear-Regression-with-VIF
📘 Project: Multiple Linear Regression Analysis – Brand Impact on Purchase Intention

🧾 Overview
This Python project performs multiple linear regression to analyze how various brand-related factors (e.g., product quality, price fairness, advertising appeal, customer service, brand reputation) influence consumers' purchase intention.

The code:
Loads data from an Excel file
Runs OLS regression
Calculates predicted values and residuals
Exports full regression output including coefficients, statistics, and prediction summary
Checks for multicollinearity using Variance Inflation Factor (VIF)
Refits model by removing highly collinear predictors
Visualizes correlation using a heatmap

📂 Files and Structure
File/Folder	Description
multiple_regression_dummy_data.xlsx	Sample dataset used in regression regression_analysis.py	Python script with full regression workflow Full_OLS_Regression_Report.xlsx	Excel file with regression output VIF_Table.xlsx	Exported table showing VIF values for predictors Reduced_Model_Summary.xlsx	Summary of regression with reduced predictors Correlation_Heatmap.png	Visual heatmap showing variable correlations README.md	Project documentation (this file)

📊 Variables Used
Independent Variables:
productQuality
priceFairness
advertisingAppeal
customerService
brandReputation

Dependent Variable:
purchaseIntention

🔁 Steps Performed
Load dataset from Excel
Fit OLS model using statsmodels
Calculate:
Coefficients
Standard errors
t-values
p-values
Confidence intervals
Export predictions and residuals
Generate VIF values to detect multicollinearity
Create correlation heatmap using seaborn
Refit model with selected predictors

📈 Tools & Libraries
Python 3.11+
pandas
statsmodels
seaborn
matplotlib
openpyxl

✅ How to Run
pip install pandas statsmodels matplotlib seaborn openpyxl
python regression_analysis.py

📬 Output
Visual and statistical insights into which brand attributes most strongly influence consumer purchase behavior.
Ready-to-use regression outputs in Excel for presentation or academic reporting.
