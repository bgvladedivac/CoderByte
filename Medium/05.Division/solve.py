def Division(num1,num2): 
    gcd = 1
    for i in range(1, num2 +1):
		if num1 % i == 0 and num2 % i == 0 and i > gcd:
			gcd = i
    return gcd
# keep this function call here  
print Division(raw_input())