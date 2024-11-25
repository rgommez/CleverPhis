import joblib

# Load model and vectorizer
model = joblib.load("src/models/phishing_model.pkl")
vectorizer = joblib.load("src/models/vectorizer.pkl")

def analyze_email(content: str) -> bool:
    content_tfidf = vectorizer.transform([content])
    return bool(model.predict(content_tfidf)[0])
