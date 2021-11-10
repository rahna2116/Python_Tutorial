#sum of the items in a list
list=input("enter the numbers separated with commas=")
list1=list.split(",")


sum=0
print("list elements are...")
print(list1)

for x in list1:
    sum=sum+int(x)
print("sum of all items in a list=",sum)
