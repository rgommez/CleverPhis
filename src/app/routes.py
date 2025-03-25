from flask import Flask, request, jsonify
from src.nlp.analyze import analyze_email
from src.database.queries import save_email
from src.security.validation import sanitize_input

def init_routes(app: Flask):
    @app.route("/analyze", methods=["POST"])
    def analyze():
        content = request.json.get("email_content")
        
        if not content:
            return jsonify({"error": "No content provided"}), 400
        
        sanitized_content = sanitize_input(content)
        result = analyze_email(sanitized_content)
        
        save_email(sanitized_content, result)
        return jsonify({"is_phishing": result})
