# O(n^2) time | O(n) space
def arrayOfProducts(array):
    result = []
    
    for i in range(len(array)):
        result.append(product(array[0:i] + array[i + 1: len(array)]))
    return result
    
def product(array: list) -> int:
	prod = 1
	for elem in array:
		prod *= elem
	return prod