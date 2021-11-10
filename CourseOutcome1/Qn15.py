#Print out all colors from color-list1 not contained in color-list2.

list1=["violet","yellow","blue","white","black"]
list2=["violet","black","orange","green","yellow"]

print(list1)
print(list2)
print("Colors from list1 but not in list2")
print([x for x in list1 if x not in list2])
