import joblib
import requests
import os

# Cargar modelo local
model = joblib.load("src/models/phishing_model.pkl")
vectorizer = joblib.load("src/models/vectorizer.pkl")

DEEPSHEEK_API_KEY = os.getenv("DEEPSHEEK_API_KEY")

def analyze_email(content: str) -> bool:
    
    # Intentar análisis con DeepSheek
    if DEEPSHEEK_API_KEY:
        try:
            response = requests.post(
                "https://api.deepsheek.com/analyze",
                json={"text": content},
                headers={"Authorization": f"Bearer {DEEPSHEEK_API_KEY}"}
            )
            if response.status_code == 200:
                return response.json().get("is_phishing", False)
        except requests.RequestException:
            pass  # Si falla, usa el modelo local
    
    # Modelo local como respaldo
    content_tfidf = vectorizer.transform([content])
    return bool(model.predict(content_tfidf)[0])


def check_phishtank(url: str) -> bool:
    response = requests.get(f"https://phishtank.org/check_url.php?url={url}")
    return "phishing" in response.text