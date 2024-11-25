from flask import jsonify, request
from src.nlp.analyze import analyze_email
from src.database.queries import save_email

def init_routes(app):
    @app.route("/analyze", methods=["POST"])
    def analyze():
        content = request.json.get("email_content")
        if not content:
            return jsonify({"error": "No content provided"}), 400
        result = analyze_email(content)
        save_email(content, result)
        return jsonify({"is_phishing": result})
