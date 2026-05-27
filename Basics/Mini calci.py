try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
except:
       print("Enter a valid number")


operator = input("Enter the operator:")
if operator == "+":
    sum = num1  + num2
    print(sum)
    
elif operator ==  "-" :
    diff = num1 - num2
    print(diff)

elif operator == "*" :
    prod = num1 * num2
    print(prod)

elif operator ==  "/" :
    try:
        div = num1 / num2 
        print (div)

    except ZeroDivisionError:
       print("Cannot divide by zero")

else :
    print("Invalid operator")