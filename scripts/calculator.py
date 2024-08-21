print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case '1':
            res = num1 + num2
        case '2':
            res = num1 - num2
        case '3':
            res = num1 * num2
        case '4':
            res = 'Error! Division by zero.' if num2 == 0 else num1 / num2
    print('Result:', res)
else:
    print("Invalid input")
