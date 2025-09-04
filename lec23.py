l=[32,1,34,24,3,7,5]
print(l)
l.append(4)   #append adds an element to the end of the list
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)

l.reverse()
print(l)
print(l.index(24))  #gives the index of the first occurrence of the element
l.insert(2,100)  #inserts 100 at index 2
print(l)