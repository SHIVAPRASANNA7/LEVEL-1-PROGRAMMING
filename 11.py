# Python code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	myList = []
	for i in range(1,n+1):
		myList.append("*"*i)
	print("\n".join(myList))

n = 5
pypart(n)
