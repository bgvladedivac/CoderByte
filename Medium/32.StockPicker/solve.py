def StockPicker(arr):
	best = 0
	for i in range(0, len(arr)-1):
		for j in range(i+1, len(arr)):
			if arr[j] - arr[i] > best:
				best = arr[j] - arr[i]
	if best > 0:
		return best
	return - 1
    
# keep this function call here  
print StockPicker(raw_input())