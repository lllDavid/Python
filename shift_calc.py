def shift_calculator():
    print("Bitwise Shift Calculator")
    print("Operations:")
    print("1. Left Shift (<<)")
    print("2. Right Shift (>>)")
    
    operation = input("Enter operation (<< or >>): ").strip()
    
    if operation not in ['<<', '>>']:
        print("Invalid operation! Please enter '<<' or '>>'.")
        return

    try:
        num = int(input("Enter the number: "))
        shift_amount = int(input("Enter the shift amount: "))
    except ValueError:
        print("Invalid input! Please enter integer values.")
        return

    if operation == '<<':
        result = num << shift_amount
        print(f"{num} << {shift_amount} = {result}")
    elif operation == '>>':
        result = num >> shift_amount
        print(f"{num} >> {shift_amount} = {result}")

shift_calculator()
