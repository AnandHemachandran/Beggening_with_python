string=list()
a=int(input("Enter the no of strings you want to concatenate : "))
for x in range(a):
	n=input("Enter a string : ")
	string.append(str(n))
print("Arrray",string)
b=""
for y in range(a):
	b=b+string[y]
	if((y+1)%3==0):
		print("Original word : ",b)
		c=b[::-1]
		print("Reversed word : ",c)	
		if(b==c):
			print("The Concatenated words produce a Palindrome")
		else:
			print("The Concatenated words do not produce a Palindrome")
		b=""

