# O(n^2) time | O(n) space
def diskStacking(disks):
    
    disks.sort(key=take_third)

    heights = [elem[2] for elem in disks]
    
    for i in range(len(heights)):
        for j in range(0, i):
            if is_bigger(disks[i], disks[j]):
                heights[i] = max(heights[i], disks[i][2] + heights[j])

    biggest_value = max(heights)
    biggest_value_index = heights.index(biggest_value)
    
    result = []
    while biggest_value > 0:
        result.append(disks[biggest_value_index])
        biggest_value = biggest_value - disks[biggest_value_index][2]
        if biggest_value != 0:
            biggest_value_index = heights.index(biggest_value)

    return result[::-1]

def take_third(elem):
    return elem[2]

def is_bigger(elem1, elem2):
    return elem1[0] > elem2[0] and elem1[1] > elem2[1] and elem1[2] > elem2[2]

disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
print(diskStacking(disks))