# O(w*n*log(n)) | O(w*n) where w = number of words and n is the longest string`s length
def groupAnagrams(words):
    cache = {}
    result = [[] for i in range(len(words))]

    index = -1
    for i in range(len(words)):
        curr_word = words[i]
        letter_list = [letter for letter in curr_word]
        letter_list.sort()
        letter_list = tuple(letter_list)

        if letter_list not in cache:
            index += 1
            cache[letter_list] = index
            result[index].append(curr_word)
        else:

            result[cache[letter_list]].append(curr_word)

    final_result = []
    for elem in result:
        if len(elem) > 0:
            final_result.append(elem)
    return final_result

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

print(groupAnagrams(words))