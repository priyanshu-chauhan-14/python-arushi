
while(True):
    choice = int(input("Enter your choice \n1.Add \n2.Subtract \n3.Multiply \n4.div \n5.Exit "))
    if (choice==1):
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        sum= num1+num2
        print("sum :",sum)
    elif (choice==2):
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        sub= num2-num1
        print("sub :",sub)
    elif (choice==3):
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        multi= num1*num2
        print("multiply is",multi)
    elif (choice==4):
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        division=num1/num2
        print("division is",division)
    elif(choice==5):
        print("Exiting")
        break
    else:
        print("Enter the valid number")