def DistinctList(arr):
	dictionary = { }
	values = list(set(arr))
	for v in values:
		dictionary[v] = 0
	
	for each in arr:
		dictionary[each] += 1
	
	result = 0
	
	for value in dictionary.values():
		if value == 2:
			result += 1
		elif value > 2:
			result += (value-1)
			
	return result
    
# keep this function call here  
print DistinctList(raw_input())