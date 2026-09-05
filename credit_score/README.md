# Credit Scoring and UPI Usage Prediction

This project demonstrates a credit-scoring workflow for predicting customer UPI usage and converting model predictions into interpretable scorecard risk levels.

## Project highlights

- Prepared numerical and categorical customer-behavior features.
- Treated missing values and investigated balance outliers.
- Selected variables using information value (IV), missingness, and correlation checks.
- Encoded categorical variables and addressed class imbalance with Borderline-SMOTE.
- Trained an XGBoost binary-classification model.
- Evaluated model performance using AUC, KS, precision, recall, and F1-score.
- Built a WOE-based scorecard and mapped scores to Poor, Fair, Good, and Excellent risk levels.
- Exported predictions and scorecard binning results for downstream analysis.

## Model results

The current notebook experiment reported:

| Metric | Test result |
| --- | ---: |
| AUC | 0.9844 |
| KS | 0.9495 |
| Selected classification threshold | 0.9990 |

These results are development results from the available dataset and require independent validation before use in a production credit decision process.

## Workflow

1. Load and inspect customer transaction and usage data.
2. Clean numeric variables and investigate extreme balances.
3. Split data using a stratified train/test split.
4. Select variables using missingness, IV, and correlation criteria.
5. Encode categorical features and balance the training data.
6. Train and evaluate the XGBoost model.
7. Apply WOE transformation and train a scorecard.
8. Generate scores, risk levels, and prediction files.

## Technologies

Python, Pandas, NumPy, Scikit-learn, XGBoost, imbalanced-learn, toad, Matplotlib, Seaborn, and Jupyter Notebook.

## Repository contents

- `UPI Prediction.ipynb` — prediction and score application workflow.
- `UPI 2.ipynb` — feature selection, model evaluation, WOE transformation, and scorecard development.

## Data privacy

Datasets, serialized models, prediction exports, and notebook outputs are not included in this public portfolio repository. Use an anonymized dataset and update the notebook input path before running the project.

## Author

**Koemhort Leng**  
Data Science & Engineering  
[GitHub](https://github.com/LengKoemHort)
