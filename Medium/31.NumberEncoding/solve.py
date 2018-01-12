def NumberEncoding(s):
	import string
	alphabet = [x for x in string.ascii_lowercase]
	
	result = ""

	for char in s.lower():
		if char.isalpha():
			result += str(alphabet.index(char) + 1)
		else:
			result += char

	return result
    
# keep this function call here  
print NumberEncoding(raw_input())