choice = int(input("Enter your choice \n1.Add \n2.Subtract \n3.Multiply \n4.Divide "))
if(choice==1):
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    sum = num1+num2
    print("Sum : ",sum)
elif(choice==2):
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    sub = num1-num2
    print("Subtraction : ",sub)
elif(choice==3):
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    mul = num1*num2
    print("Multiply : ",mul)
elif(choice==4):
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    div = num1/num2
    print("Division : ",div)
else:
    print("Enter the valid choice")