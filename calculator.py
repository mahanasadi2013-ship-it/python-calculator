while True:
    num1 = float(input("First Number: "))
    mo = input("Mathemical Operator: ")
    num2 = float(input("Second Number: "))
    print("—" * 41)
    if mo == "+":
        print(num1 + num2)
    
    elif mo == "-":
        print(num1 - num2)
