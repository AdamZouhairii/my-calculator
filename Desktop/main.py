def sum_operation(a, b):
    return a + b

def real_division_operation(a, b):
    if b != 0:
        return a / b
    else:
        return "Errordivzero: "

def subtraction_operation(a, b):
    return a - b

def power_operation(a, b):
    return a ** b

while True:
    print("Calculator Menu:")
    print("1. Sum")
    print("2. Real Division")
    print("3. Subtraction")
    print("4. Power")
    print("5. Exit")

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
        result = power_operation(a, b)
    else:
        print("Invalid")
        continue

    print("Result:", result)
