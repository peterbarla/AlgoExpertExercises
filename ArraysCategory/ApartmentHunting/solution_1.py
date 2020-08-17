# O(ba) time | O(ba) where b =  number of block and a = number of attributes
def apartmentHunting(blocks, reqs):
    building_distances = []
    for req in reqs:
        building_distances.append(get_distances_for_req(req, blocks))

    best_block_area = -1
    min_distance = float('inf')
    for index in range(len(blocks)):
        max_distance = -1
        for building in building_distances:
            max_distance = max(max_distance, building[index])
        if max_distance < min_distance:
            min_distance = max_distance
            best_block_area = index

    return best_block_area



def get_distances_for_req(req, blocks):
    distances = [float('inf') for i in range(len(blocks))]

    for index, block in enumerate(blocks, 0):
        if block[req]:
            distances[index] = 0
        else:
            if index - 1 >= 0:
                if distances[index - 1] != float('inf'):
                    distances[index] = distances[index - 1] + 1

    for index in range(len(distances) - 2, -1, -1):
        if distances[index] != float('inf') and distances[index + 1] < distances[index]:
            distances[index] = distances[index + 1] + 1
        elif distances[index] == float('inf'):
            distances[index] = distances[index + 1] + 1
            
    return distances

blocks = [
    {"gym": False, "office": True, "school": True, "store": False},
    {"gym": True, "office": False, "school": False, "store": False},
    {"gym": True, "office": False, "school": True, "store": False},
    {"gym": False, "office": False, "school": True, "store": False},
    {"gym": False, "office": False, "school": True, "store": True}
  ]
reqs = ["gym", "office", "school", "store"]


print(apartmentHunting(blocks, reqs))