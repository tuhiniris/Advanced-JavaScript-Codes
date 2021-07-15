import sys,time,collections,itertools

def def_value():
    return False
    
memo = collections.defaultdict(def_value)
tracker = 0

def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(5))

arr = ['A','B','C']
x = list(itertools.accumulate(arr))
print(x)
