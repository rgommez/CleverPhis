import re
import html

def sanitize_input(content: str) -> str:
    content = html.escape(content)  # Escapar HTML
    content = re.sub(r'[^\w\s@.:/-]', '', content)  # Remover caracteres sospechosos
    return content

def validate_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
