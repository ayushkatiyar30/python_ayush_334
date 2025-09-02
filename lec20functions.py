def add(a,b=5): #yahan b default argument hai agr kuch nhi denge tobydefault b 5 ho jayega
     print(a+b)
# print("Enter the value of a:",end="")
# a=int(input())
# # print("Enter the value of b:",end="")
# # b=int(input())

# add(a)
# def name(fname,mname="bal",lname="pal"):
#     print("heyy",fname,mname,lname)
# name("lal","singh")
def average(*nums):
    total = sum(nums)
    count = len(nums)
    return total / count if count > 0 else 0
# nums = [10, 20]
print(average(40, 5))
def name(*names):
    for i in range(len(names)):
        print("heyy", names[i])
name("lal","singh","pal","sharma")

