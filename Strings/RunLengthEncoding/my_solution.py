# O(n) time | O(1) space
def runLengthEncoding(string):
    result = ''
    index = 0
    while index < len(string):
        res, string = runLength(index, string)
        result += res
    return result

		
def runLength(index: int, string: str):
    counter = 1
    elem = string[index]
    reso = ''
    while index < len(string) - 1 and counter < 9:
        if string[index + 1] == elem:
            counter += 1
            index += 1
        else:
            index += 1
            reso += str(counter) + elem
            return reso, string[index:]
    reso += str(counter) + elem
    return reso, string[index + 1:]

print(runLengthEncoding('AAAAAAAAAAAAABBCCCCDD'))