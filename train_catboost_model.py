import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load labeled data
df = pd.read_csv('output.csv')
print(df['Congestion'].value_counts())
# Features and target (Only include nodes, packet size, X, Y, and rate)
X = df[['Nodes', 'PacketSize', 'X', 'Y', 'Rate']]  # Features
y = df['Congestion']  # Target column for congestion
print(df.head(10))
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train CatBoost model
model = CatBoostClassifier(verbose=0)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("CatBoost Classification Report:")
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, "catboost_congestion_model.pkl")
