#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’

str=input("enter a string=")

if str[-3:]=="ing":
    print(str+"ly")
else:
    print(str+"ing")


