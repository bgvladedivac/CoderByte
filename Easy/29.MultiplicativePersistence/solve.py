def MultiplicativePersistence(num):
	n = str(num)
	
	if len(n) == 1:
		return 0
		
	digits = [int(x)  for x in n]
	result = 1
	for d in digits:
		result = result * d
	
	return 1 + MultiplicativePersistence(result)
# keep this function call here  
print MultiplicativePersistence(raw_input())