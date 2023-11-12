from flask import request, jsonify
from app import app
import services.metrics_service as metrics_service

@app.route("/api/v1/metrics/<id>", methods=["GET"])
def get_latest_metrics(id):
    if request.method == "GET":
        result = metrics_service.get_latest_metrics(id)
        return jsonify(result), 200
    
@app.route("/api/v1/metrics/voltage/<id>", methods=["GET"])
def get_voltage_trend(id):
    if request.method == "GET":
        result = metrics_service.get_voltage_trend(id)
        return jsonify(result), 200