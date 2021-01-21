def taskAssignment(k, tasks):
    tasks.sort()
    left = 0
    right = len(tasks) - 1
	
    result = []
    while left < right:
        result.append([left, right])
        left += 1
        right -= 1

    maxx = 0
    for elem in result:
        if tasks[elem[0]] + tasks[elem[1]] > maxx:
            maxx = tasks[elem[0]] + tasks[elem[1]]
    return result

print(taskAssignment(3, [1, 3, 5, 3, 1, 4]))