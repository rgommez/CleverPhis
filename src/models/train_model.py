import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("data/phishing_dataset.csv")
X = data["email_content"]
y = data["is_phishing"]

# Train model
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)
model = RandomForestClassifier()
model.fit(X_tfidf, y)

# Save model
joblib.dump(model, "src/models/phishing_model.pkl")
joblib.dump(vectorizer, "src/models/vectorizer.pkl")
