# O(capacity*len(items)) time | O(capacity) space
import copy
def knapsackProblem(items, capacity):
    weights = [elem[1] for elem in items]
    values = [elem[0] for elem in items]
    prev_caps = [[0, []] for i in range(capacity + 1)]
    curr_caps = [[0, []] for i in range(capacity + 1)]

    for i in range(len(weights)):
        for j in range(len(curr_caps)):
            if weights[i] <= j:
                if values[i] + prev_caps[j - weights[i]][0] >= prev_caps[j][0]:
                    curr_caps[j][0] = values[i] + prev_caps[j - weights[i]][0]
                    curr_caps[j][1] = list([i] + prev_caps[j - weights[i]][1])
                else:
                    curr_caps[j][0] = prev_caps[j][0]
                    curr_caps[j][1] = prev_caps[j][1][0:]
        prev_caps = copy.deepcopy(curr_caps)

    return curr_caps[-1]


items = [[1, 2], [4, 3], [5, 6], [6, 7]]
cap = 10

print(knapsackProblem(items, cap))