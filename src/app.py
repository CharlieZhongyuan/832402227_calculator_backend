from flask import Flask, request, jsonify
from flask_cors import CORS
from src.database import init_db, insert_record, get_all_records, delete_record
from src.calculator import calculate
app = Flask(__name__)
CORS(app)
init_db()
@app.route("/api/calculate", methods=["POST"])
def do_calculate():
    data = request.get_json()
    if not data or "expression" not in data:
        return jsonify({"success": False, "message": "Missing expression"}), 400

    expression = data["expression"]
    result, error = calculate(expression)

    if error:
        return jsonify({"success": False, "message": error}), 400

    insert_record(expression, result)
    return jsonify({
        "success": True,
        "expression": expression,
        "result": result
    }), 200
@app.route("/api/history", methods=["GET"])
def get_history():
    records = get_all_records()
    return jsonify({"success": True, "history": records}), 200
@app.route("/api/history/<int:record_id>", methods=["DELETE"])
def remove_history(record_id):
    success = delete_record(record_id)
    if success:
        return jsonify({"success": True, "message": "Deleted"}), 200
    else:
        return jsonify({"success": False, "message": "Record not found"}), 404
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)