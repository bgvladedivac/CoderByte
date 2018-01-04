def BinaryConverter(s):
	result = [int(x) for x in s[::-1]]
	base = 2
	r = 0
	
	for i in range(0, len(result)):
		if result[i] == 1:
			r += base ** i
	return r
    
# keep this function call here  
print BinaryConverter(raw_input())