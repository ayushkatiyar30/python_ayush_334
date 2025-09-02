print("SIMPLE CALCULATOR".center(100))
x= int(input("Enter your first number: "))
y= int(input("Enter your second number: "))
print("Enter 1 for addition")
print("Enter 2 for subt")
print("Enter 3 for product")
print("Enter 4 for divide")
c=int(input())
match c:
    case 1:
        print("addition of numbers is",x+y)
    case 2:
        print("subtraction of numbers is",x-y)
    case 3:
        print("product of numbers is",x*y)
    case 4:
        print("Dividion of numbers is",x/y)
    case _ if c==90:
        print("not possible")
    case _:
        print("Invalid operation")