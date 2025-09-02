marks=[[85, 90, 78], [88, 92, 80], [75, 85, 90],8,"Hello"]
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])  # This will print the integer 8
print(marks[4])  # This will print the string "Hello"
if [85, 90, 78] in marks:
    print("[85, 90, 78] is present in the list.")
else:
    print("[85, 90, 78] is not present in the list.")
if "ello" in "hello":
    print("ello is present in hello.")
print(marks[:][::-1])  # This will print the entire list in reverse order
print(marks[1][2])  # This will print the third element of the second list


lst=[i*i for i in range(10)]
print(lst)
lst1=[i*i for i in range(10) if i%2==0]
print(lst1)