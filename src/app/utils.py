import re

def validate_email_content(content: str) -> bool:
    return len(content) > 10  # Simple validation


def validate_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None