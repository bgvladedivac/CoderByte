def are_brackets_matched(expression, left_bracket, right_bracket):
	return expression.count(left_bracket) == expression.count(right_bracket)

def get_total_occurences(expression, left_bracket, right_bracket):
	return expression.count(left_bracket) + expression.count(right_bracket)
	
def MultipleBrackets(input):
	result =  are_brackets_matched(input, "(", ")") and \
		are_brackets_matched(input, "[", "]")
		
	if result == 0:
		return 0
	
	return "1 " + str((get_total_occurences(input, "(", ")") + get_total_occurences(input, "[", "]")) // 2)
    
# keep this function call here  
print MultipleBrackets(raw_input())