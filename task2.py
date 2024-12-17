def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
       
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        choice = input("Enter the operation (1/2/3/4 or +, -, *, /): ").strip()

        
        if choice in ['1', '+']:
            result = num1 + num2
            operation = '+'
        elif choice in ['2', '-']:
            result = num1 - num2
            operation = '-'
        elif choice in ['3', '*']:
            result = num1 * num2
            operation = '*'
        elif choice in ['4', '/']:
            if num2 != 0:
                result = num1 / num2
                operation = '/'
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operation. Please try again.")
            return

        
        print(f"Result: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


calculator()