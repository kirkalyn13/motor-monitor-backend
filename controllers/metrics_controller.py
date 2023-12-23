from flask import request, jsonify
from app import app
import services.metrics_service as metrics_service
from utilities.error import error

@app.route("/api/v1/metrics/<id>", methods=["GET"])
def get_latest_metrics(id):
    if request.method == "GET":
        try:
            rated_voltage = float(request.args.get('ratedVoltage'))
            rated_current = float(request.args.get('ratedCurrent'))
            max_temperature = float(request.args.get('maxTemperature'))
            result = metrics_service.get_latest_metrics(id, rated_voltage, rated_current, max_temperature)
            return jsonify(result), 200
        except Exception as e:
            return jsonify(error(str(e))), 500
    
@app.route("/api/v1/metrics/voltage/<id>", methods=["GET"])
def get_voltage_trend(id):
    if request.method == "GET":
        try:
            result = metrics_service.get_voltage_trend(id)
            return jsonify(result), 200
        except Exception as e:
            return jsonify(error(str(e))), 500
    
@app.route("/api/v1/metrics/current/<id>", methods=["GET"])
def get_current_trend(id):
    if request.method == "GET":
        try:
            result = metrics_service.get_current_trend(id)
            return jsonify(result), 200
        except Exception as e:
            return jsonify(error(str(e))), 500
    
@app.route("/api/v1/metrics/temperature/<id>", methods=["GET"])
def get_temperature_trend(id):
    if request.method == "GET":
        try:
            result = metrics_service.get_temperature_trend(id)
            return jsonify(result), 200
        except Exception as e:
            return jsonify(error(str(e))), 500
        
@app.route("/api/v1/metrics/summary/<id>", methods=["GET"])
def get_metrics_summary(id):
    if request.method == "GET":
        try:
            rated_voltage = float(request.args.get('ratedVoltage'))
            rated_current = float(request.args.get('ratedCurrent'))
            max_temperature = float(request.args.get('maxTemperature'))
            result = metrics_service.get_metrics_summary(id, rated_voltage, rated_current, max_temperature)
            return jsonify(result), 200
        except Exception as e:
            return jsonify(error(str(e))), 500
        
@app.route("/api/v1/metrics/alarms/<id>", methods=["GET"])
def get_alarms(id):
    if request.method == "GET":
        try:
            rated_voltage = float(request.args.get('ratedVoltage'))
            rated_current = float(request.args.get('ratedCurrent'))
            max_temperature = float(request.args.get('maxTemperature'))
            result = metrics_service.get_alarms(id, rated_voltage, rated_current, max_temperature)
            return jsonify(result), 200
        except Exception as e:
            return jsonify(error(str(e))), 500
        
@app.route("/api/v1/metrics/<id>", methods=["POST"])
def add_metrics(id):
    if request.method == "POST":
        try:
            line1_voltage = float(request.args.get('line1Voltage'))
            line2_voltage = float(request.args.get('line2Voltage'))
            line3_voltage = float(request.args.get('line3Voltage'))
            line1_current = float(request.args.get('line1Current'))
            line2_current = float(request.args.get('line2Current'))
            line3_current = float(request.args.get('line3Current'))
            temperature = float(request.args.get('temperature'))
            result = metrics_service.add_metrics(
                id, 
                line1_voltage, 
                line2_voltage, 
                line3_voltage,
                line1_current,
                line2_current,
                line3_current,
                temperature
                )
            return jsonify(result), 201
        except Exception as e:
            return jsonify(error(str(e))), 500