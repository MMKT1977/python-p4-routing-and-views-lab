#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<int:num1>/<path:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        'div':lambda a, b: a / b,
        '%': lambda a, b: a % b
    }
    
    op_func = operations.get(operation)
    
    if op_func:
        try:
            result = op_func(num1, num2)
            
            if operation == 'div':
                return f"{result:.1f}"  
            return str(int(result) if result == int(result) else result)
        except ZeroDivisionError:
            return "Error: Division by zero!"
    else:
        return f"Error: Operation '{operation}' is not supported. Please use one of: {', '.join(operations.keys())}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
