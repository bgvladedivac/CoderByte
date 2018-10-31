# Divide and conquer
# if any two numbers excluding the first element
# in the array can sum up to the first 
# element in the array.
# Permutations sounds 
# target_number = 17
# 4 5  | 4 6 | 5 6 | 10 | 11  | 
# 1 2 3 
#
#
# 1 2   2 3    1 3    2 1  3 2    !n - 1
#

import itertools

def TwoSum(arr):
	permutations_of_2 = list(itertools.combinations(arr[1:], 2))
	target_number = arr[0]

	pairs = []
	for permutation in permutations_of_2:
		if sum(permutation) == target_number:
			pairs.append(permutation)

	
	if len(pairs) == 0:
		return - 1

	result = ""

	tuples_in_strings = []
	for each_tuple in pairs:
		first_el = str(each_tuple[0])
		second_el = str(each_tuple[1])
		tuples_in_strings.append(",".join([first_el, second_el]))


	return " ".join(tuples_in_strings)
#first_input = [17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]
second_input = [7, 6, 4, 1, 7, -2, 3, 12]

#print(TwoSum(first_input)) # 6,11 10,7 15,2
print(TwoSum(second_input)) # 6,1 4,3