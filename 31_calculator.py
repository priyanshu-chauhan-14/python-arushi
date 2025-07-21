choice=int(input("enter your choice \1.add \2.sub \3.multi \4.div"))
if (choice==1):
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    sum=num1+num2
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
    print("multi :",multi)
elif (choice==4):
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    div= num2/num1
    print("div :", div)