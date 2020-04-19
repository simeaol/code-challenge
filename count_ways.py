def countWays_recursively(arr, m, N): 
	pass



def countWays(arr, m, N): 

	count = [0 for i in range(N + 1)] 
	
	# base case 
	count[0] = 1
	
	for i in range(1, N + 1): 
		for j in arr: 

			if (i >= j): 
				count[i] += count[i -j] 

	return count[N] 
	
if __name__ == "__main__":
	#arr = [1, 5, 6] 
	arr = [1, 2, 3]
	m = len(arr) 
	N = 5
	print("Total number of ways = ", countWays(arr, m, N)) 
			
# This code is contributed by Anant Agarwal. 
