string=list()
a=int(input("Enter the no of total strings you want: "))
z=int(input("How much string do you want to concatenate each at a time: "))
for x in range(a):
	n=input("Enter a string : ")
	string.append(str(n))
print("Arrray",string)
b=""
for y in range(a):
	b=b+string[y]
	if((y+1)%z==0)://palindrome
		print("Original word : ",b)
		c=b[::-1]
		print("Reversed word : ",c)	
		if(b==c):
			print("The Concatenated words produce a Palindrome")
		else:
			print("The Concatenated words do not produce a Palindrome")
		b=""

