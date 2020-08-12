# O(n) time | O(1) space
def longestPeak(array):
    longest_peak_length = 0
    for i in range(1, len(array) - 1):
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        
        if not isPeak:
            continue
        print(array[i - 1], array[i], array[i + 1])
        curr_peak_length = 3
        
        for j in range(i - 2, -1, -1):
            if array[j + 1] > array[j]:
                curr_peak_length += 1
            else: break
                
        for j in range(i + 1, len(array) - 1):
            if array[j] > array[j + 1]:
                curr_peak_length += 1
            else: break
                
        if curr_peak_length > longest_peak_length:
            longest_peak_length = curr_peak_length
            
    return longest_peak_length

arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(arr))