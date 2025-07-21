# This is the program to demonstrate type casting 
# Type casting means changing the data type of one variable into another 

#-------------------------------------------------------------------------------------------------------
# String into integer or float 
print("String into integer or float")
a = " 345 "
print(type(a))
# str ---> int
a = int(a)
print(type(a)) # Successfully converted
# str ---> float 
a = float(a)
print(type(a)) # Successfully converted

'''
b = "34a5"
b = int(b)
print(type(b)) Unsuccessful because it cannot be converted into integer 
'''

#-------------------------------------------------------------------------------------------------------
#float to string   
print("\nFloat to string ")
a = 3452.45657
print(type(a))
a = str(a)
print(type(a))

#--------------------------------------------------------------------------------------------------------
#Integer to String   
print("\nFloat to String ")
a = 3452.45657
print(type(a))
a = str(a)
print(type(a))

#--------------------------------------------------------------------------------------------------------
# String  to Boolean
print("\nBoolean to String ")
a = ""
print(type(a))
a = bool(a)
print(type(a))
print(a)