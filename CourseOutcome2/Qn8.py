#Accept a list of words and return length of longest word
list=[]
length=[]
for x in range(0,5):
    w=input("enter the word=")
    length.append(len(w))
    list.append(w)
print(list)
print("length of longest word=",max(length))
