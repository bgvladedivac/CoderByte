import re
def get_biggest_occurence(word):
	chars_occurences = {}
	for char in word.lower():
		if char in chars_occurences:
			chars_occurences[char] += 1
		else:
			chars_occurences[char] = 1
	return max(chars_occurences.values())
def is_word_valid(word):
	chars_occurences = {}
	for char in word.lower():
		if char in chars_occurences:
			chars_occurences[char] += 1
		else:
			chars_occurences[char] = 1
	
 	for key in chars_occurences.keys():
 		if chars_occurences[key] >= 2:
 			return True
 	return False

def LetterCount(input): 
    words = re.findall(r'\w+', input)
    valid_words = []
    for word in words:
	    if is_word_valid(word):
		    valid_words.append(word)
		    
    chars_occurences = {}
    for word in valid_words:
	    chars_occurences[word] = get_biggest_occurence(word)
	
    if len(chars_occurences.values()) > 1:
        m = min(chars_occurences.values())
        ma = max(chars_occurences.values())
	
        if m == ma:
	        for word in valid_words:
		        if word in chars_occurences.keys():
			        return word

#imame edna nai - golqma stoinost, trqbva da vyrnem neinata duma.
    elif len(chars_occurences.keys()) == 1:
	    return chars_occurences.keys()[0]

    else:
	    return -1
		    
    # code goes here 
    return input
    
# keep this function call here  
print LetterCount(raw_input())