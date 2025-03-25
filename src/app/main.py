from flask import Flask
from flask_cors import CORS
from src.app.routes import init_routes

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = "your_secret_key"

init_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
