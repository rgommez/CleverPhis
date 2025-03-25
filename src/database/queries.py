from src.database.db import SessionLocal
from sqlalchemy.sql import text

def save_email(content, is_phishing):
    session = SessionLocal()
    try:
        query = text("INSERT INTO phishing_emails (email_content, is_phishing) VALUES (:content, :is_phishing)")
        session.execute(query, {"content": content, "is_phishing": is_phishing})
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error al guardar en la base de datos: {e}")
    finally:
        session.close()
