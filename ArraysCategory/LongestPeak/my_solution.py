# O(n) time | O(n) space
def longestPeak(array):
    if len(array) == 0: return 0
    peak_environment = []
    tmp_environment = [array[0]]
    
    inc = True
    dec = False
    first_change = False
    first_check = True
    inc_added = False
    dec_added = False
    for index in range(1, len(array)):
        if inc:
            if array[index] > tmp_environment[-1]:
                if first_check:
                    first_check = False
                    inc_added = True
                tmp_environment.append(array[index])
            elif array[index] < tmp_environment[-1]:
                if first_check:
                    tmp_environment.clear()
                    inc_added = False
                    dec_added = False
                    tmp_environment.append(array[index])
                    continue
                tmp_environment.append(array[index])
                inc = False
                dec = True
                first_change = True
                dec_added = True
            else:
                inc = True
                dec = False
                if len(tmp_environment) >= 3 and len(tmp_environment) >= len(peak_environment) and inc_added and dec_added:
                    peak_environment = tmp_environment[0:]
                tmp_environment.clear()
                tmp_environment.append(array[index])
                first_check = True
        elif dec:
            if array[index] > tmp_environment[-1]:
                if len(tmp_environment) >= 3 and len(tmp_environment) >= len(peak_environment) and inc_added and dec_added:
                    peak_environment = tmp_environment[0:]
                tmp_environment.clear()
                if first_change:
                    tmp_environment.append(array[index - 1])
                    first_change = False
                    dec_added = True
                tmp_environment.append(array[index])
                dec = False
                inc = True
            elif array[index] < tmp_environment[-1]:
                tmp_environment.append(array[index])
            else:
                inc = True
                dec = False
                if len(tmp_environment) >= 3 and len(tmp_environment) >= len(peak_environment) and inc_added and dec_added:
                    peak_environment = tmp_environment[0:]
                tmp_environment.clear()
                tmp_environment.append(array[index])
        if index == len(array) - 1:
            if len(tmp_environment) >= 3 and len(tmp_environment) >= len(peak_environment) and inc_added and dec_added:
                peak_environment = tmp_environment[0:]
    if not inc_added or not dec_added: return 0
    return len(peak_environment)


arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(arr))
