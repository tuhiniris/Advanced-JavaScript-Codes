from collections import defaultdict
import sys,time

cache = defaultdict()

def multiply(n):
	return (n**n)

def quick(n):
	if n not in cache:
		#print("MISS")
		result = multiply(n)
		cache[n] = result		
		return result
	else:
		return cache[n]

for i in range(0,33000,299):
	print(quick(i)%25)

print("DONE CACHING")
time.sleep(2)

for i in range(0,33000,299):
	print(quick(i)%25)

'''
# Output to File : 

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f		
	
print(quick(999))
print(quick(999))

# Output to File :
sys.stdout = orig_stdout
f.close()
'''
