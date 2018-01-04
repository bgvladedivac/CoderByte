def PalindromeTwo(s):
	result = "".join([x.lower() for x in s if x.isalpha()])
	if result == result[::-1]:
		return "true"
	return "false"
    
# keep this function call here  
print PalindromeTwo(raw_input())