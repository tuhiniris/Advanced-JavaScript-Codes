from collections import defaultdict
def def_value():
    return False

def uniqSort(arr):
	memo = defaultdict(def_value)
	result = []
	
	for i in range(len(arr)):
		if memo[arr[i]]==False:
			result.append(arr[i])
			memo[arr[i]]=True
	
	#print(memo)
	result.sort()
	return(result)
	
ans = uniqSort([4,2,2,3,2,2,2])
print(ans)
