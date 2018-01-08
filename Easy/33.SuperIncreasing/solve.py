def Superincreasing(arr):
	for x in range(0, len(arr)-1):
		s = sum(arr[0:x+1])
		if arr[x+1] <= s:
			return "false"
	return "true"
    
# keep this function call here  
print Superincreasing(raw_input())