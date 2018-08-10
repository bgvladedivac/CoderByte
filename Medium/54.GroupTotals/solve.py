def GroupTotals(strArr): 
	d = {}

	for x in strArr:
		key, value = x.split(":")
		
		if key in d:
			d[key] += int(value)
		else:
			d[key] = int(value)

	d = {k: v for k,v in d.items() if v != 0}
	sd = sorted(d.items())

	result = []

	for k, v in sd:
		result.append(k+":"+str(v))

	return ",".join(result)
# Divide and conquer
# get the keys and values, remove the 0's/ sort out the output in specific format

print(GroupTotals(["B:-1", "A:1", "B:3", "A:5"]))
print(GroupTotals(["X:-1", "Y:1", "X:-4", "B:3", "X:5"]))
#print(GroupTotals(["Z:0", "A:-1"]))
