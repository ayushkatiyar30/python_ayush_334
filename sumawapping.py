a=float(input("Enter first number:"))
b=float(input("Enter Second number:"))
print("Sum of entered number is: ",a+b)
print("Before swapping a:",a,"b:",b)
a=a+b
b=a-b
a=a-b
print("After swapping a:",a,"b:",b)