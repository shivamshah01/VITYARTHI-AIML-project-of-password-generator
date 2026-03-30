# 📋 Problem Statement & Objectives
## House Price Prediction System

---

##  Problem Statement

> **Real estate pricing is highly inconsistent, opaque, and difficult to estimate without expert knowledge.**

In today's housing market, buyers, sellers, and investors face a critical challenge:
**there is no simple, data-driven way for a common person to estimate the fair price of a house** based on the area they are looking at.

House prices are influenced by multiple interdependent factors — the size of the population in a region, whether it is a rural, urban, or metro area, and the overall cost of living index. Manually assessing all these variables is time-consuming, error-prone, and often biased.

### The Core Problem

| Factor | Challenge |
|---|---|
| **Population** | Densely populated areas command higher prices, but by how much? |
| **Locality Type** | Urban vs rural vs metro pricing differs vastly with no clear formula |
| **Cost of Living** | Higher living costs correlate with price, but the relationship is non-trivial |
| **No Unified Model** | No lightweight, accessible tool exists to combine these factors instantly |

Without a predictive model, stakeholders are left relying on guesswork, outdated listings, or expensive real estate consultants — leading to **uninformed decisions and financial risk**.

---

##  Objectives

The House Price Prediction System is designed to directly solve the above problem through the following objectives:

### Primary Objective
> Build a machine learning model that accurately predicts house prices using population, locality type, and cost of living as input features.

### Secondary Objectives

1. **Automate Feature Encoding**
   Convert categorical locality data (`urban`, `rural`, `metro`) into a numeric format suitable for machine learning using `LabelEncoder`.

2. **Establish a Reproducible ML Pipeline**
   Implement a clean, modular pipeline — data preparation → encoding → splitting → training → evaluation → prediction.

3. **Train & Evaluate a Regression Model**
   Use Linear Regression to learn price patterns from historical data and measure performance using the R² (coefficient of determination) score.

4. **Enable Real-Time User Prediction**
   Accept live inputs from a user (population, locality, cost of living) and return an instant predicted house price without any manual calculation.

5. **Serve as an Extensible Baseline**
   Provide a working prototype that can be scaled with larger datasets and upgraded with advanced models (Random Forest, XGBoost, etc.) in the future.

---

##  Scope

| In Scope | Out of Scope |
|---|---|
| Predicting price from 3 structured features | Image-based or NLP-based price prediction |
| Command-line user interaction | Web or mobile UI (future enhancement) |
| Linear Regression model | Deep learning or neural network models |
| Small prototype dataset (7 records) | Large-scale production dataset |
| Python-based implementation | Cloud deployment or API serving |

---

##  Expected Outcome

Upon successful execution, the system will:

- Report the **model accuracy** (R² score) on the test split
- Accept three inputs from the user
- Output a **predicted house price in USD** based on the trained model

This makes house price estimation **accessible, fast, and data-driven** for anyone — without needing real estate expertise.

---

*House Price Prediction System — Problem Statement v1.0 | March 2026*
