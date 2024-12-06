from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def subtract (n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

calculator_dictionary = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}
def calculator():
    print(logo)
    should_accumulate = True
    first_number = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in calculator_dictionary:
            print(symbol)
        operation = input("Pick an operation: ")
        second_number = float(input("What's the second number?: "))
        answer = calculator_dictionary[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {answer}")


        continue_calculations = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ").lower()
        if continue_calculations == "y":
            first_number = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()