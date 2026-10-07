from flask import Flask, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@app.route("/")
def home():
    return jsonify({
        "message": "Calculator API is running"
    })


@app.route("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    return jsonify({"result": add(a, b)})


@app.route("/subtract/<int:a>/<int:b>")
def subtract_numbers(a, b):
    return jsonify({"result": subtract(a, b)})


@app.route("/multiply/<int:a>/<int:b>")
def multiply_numbers(a, b):
    return jsonify({"result": multiply(a, b)})


@app.route("/divide/<int:a>/<int:b>")
def divide_numbers(a, b):
    if b == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    return jsonify({"result": divide(a, b)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)