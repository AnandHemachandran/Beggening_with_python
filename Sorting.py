number=list()
a=int(input("Enter the total no of inputs "))
for x in range(a):
	n=input("Enter a number: ")
	number.append(int(n))
print("Array :",number)
for i in range(a):
	for j in range(i+1,a):
		if (number[i]>number[j]):
			number[i], number[j] = number[j], number[i]
		
print (number)
