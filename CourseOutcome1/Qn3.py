
#a)Find positive list of numbers
l1=[-5,-4,-3,-2,-1,1,2,3,4,-5,-6,-7,8,9]
l2=[x for x in l1 if x>0]
print(l2)

#b)Square of numbers
n=int(input("Enter the limit"))
print([x*x for x in range(n+1)])

#c)Form a list of vowels selected from a given word
word=input("Enter a word=")
vowels=["A","E","I","O","U","a","e","i","o","u"]
vow=[x for x in word if x in vowels]
print(vow)

#d)List ordinal value of each element
word=input("Enter a word=")
ordinal=[ord(x) for x in word]
print(ordinal)

