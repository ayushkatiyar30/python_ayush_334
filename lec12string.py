names = "Ayush,yash"
print(len(names))
print(names[0:5])      #we use (shift+alt+ up/down) to copy paste same line
print(names[:5])        #includes 0 but not 5
print(names[2:5])
print(names[:])
print(names[:-6])     #print(names[0:(len(names)=10)-6]) =[0:4]   
for i in names:
    print(i)