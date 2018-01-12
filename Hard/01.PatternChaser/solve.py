def PatternChaser(s):
	occurences = {}
	
	for i in range(0, len(s)-1):
		check = s[i]
		for j in range(i+1, len(s)):
			check += s[j]
			
			if s.count(check) >= 2:
				occurences[check] = s.count(check)
	
	if len(list(occurences.keys())) == 0:
		return "no null"
		
	for key in sorted(occurences, key = lambda l: len(l), reverse=True):
		return "yes " + key
    
# keep this function call here  
print PatternChaser(raw_input())