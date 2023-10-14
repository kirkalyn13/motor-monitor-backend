from flask import request, jsonify
from app import app
from services.voltage_service import calculate_voltage
from utilities.error import error
import time

@app.route("/api/v1/hello", methods=["GET"])
def hello_controller():
    return jsonify("HELLO"), 200

@app.route("/api/v1/analyze", methods=["POST"])
def analyze_controller():
    if request.method == "POST":
        try:
            print("Analyzing motor...")
            time.sleep(1)
            print("Obtaining data...")
            time.sleep(2)
            print("Running diagnostics...")
            time.sleep(3)
            print("Generating report...")
            time.sleep(3)
            print("Analysis done.")

            result = {
                "status": "success",
                "motorHealth": "OK",
                "readings": {
                    "1": 100,
                    "2": 150,
                    "3": 120,
                    "4": 220,
                    "5": 200,
                }
            }
            # raise ValueError("Forced exception")
            return jsonify(result), 200
        except:
            return jsonify(error("Analysis Failed.")), 500
        
    
@app.route("/api/v1/voltage", methods=["POST"])
def voltage_controller():
    if request.method == "POST":
        data = request.get_json()
        result = calculate_voltage(data["current"], data["resistance"])
        return jsonify(result), 200