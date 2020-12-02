def underscorifySubstring(string, substring):
    first_letter_of_substr = substring[0]
    second_letter_of_substr = substring[1]
    first_index = -1
    last_index = -1
    running = False
    found = False

    substr_index = 0
    result = []

    for i in range(len(string)):
        if not running:
            if found:
                if string[i] == first_letter_of_substr:
                    #print('i')
                    substr_index = 1
                    running = True
                elif string[i] == second_letter_of_substr:
                    substr_index = 2
                    running = True
                else:
                    found = False
                    #print('fewfwefwef')
                    #print(first_index, last_index, i)
                    result.append((first_index, last_index))
            #print(string[i])
            else:
                if string[i] == first_letter_of_substr:
                    running = True
                    first_index = i
                    substr_index = 1
                #else:
                #if found:
                    #found = False
                    #print('fewfwefwef')
                    #print(first_index, last_index, i)
                    #result.append((first_index, last_index))
                    #string = string[0: first_index] + '_' + string[first_index: last_index] + '_' + string[last_index:]
        else:
            if substr_index == len(substring) - 1 and string[i] == substring[substr_index]:
                #print(string[i], substring[substr_index], substr_index,end='\n')
                #print('megvan')
                last_index = i
                found = True
                running = False
                if i == len(string) - 1:
                    result.append((first_index, last_index))
                #i -= 1
            elif string[i] == substring[substr_index]:
                #print(string[i], substring[substr_index], substr_index)
                substr_index += 1
            else:
                running = False
                if found:
                    result.append((first_index, last_index))
                found = False

    offset = 0
    print(result)
    for elem in result:
        first, second = elem
        string = string[0: first + offset] + '_' + string[first + offset: second + 1 + offset] + '_' + string[second + 1 + offset:]
        offset += 2
    return string
            

string = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc"
substr = "abc"

print(underscorifySubstring(string, substr))