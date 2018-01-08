def generate_set(sp, ep):
	return [x for x in range(sp, ep+1)]
			
def OverlappingRanges(arr):
	first_set = generate_set(arr[0], arr[1])
	second_set = generate_set(arr[2], arr[3])
	
	result = arr[4] <= len([x for x in first_set if x in second_set])
	return "true" if result else "false"
    
# keep this function call here  
print OverlappingRanges(raw_input())