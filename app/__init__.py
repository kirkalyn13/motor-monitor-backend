from flask import Flask

app = Flask(__name__)

# Import controllers here: 
from controllers import voltage_controller