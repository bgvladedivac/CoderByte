import math

def isPerfectSquare(n):
	s = int(math.sqrt(n))
	return s*s == n

def FibonacciChecker(num):
	if isPerfectSquare(5*num*num -4) or isPerfectSquare(5*num*num +4):
		return "yes"
	return "no"
# keep this function call here  
print FibonacciChecker(raw_input())