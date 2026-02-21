l=[1,2,3]
#add method
#append
l.append(4)
print(l)
#insert
l.insert(0,0)
print(l)
#extend
l.extend([5,6])
print(l)
#remove method
l.remove(2)
#pop
l.pop()
print(l)
l.pop(0)
print(l)
#del:remove by index
del l[1]
print(l)
#clear:remove all elements
l.clear()
print(l)
l=[6,2,1,4,5]
#sort
l.sort()
print(l)
#reverse
l.reverse()
print(l)
l=[1,2,3]
rev=l[::-1] #slicing
print(rev)


