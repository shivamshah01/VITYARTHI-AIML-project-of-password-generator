import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {
    "population": [50000, 70000, 90000, 60000, 80000, 75000, 65000],
    "locality": ["urban", "urban", "metro", "rural", "metro", "urban", "rural"],
    "cost_of_living": [300, 400, 500, 200, 450, 350, 250],
    "price": [200000, 300000, 500000, 150000, 450000, 320000, 180000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Encode locality (text → number)
le = LabelEncoder()
df["locality"] = le.fit_transform(df["locality"])

# Features and target
X = df[["population", "locality", "cost_of_living"]]
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
print("Model Accuracy:", model.score(X_test, y_test))

# --- User Input ---
population = int(input("Enter population: "))
locality = input("Enter locality (urban/rural/metro): ")
cost = float(input("Enter cost of living index: "))

# Convert locality using same encoder
locality_encoded = le.transform([locality])[0]

# Prediction
predicted_price = model.predict([[population, locality_encoded, cost]])

print("Predicted House Price:", predicted_price[0])