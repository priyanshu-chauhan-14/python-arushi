choice=int(input("enter the percentage of your marks"))
if choice>100:
    print("Bhaang khaye ho kya ")
elif choice>=90 and choice<=100:
    print("the grade A")
elif choice>=80 and choice<=89:
    print("enter the grade B")
elif choice>=70 and choice<=79:
    print("enter the grade C")
elif choice>=60 and choice<=69:
    print("enter the grade D")
else :
    print("better luck next time")