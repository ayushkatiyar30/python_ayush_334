i=int(input("enter i:"))
while(i<=5):
    i=int(input("enter i:"))
    print(i)


# break and continue


for i in range(1, 8):
    if i != 3:
       print(i)
    if i == 3:
      print("Skipping 3")
      continue
    if i == 5:
      print("Breaking at 5")
      break
for i in range(1, 15):
    print("5 x",i, " =", 5*i)
    if(i== 10):
       continue      
