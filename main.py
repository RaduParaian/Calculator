import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is undefined."
    else: 
        return num1 / num2

def exponentiate(num1, num2):
    return num1 ** num2

def square_root(num1):
    if num1 < 0:
        return "Error: Cannot take the square root of a negative number."
    else:
        return math.sqrt(num1)

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': exponentiate
}

functions = {
    'sqrt': square_root
}

def safe_eval(expression):
    try:
        for func in functions:
            expression = expression.replace(func, f'functions["{func}"]')
        
        expression = expression.replace('^', '**')

        result = eval(expression, {"__builtins__": None}, {"math": math, "functions": functions, "operations": operations})
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."
    except Exception as e:
        return f"Error: Invalid input ({e})."

def calculator():
    print("\n**************************************************************")
    print("*********************** SUPERCALC 3003 ***********************")
    print("**************************************************************\n")
    print("///Instructions///")
    print("Operations: +, -, *, /, ^, sqrt, (, )")
    print("Type 'exit' to turn off the calculator.")
    
    while True:
        expression = input("\nEnter your calculation: ").lower()
        
        if expression == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        result = safe_eval(expression)
        print(f"Result: {result}")

calculator()