#Fibonacci series 

n=int(input("Enter the limit="))
next=0
t1=1
t2=1

if n>=1:
   print(next)
if n>=2:
   print(t2)

for x in range(3,n+1):
    print(t2)
    next=t1
    t1=t2
    t2=next+t1