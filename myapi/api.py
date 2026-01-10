from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Welcome to My API!</h1>"
@app.route("/api/cars",methods=["GET"])
def cars():
    mycars=[
        {"model":"BMW X5","year":2020,"price":60000},
        {"model":"Audi Q7","year":2019,"price":55000},
        {"model":"Mercedes GLE","year":2021,"price":70000}
    ]
    return jsonify(mycars)

@app.route("/api/calculator/<int:num1>/<int:num2>/<string:operation>",methods=["GET"])
def calculator(num1,num2,operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({"error": "Division by zero is not allowed"}), 400
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)