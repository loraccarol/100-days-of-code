from os import system

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2

def calculator():
    continue_calculating = True
    first_number = float(input("What's the first number? "))

    while continue_calculating:

        operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
        }

        for symbol in operations:
            print(symbol)
        operation = input('Pick an operation: ')
        second_number = float(input("What's the next number? "))

        result = operations[operation](first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {result}")

        keep_going = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

        if keep_going == 'y':
            first_number = result
        else:
            continue_calculating = False
            system('cls')
            calculator()

calculator()
