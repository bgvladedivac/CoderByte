def LargestPair(num):
	str_num = str(num)
	biggest = int(str_num[0:2])
	 
	l = len(str_num)
	for i in range(1, l-1):
		number = str_num[i:i+2]

		if number > biggest:
			biggest = number

	return biggest
# keep this function call here  
print LargestPair(raw_input())