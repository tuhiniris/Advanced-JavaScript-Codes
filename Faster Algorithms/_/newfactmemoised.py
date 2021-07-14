from collections import defaultdict
import sys,time
def def_value():
    return False
    
memo = defaultdict(def_value)

tracker = 0

def callMe(n):	
	global tracker
	tracker+=1
	print(tracker)
	if(tracker==n):
		return 'loops!'		
	return (callMe(n))

print(callMe(10))


'''
def factorial(n):
	if n<=1:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(10))
'''

