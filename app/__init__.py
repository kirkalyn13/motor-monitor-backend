from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Define CORS options
cors_config = {
    "origins": ["https://motor-monitor-frontend.vercel.app", "http://localhost:3000"], 
    "methods": ["GET", "POST", "PUT", "DELETE"], 
    "allow_headers": ["Content-Type"],
    "supports_credentials": True,
    "max_age": 120,
}

CORS(app, resources={r"/api/*": cors_config}) 

# Import controllers here: 
from controllers import metrics_controller
from controllers import health_controller