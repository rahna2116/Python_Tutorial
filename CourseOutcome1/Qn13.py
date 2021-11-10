#Display first and last colors from the list of colors

colors=input("enter the color names separated by comma=")
list=colors.split(",")
print("first color=",list[0])
print("last color=",list[-1])