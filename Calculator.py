def calculate(num1, operator, num2):
    if operator == "+":
        print(num1,"+",num2, "is", num1 + num2)
    elif operator == "-":
        print(num1,"-",num2, "is", num1 - num2)
    elif operator == "*":
        print(num1,"*",num2, "is", num1 * num2)
    elif operator == "^":
        print(num1,"^",num2, "is", num1 ** num2)
    elif operator == "/":
        if num2 != 0:
            print(num1,"/",num2, "is", num1 / num2)
        else:
            print("Error: Division by zero!")
    else:
        print("Error: Invalid operator entered!")
        
num1 = float(input("Enter the first number: "))
operator = input("Enter the arithmetic operator (+, -, *, /,^): ")
num2 = float(input("Enter the second number: "))
calculate(num1, operator, num2) # it can run too when writen as "calculate()"


