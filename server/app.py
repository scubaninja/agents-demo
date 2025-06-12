import os
from flask import Flask
from models import init_db
from routes.games import games_bp
from routes.categories import categories_bp
from routes.publishers import publishers_bp
from utils.database import init_db

# Get the server directory path
base_dir: str = os.path.abspath(os.path.dirname(__file__))

app: Flask = Flask(__name__)

# Initialize the database with the app
init_db(app)

# Register blueprints
app.register_blueprint(games_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(publishers_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5100) # Port 5100 to avoid macOS conflicts