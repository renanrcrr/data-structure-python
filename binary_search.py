def binary_search(list, key, ini, end):
	if ini > end:
		return False

	middle = (ini + end) // 2

	if key == list[middle]:
		return True
		
	if key < list[middle]:
		return binary_search(list, key, ini, middle - 1)
		
	return binary_search(list, key, middle + 1, end)

list = [11, 5, 10, 20, 15, 4]

key = 15

list.sort()

if binary_search(list, key, 0, len(list) - 1) == True:
	print('Found')

else:
	print('Did not find')