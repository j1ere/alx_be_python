num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operator = input("Choose the operation (+, -, *, /):")

match operator:
    case "+":
        print(f"The result is {num1+num2}.")
    case "-":
        print(f"The result is {num1-num2}.")
    case "*":
        print(f"The result is {num1*num2}.")
    case "/":
        try:
            print(f"The result is {num1/num2}")
        except:
            print("Cannot divide by zero.")
    case _ :
        print("ERROR! unrecorgnized operator.")