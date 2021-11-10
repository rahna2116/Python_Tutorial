
list1=[2,4,6,7,8]
list2=[7,44,5,7,9]
print(list1)
print(list2)

#(a)Check Whether list are of same length

if len(list1)==len(list2):
    print("lists have the same length")
else:
    print("List are of different length")

#check whether lists have the same length

if sum(list1)==sum(list2):
    print("Both lists have same sum")
else:
    print("Both lists have different sum")

#check if the same values occur in both

list3=[x for x in list1 if x in list2]
if len(list3)<1:
    print("No repetition of values")
else:
    print("Repeated values:",list3)