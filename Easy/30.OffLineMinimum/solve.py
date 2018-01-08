def OffLineMinimum(strArr):
	digits = []
	subset = []
	
	for s in strArr:
		if s.isdigit():
			digits.append(s)
		elif s == "E":
			subset.append(min(digits))
			digits.remove(min(digits))
		
	return ",".join(subset)
    
# keep this function call here  
print OffLineMinimum(raw_input())