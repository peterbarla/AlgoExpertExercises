def minimumWaitingTime(queries):
    if len(queries) == 1:
        return queries[0]
    queries.sort()
    biggest = queries[-1]
    for i in range(len(queries) - 1, 0, -1):
        queries[i] = queries[i - 1]
    queries[0] = biggest
    summ = 0
    for i in range(1, len(queries)):
        summ += sum(queries[1: i + 1])
    return summ

print(minimumWaitingTime([3, 2, 1, 2, 6]))