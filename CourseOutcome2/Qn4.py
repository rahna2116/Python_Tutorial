
upper=int(input("Enter the upper limit="))
lower=int(input("Enter the lower limit="))
list=[]
list1=[]

for x in range(lower, upper + 1):
    if x % 2 == 0:
        list.append(x)

for y in list:
    for z in range(1,y):
          if (z*z) ==y:
             list1.append(y)
print(list1)

