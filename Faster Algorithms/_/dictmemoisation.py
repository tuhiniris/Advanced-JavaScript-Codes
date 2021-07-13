import collections

def def_value():
    return False
    
memo = collections.defaultdict(def_value)
for i in range(5):
	memo[i] = True
