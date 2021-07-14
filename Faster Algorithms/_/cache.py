from collections import defaultdict

def def_value():
    return False

def isUnique(arr):
	memo = defaultdict(def_value)
	result = True	
	for i in range(len(arr)):	
		if(memo[arr[i]]==True):
			result = False
			break			
		else:
			memo[arr[i]] = True
	return result			


val = ['a','b','b','d']
print(isUnique(val))
             
