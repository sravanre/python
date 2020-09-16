# ZeroDivisionError
try:
    num1 = int(input("Enter number1 :"))
    num2 = int(input("Enter number2 :"))

    result=num1/num2
    print("result of division", result)
except ZeroDivisionError as ze:
    print("Problem in division: ",ze)

except ValueError as ve:
    print("value erro")
    print(ve)
    

