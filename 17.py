
def swapList(list):
	
	first = list.pop(0)
	last = list.pop(-1)
	
	list.insert(0, last)
	list.append(first)
	
	return list
	
newList = [7, 45, 18, 17, 8]

print(swapList(newList))
