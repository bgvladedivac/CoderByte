def ArrayAddition(array):
	max_number = max(array)
	new_array = list(sorted(array))[:-1]
	
	for i in range(0, len(new_array) - 1):
		sum = 0
		for x in range(i+1, len(new_array)):
			sum += array[x]
			if sum == max_number:
				return "true"
			
	return "false"



print ArrayAddition(raw_input())