# O(ba ^ 2) time | O(ba) space where b =  number of block and a = number of attributes
import copy
def apartmentHunting(blocks, reqs):
    building_distances_for_blocks = []
    for block in blocks:
        building_distances_for_blocks.append(copy.deepcopy(block))

    for index, b in enumerate(building_distances_for_blocks, 0):
        for key, value in b.items():
            if not blocks[index][key]:
                b[key] = float('inf')
            else:
                b[key] = 0



    for index1, block in enumerate(building_distances_for_blocks, 0):
        for key, value in block.items():
            for index2, b in enumerate(blocks, 0):
                if block[key] != 0:
                    if b[key]:
                        if abs(index2 - index1) < block[key]:
                            block[key] = abs(index2 - index1)
        
    distance = float('inf')
    result_index = -1
    for index, b in enumerate(building_distances_for_blocks, 0):
        block_max = float('-inf')
        for key, value in b.items():
            if key in reqs:
                block_max = max(b[key], block_max)
        if block_max < distance:
            distance = block_max
            result_index = index
    
    return result_index
             
blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True}
  ]

reqs = ["gym", "school", "store"]


print(apartmentHunting(blocks, reqs))