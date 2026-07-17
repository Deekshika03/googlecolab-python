#ps : Evaluating the Impact of Regularization on Linear Regression Using the Diabetes Dataset
"""Tasks & Requirements 
Baseline Evaluation:Train a baseline LinearRegression, Ridge ($\alpha=1.0$), and Lasso ($\alpha=0.1$) model on an 80/20 train-test split of the Diabetes dataset. 
Evaluate and compare their predictive accuracy using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and the Coefficient of Determination ($R^2$).
Hyperparameter Tuning ($\alpha$): Train multiple Ridge and Lasso models across a logarithmic scale of alpha values ([0.01, 0.1, 1, 10, 100]) to identify the optimal regularization strength.
Sparsity & Coefficient Analysis: Track the magnitude of feature coefficients and count the number of zeroed-out weights in the Lasso model as $\alpha$ increases.
Data Visualization: Plot two synchronized subplots:Subplot 1: $R^2$ Score vs. Alpha (on a log scale) for both Ridge and Lasso to visually identify underfitting and overfitting thresholds.
Subplot 2: Lasso Coefficient Path vs. Alpha (on a log scale) to visualize feature elimination."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
features = diabetes.feature_names

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    )
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)
    return mae, mse, rmse, r2

lr = LinearRegression().fit(X_train, y_train)
ridge_base = Ridge(alpha=1.0).fit(X_train, y_train)
lasso_base = Lasso(alpha=0.1).fit(X_train, y_train)

models = {'Linear': lr, 'Ridge (alpha=1.0)': ridge_base, 'Lasso (alpha=0.1)': lasso_base}
print("base line comparison")
for name, model in models.items():
    mae, mse, rmse, r2 = evaluate_model(model, X_test, y_test)
    print(f"{name}:\t MAE: {mae:.2f} | MSE: {mse:.2f} | RMSE: {rmse:.2f} | R2: {r2:.4f}")

alphas = [0.01, 0.1, 1, 10, 100]
ridge_r2, lasso_r2 = [], []
ridge_coefs, lasso_coefs = [], []
lasso_zero_counts = []

for a in alphas:
    r = Ridge(alpha=a).fit(X_train, y_train)
    ridge_r2.append(r2_score(y_test, r.predict(X_test)))
    ridge_coefs.append(r.coef_)

    l = Lasso(alpha=a).fit(X_train, y_train)
    lasso_r2.append(r2_score(y_test, l.predict(X_test)))
    lasso_coefs.append(l.coef_)
    lasso_zero_counts.append(np.sum(l.coef_ == 0))

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.semilogx(alphas, ridge_r2, label='Ridge $R^2$', marker='o')
plt.semilogx(alphas, lasso_r2, label='Lasso $R^2$', marker='s')
plt.title('Model Performance ($R^2$) vs. Alpha')
plt.xlabel('Alpha (log scale)')
plt.ylabel('$R^2$ Score')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
ax = plt.gca()
ax.plot(alphas, lasso_coefs)
ax.set_xscale('log')
plt.title('Lasso Coefficients vs. Alpha')
plt.xlabel('Alpha (log scale)')
plt.ylabel('Coefficient Magnitude')
plt.axis('tight')
plt.grid(True)

plt.tight_layout()
plt.show()
