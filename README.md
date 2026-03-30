 House Price Prediction System

A **supervised machine learning** project that predicts residential house prices based on population, locality type, and cost of living index — built with Python and scikit-learn.

---
 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [License](#license)

---

 Overview

This project demonstrates a complete ML pipeline:

1. Load and preprocess structured data using **pandas**
2. Encode categorical features with **LabelEncoder**
3. Train a **Linear Regression** model using **scikit-learn**
4. Evaluate model accuracy using the **R² score**
5. Accept real-time user inputs and return a predicted house price

---

 Features

-  Categorical encoding of locality type (urban / rural / metro)
-  80/20 train-test split
-  R² score-based model evaluation
-  Interactive command-line prediction interface

---

 Tech Stack

| Library | Purpose |
|---|---|
| `pandas` | Data loading and manipulation |
| `scikit-learn` | ML model, encoding, train/test split |
| `Python 3.x` | Core language |

---

 Dataset

A prototype dataset with **7 records** and 3 input features:

| Feature | Type | Description |
|---|---|---|
| `population` | int | Total area population |
| `locality` | str (encoded) | Area type: urban / rural / metro |
| `cost_of_living` | float | Living cost index |
| `price` | int (**target**) | House price in USD |

---

 How It Works

```
Raw Data → Label Encoding → Train/Test Split → Linear Regression → Evaluate → Predict
```

The `locality` column is encoded alphabetically:
- `metro` → `0`
- `rural` → `1`
- `urban` → `2`

The trained model learns price patterns from the training set, then predicts house prices for new inputs provided by the user.

---

## Getting Started

### Prerequisites

```bash
pip install pandas scikit-learn
```

### Clone & Run

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
python house_price_prediction.py
```

---

## Usage

When you run the script, you will be prompted to enter:

```
Enter population: 72000
Enter locality (urban/rural/metro): urban
Enter cost of living index: 380
```

---

## Sample Output

```
Model Accuracy: 0.9732

Enter population: 72000
Enter locality (urban/rural/metro): urban
Enter cost of living index: 380

Predicted House Price: 312450.78
```

>  **Note:** Accuracy score varies between runs because no `random_state` is set in `train_test_split`.

---

## Limitations

| Issue | Impact |
|---|---|
| Only 7 training records | High variance, potential overfitting |
| No `random_state` | Non-reproducible results |
| No input validation | Crashes on unknown locality strings |
| Linear model only | Cannot capture non-linear price patterns |

---

## Future Improvements

- [ ] Add `random_state=42` to `train_test_split` for reproducibility
- [ ] Expand dataset with real-world housing data (e.g., Kaggle)
- [ ] Add input validation / error handling for unknown localities
- [ ] Try advanced models: Random Forest, XGBoost, Gradient Boosting
- [ ] Apply `StandardScaler` for feature normalization
- [ ] Add K-Fold cross-validation
- [ ] Build a web interface using **Flask** or **Streamlit**

---

## Project Structure

```
house-price-prediction/
│
├── house_price_prediction.py   # Main script
└── README.md                   # Project documentation
```

---

