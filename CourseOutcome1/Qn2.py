a=int(input("Enter any year="))
b=int(input("Enter the present year="))

while (b<=a):
    if b%100==0:
        if b%400==0:
            print(b)
    elif b%4==0:
        print(b)
    b+=1
