def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operations = ["+", "-", "*", "/"]

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operator = input("Enter an operator\n+\n-\n*\n/\n: ")

calc_dict = {
    "+" : add(n1, n2),
    "-" : subtract(n1, n2),
    "*" : multiply(n1,n2),
    "/" : divide(n1,n2)
}

while True:
    if operator in operations:
        break
    else:
        operator = input("Enter a valid operator\n+\n-\n*\n/\n: ")

calc = calc_dict[operator]
print(calc)
