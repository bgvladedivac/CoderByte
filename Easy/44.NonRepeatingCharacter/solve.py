def get_set_of_an_array(array):
	result = []

	for x in array:
		if x not in result:
			result.append(x)

	return result

def NonrepeatingCharacter(input):
	no_space = [x for x in input if x != " "]
	no_space_chars = get_set_of_an_array(no_space)

	occurences = {}

	for x in no_space:
		if x in occurences:
			occurences[x] += 1
		else:
			occurences[x] = 1

	for x in no_space_chars:
		if x in occurences and occurences[x] == 1:
			return x
    
# keep this function call here  
print NonrepeatingCharacter(raw_input())