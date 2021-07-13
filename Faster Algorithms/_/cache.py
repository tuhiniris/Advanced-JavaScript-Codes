def isUnique(arr):
	memo = {}
	result = True
	for i in range(len(arr)):
		print(memo)
		print("Loop : ",i)
		if (memo[arr[i]]):
			result = False
		else:
			memo[arr[i]] = True
	return result			


val = [1,2,3]
print(isUnique(val))
