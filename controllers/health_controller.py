from flask import request, jsonify
from app import app
import services.health_service as health_service
from utilities.error import error

@app.route("/healthz", methods=["GET"])
def get_server_health():
    if request.method == "GET":
        try:
            db_ok = health_service.get_db_test()
            if db_ok == True:
                status = {'status': 'ok'}
            else:
                status = {
                    'status': 'No Connection',
                    'message': 'Database connection failed.'
                }
            return jsonify(status)
        except Exception as e:
            return jsonify(error(str(e))), 500