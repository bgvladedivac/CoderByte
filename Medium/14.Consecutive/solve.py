def Consecutive(arr): 
    arr = list(sorted(arr))
    numbers = []

    for i in range(arr[0] + 1, max(arr)):
		 
	    if i not in arr:
			numbers.append(i)

    return len(numbers)
 
    
# keep this function call here  
print Consecutive(raw_input())