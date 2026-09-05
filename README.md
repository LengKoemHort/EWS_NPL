# Early Warning System for Non-Performing Loans

An end-to-end credit-risk modeling project for identifying loans that may become non-performing. The project demonstrates practical data preparation, feature governance, leakage detection, feature selection, XGBoost modeling, validation, and production-readiness planning.

## Project highlights

- Standardized a loan portfolio dataset containing more than 217,000 records.
- Reduced in-memory dataset usage by approximately 86% through data-type optimization.
- Investigated missing values, duplicate fields, currency normalization, and potential outliers.
- Detected and excluded target leakage before model training.
- Selected predictive features using information value (IV) and WOE-based analysis.
- Trained and evaluated an XGBoost binary-classification model.
- Documented threshold calibration, time-based validation, monitoring, and governance considerations.

## Model results

The current development split produced the following results:

| Metric | Test result |
| --- | ---: |
| AUC | 0.8134 |
| Gini | 0.627 |
| NPL recall at the default threshold | 75.0% |

The default probability threshold is not treated as production-ready. A business-driven threshold should be selected based on review capacity, the cost of missed defaults, and the cost of false positives.

## Workflow

1. Clean and standardize source data types and column names.
2. Handle missing values and investigate data-quality issues.
3. Check identifiers, dates, duplicate variables, and target leakage.
4. Rank candidate variables using information value and select model features.
5. Split the data using stratification and preserve the target rate.
6. Train an XGBoost classifier with imbalance-aware weighting.
7. Evaluate AUC, Gini, precision, recall, and flagged-portfolio rate.
8. Document limitations and next steps for production validation.

## Repository structure

```text
credit_risk/
├── data_preprocessing.ipynb       # Initial exploration and preparation
├── remove_outlier.ipynb           # Outlier investigation and cleaning
├── iv_define.ipynb                # IV analysis and feature selection
├── cross_validate.ipynb           # Train/test split preparation
├── feature_selection_output/
│   └── xgboost.ipynb              # XGBoost training and evaluation
├── solution.md                    # Production-readiness action plan
└── README.md
```

## Technologies

Python, Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn, Jupyter Notebook, and SQL-oriented data preparation.

## Data and privacy

The original loan-level data, trained model files, and internal reports are intentionally excluded from this public portfolio repository. They may contain confidential customer, financial, or organizational information. To reproduce the workflow, provide an appropriately anonymized dataset with a binary `IS_NPL` target and update the input paths in the notebooks.

## Portfolio note

This project demonstrates applied credit-risk analytics and machine-learning development. The reported results are from a development dataset and should not be interpreted as approval for production lending decisions without independent validation, monitoring, governance review, and business sign-off.

## Author

**Koemhort Leng**  
Data Science & Engineering  
[GitHub](https://github.com/LengKoemHort)
