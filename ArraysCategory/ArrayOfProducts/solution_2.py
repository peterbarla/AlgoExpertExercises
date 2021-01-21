# O(n) time | O(n) space
def arrayOfProducts(array):
    left = [1 for _ in range(len(array))]
	right = [1 for _ in range(len(array))]
	result = [1 for _ in range(len(array))]
	
	prod = 1
	for i in range(len(array)):
		left[i] = prod
		prod *= array[i]
	
	prod = 1
	for i in reversed(range(len(array))):
		right[i] = prod
		prod *= array[i]
		
	for i in range(len(array)):
		result[i] = left[i] * right[i]
	
    return result