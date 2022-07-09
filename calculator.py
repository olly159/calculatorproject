from art import logo

def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("whats the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operational_symbol = input("pick the operation: ")
        num2 = float(input("whats the second number?: "))
        calculation_function = operations[operational_symbol]
        answer = calculation_function(num1, num2)


        print(f"{num1} {operational_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()