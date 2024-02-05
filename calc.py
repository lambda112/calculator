from os import system
operations = ["+", "-", "*", "/"]


def add(n1, n2):
    """Add two numbers together"""
    return n1 + n2


def subtract(n1,n2):
    """Subtract two numbers together"""
    return n1 - n2


def multiply(n1,n2):
    """Multiply two numbers together"""
    return n1 * n2


def divide(n1,n2):
    """Divide two numbers together. Returns 1 if number is 0"""

    if n1 == 0 or n2 == 0:
        print(f"Cannot divide by 0!")
        return 1

    return n1 / n2


calc_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculation(same_value:bool = False, calc:int = 0):
    
    while True:
        try:
            if same_value:
                n1 = calc
                n2 = int(input("Enter second number: "))
                break

            else:
                n1 = int(input("Enter first number: "))
                n2 = int(input("Enter second number: "))
                break

        except ValueError:
            print("Enter a number please!\n")


    operator = input("Enter an operator\n+\n-\n*\n/\n: ")

    while True:
        if operator in operations:
            break
        else:
            operator = input("Enter a valid operator\n+\n-\n*\n/\n: ")

    calc = calc_dict[operator](n1, n2)
    print(f"{calc}\n") 
    return calc


calc = calculation()
while True:

    finished = input(f"Type 'y' to continue calculating with {calc} or 'n' to start new calculation: ")

    while finished not in ["y", "n"]:
        finished = input(f"Type 'y' to continue calculating with {calc} or 'n' to start new calculation: ")

    if finished == "y":
        calc = calculation(True, calc)

    else:
        system("cls")
        calc = calculation()