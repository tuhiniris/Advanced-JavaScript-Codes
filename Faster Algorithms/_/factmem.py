from collections import defaultdict
import sys,time
def def_value():
    return False
    
memo = defaultdict(def_value)

tracker = 0

def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(5))

