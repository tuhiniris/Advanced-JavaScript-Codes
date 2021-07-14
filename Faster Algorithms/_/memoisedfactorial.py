from collections import defaultdict
import sys
def def_value():
    return False

'''
def factorial(n):
	if n<=1:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(10))
'''

cache = defaultdict(def_value)

def multiply(n):
	return (n**n)

def quick(n):
	if n not in cache:
		result = multiply(n)
		cache[n] = result		
		return result
	else:
		print("From Cache")
		return cache[n]	


# Output to File : 

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f		
	
print(quick(999))
print(quick(999))


# Output to File :
sys.stdout = orig_stdout
f.close()
