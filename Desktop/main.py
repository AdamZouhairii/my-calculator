def sum_operation(a, b):
    return a + b

def real_division_operation(a, b):
    if b != 0:
        return a / b
    else:
        return "Errordivzero: "

def subtraction_operation(a, b):
    return a - b

def pow(2, b):
    return a ** b

while True:
    print("Calculator Menu:")
    print("Sum")
    print("Real Division")
    print("Subtraction")
    print("Power")
    print("Exit")

    choice = input("Enter your choice : ")

    if choice == '5':
        print("Exiting")
        break

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid")
        continue

    if choice == '1':
        result = sum_operation(a, b)
    elif choice == '2':
        result = real_division_operation(a, b)
    elif choice == '3':
        result = subtraction_operation(a, b)
    elif choice == '4':
        result = pow(a, b)
    else:
        print("Invalid")
        continue

    print("Result:", result)
