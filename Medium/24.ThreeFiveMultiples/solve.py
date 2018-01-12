def ThreeFiveMultiples(num):
	result = 0
	for i in range(1, num):
		if i % 3 == 0:
			result += i
		elif i % 5 == 0:
			result += i
	return result
    
# keep this function call here  
print ThreeFiveMultiples(raw_input())