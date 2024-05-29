print("Hello world!")
def deciToBy():
	n = 10
	list = []
	while n != 0:
		rem = n%2
		list.append(rem)
		n = n//2
		#print(rem)
	print(list[::-1])
deciToBy()
