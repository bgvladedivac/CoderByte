def BitwiseOne(strArr):
	result = ""
	for i in range(0, len(strArr[0])):
		if strArr[0][i] == "0" and strArr[1][i] == "0":
			result += "0"
		else:
			result += "1"
	return result
    
# keep this function call here  
print BitwiseOne(raw_input())