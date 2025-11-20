num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print (f"Entered {num1} value is greater")
elif num2 > num1 and num2 > num3:
    print (f"Entered {num2} value is greater ")
elif num3 > num1 and num3 > num2:
    print (f"Entered {num3} value is greater ")
elif num1 == num2 and num2 == num3:
    print ("Entered numbers ere equal")