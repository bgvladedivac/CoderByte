def SimpleMode(arr):
	histogram = {}
	for d in arr:
		if d in histogram:
			histogram[d] += 1
		else:
			histogram[d] = 1
			
	tuple_pairs = sorted(histogram.items(), key=lambda x: x[1])
	
	if tuple_pairs[len(tuple_pairs)-1][1] != tuple_pairs[len(tuple_pairs)-2][1]:
		return tuple_pairs[len(tuple_pairs)-1][0]
	
	max_occurence_value = tuple_pairs[len(tuple_pairs)-1][1]
	
	for d in arr:
		if histogram[d] == max_occurence_value:
			return d
    
# keep this function call here  
print SimpleMode(raw_input())