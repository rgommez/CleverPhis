from src.database.db import SessionLocal
from sqlalchemy import text

def save_email(content, is_phishing):
    session = SessionLocal()
    query = text("INSERT INTO phishing_emails (email_content, is_phishing) VALUES (:content, :is_phishing)")
    session.execute(query, {"content": content, "is_phishing": is_phishing})
    session.commit()
    session.close()
