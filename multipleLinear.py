
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


# 1. Load Excel data
df = pd.read_excel('multiple_regression_dummy_data.xlsx')  # Your file name

# 2. Define X (independent) and y (dependent) variables
X = df[['productQuality', 'priceFairness', 'advertisingAppeal', 'customerService', 'brandReputation']]
y = df['purchaseIntention']

# 3. Add constant (intercept)
X = sm.add_constant(X)

# 4. Fit OLS model
model = sm.OLS(y, X).fit()

# 5. Coefficient summary table
summary_df = pd.DataFrame({
    'Coefficient': model.params,
    'Standard Error': model.bse,
    't-value': model.tvalues,
    'p-value': model.pvalues,
    'CI Lower 95%': model.conf_int()[0],
    'CI Upper 95%': model.conf_int()[1]
})

# 6. Predictions and residuals
predictions_df = pd.DataFrame({
    'Actual': y,
    'Predicted': model.predict(X),
    'Residual': model.resid
})

# 7. Model fit statistics
summary_stats = {
    'R-squared': model.rsquared,
    'Adjusted R-squared': model.rsquared_adj,
    'F-statistic': model.fvalue,
    'F-stat p-value': model.f_pvalue,
    'AIC': model.aic,
    'BIC': model.bic,
    'No. of observations': int(model.nobs)
}
summary_stats_df = pd.DataFrame.from_dict(summary_stats, orient='index', columns=['Value'])

# 8. Export all to Excel
with pd.ExcelWriter('Full_OLS_Regression_Report.xlsx', engine='openpyxl') as writer:
    summary_df.to_excel(writer, sheet_name='Regression Coefficients')
    predictions_df.to_excel(writer, sheet_name='Predictions_Residuals', index=False)
    summary_stats_df.to_excel(writer, sheet_name='Model Summary')

from statsmodels.stats.outliers_influence import variance_inflation_factor

# Reuse X from your regression, without the constant column
X_no_const = X.drop(columns='const')

# Compute VIF for each feature
vif_data = pd.DataFrame()
vif_data['Feature'] = X_no_const.columns
vif_data['VIF'] = [variance_inflation_factor(X_no_const.values, i) for i in range(X_no_const.shape[1])]

print(vif_data)
