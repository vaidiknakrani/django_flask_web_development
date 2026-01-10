from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../flask/templates')
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

def calculate_total(marks):
    return sum(marks)

def calculate_grade(marks):
    if not marks:
        return 'F'
    total = sum(marks)
    average = total / len(marks)
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

students_list = []

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        
        # Handle form submission if JSON is missing
        if not data:
            data = {
                "name": request.form.get('name'),
                "course": request.form.get('course'),
                "subjects": [{"marks": request.form.get('marks') or 0}]
            }

        if not data or not data.get('name'):
            return jsonify({"error": "Invalid JSON or Form data"}), 400
        user_name = data.get('name')
        course = data.get('course')
        subjects = data.get('subjects', [])
        
        # Extract marks from the subject objects
        marks = [float(sub['marks']) for sub in subjects]
        
        total = calculate_total(marks)
        grade = calculate_grade(marks)
        
        students_list.append({
            "name": user_name,
            "course": course,
            "marks": marks,
            "total": total,
            "grade": grade
        })
        
        # Redirect to view if request came from a browser form
        if 'text/html' in request.headers.get('Accept', ''):
            return redirect(url_for('student'))
            
        return jsonify({"message": "Student added successfully"})

    # GET request: Return sorted list
    students_list.sort(key=lambda x: x['total'], reverse=True)
    # Render template if accessed via browser
    if 'text/html' in request.headers.get('Accept', ''):
        return render_template('student.html', students=students_list)
    return jsonify(students_list)

@app.route('/view_students')
def view_students():
    return redirect(url_for('student'))

if __name__ == "__main__":
    app.run(debug=True)