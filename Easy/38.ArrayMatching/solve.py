import re


def extract_digits(s):
	return [int(x) for x in re.findall(r'\d+', s)]

def ArrayMatching(strArr):

#"[5, 2, 3]", "[2, 2, 3, 10, 6]"
# Divide and conquer

# 1. Extract vsichki chisla ot masiva i da si obrazuvam nov masiv 
# samo s chislata.

# 2. Da namerq po - malkiqt masiv, da iteriram mejdu dvata i da sybera
# vsichki chisla.

# 3.Da appendna krainiqt takyv.
	first_array = extract_digits(strArr[0])
	second_array = extract_digits(strArr[1])
	min_len = min(len(first_array), len(second_array))

	result = []
	for i in range(0, min_len):
		current_sum = first_array[i] + second_array[i]
		result.append(current_sum)

	if len(first_array) < len(second_array):
		for i in range(min_len, len(second_array)):
			result.append(second_array[i])

	else:
		for i in range(min_len, len(first_array)):
			result.append(first_array[i])

	return "-".join([str(x) for x in result])
    
# keep this function call here  
print ArrayMatching(raw_input())