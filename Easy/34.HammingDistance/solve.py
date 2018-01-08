def HammingDistance(strArr): 
	counter = 0
	for i in range(0, len(strArr[0])):
		if strArr[0][i] != strArr[1][i]:
			counter += 1
	return counter
    
# keep this function call here  
print HammingDistance(raw_input())