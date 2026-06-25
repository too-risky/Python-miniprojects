# Python Calculator 

print("Welcome to the Python Calculator!")
operator = input("Select an operation {+ for addition, - for subtraction, * for multiplication, / for division}: ")
num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))

if operator == '+' : 
    result = num1 + num2
    print(round(result, 3))
elif operator == '-' : 
    result = num1 - num2
    print(round(result, 3))
elif operator == '*' :
    result = num1 * num2
    print(round(result, 3))
elif operator == '/' :
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    elif operator == '/' :
        result = num1 / num2
        print(round(result, 3))
else :
    print("Invalid operator. Please select a valid operation.")
