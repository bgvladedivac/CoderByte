def TripleDouble(num1, num2):
	num1s = str(num1)

	for x in range(0, len(num1s) - 2):
		elements = list(set(num1s[x:x+3]))

		if len(elements) == 1:
			num2s = str(num2)
			for y in range(0, len(num2s) - 1):
				elements2 = list(set(num2s[y:y+2]))

				if len(elements2) == 1 and elements2[0] == elements[0]:
					return 1

	return 0
    
# keep this function call here  
print TripleDouble(raw_input())