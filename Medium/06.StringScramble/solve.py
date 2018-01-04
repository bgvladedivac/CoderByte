def StringScramble(str1,str2):
	import itertools
	result = itertools.permutations([x for x in str1])
	for x in result:
		w = "".join(x)
        if w == str2:
	        return "true"
	return "false"
    
# keep this function call here  
print StringScramble(raw_input())