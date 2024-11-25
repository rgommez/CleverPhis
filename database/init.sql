CREATE TABLE phishing_emails (
    id SERIAL PRIMARY KEY,
    email_content TEXT NOT NULL,
    is_phishing BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
