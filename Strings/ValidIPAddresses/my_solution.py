# O(1) time | O(1) space
def validIPAddresses(string):
    Ips = []
    for i in range(1, min(len(string), 4)):
        parts = ['', '', '', '']
        parts[0] = string[:i]
        if not isValid(parts[0]):
            continue
		
        for j in range(i + 1, i + min(len(string) - i, 4)):
            parts[1] = string[i : j]
            if not isValid(parts[1]):
                continue
				
            for k in range(j + 1, j + min(len(string) - j, 4)):
                parts[2] = string[j: k]
                parts[3] = string[k:]
				
                if isValid(parts[2]) and isValid(parts[3]):
                    Ips.append('.'.join(parts))
    return Ips
	
def isValid(string: str) -> bool:
	num = int(string)
	if num > 255:
		return False
	return len(string) == len(str(num))