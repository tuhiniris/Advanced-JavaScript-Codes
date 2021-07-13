import collections

def def_value():
    return False
    
memo = collections.defaultdict(def_value)
for i in range(5):
	memo[i] = True

print(memo[2])
memo[2]=False
print(memo[2])
