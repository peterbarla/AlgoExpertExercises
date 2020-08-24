# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    new_string = []
    for i in range(len(string)):
        if abc.index(string[i]) + key > len(abc) - 1:
            how_many_times = (abc.index(string[i]) + key) //len(abc)
            index = (abc.index(string[i]) + key) - how_many_times*len(abc) - 1
            new_string.append(abc[index + 1])
        else: new_string.append(abc[abc.index(string[i]) + key])
    return ''.join(new_string)

string = 'ovmqkwtujqmfkao'
key = 52
print(caesarCipherEncryptor(string, key))