
def numbersInPi(pi, numbers):
    global number_of_spaces
    tmp = 0
    calculate_spaces(pi, numbers, tmp)

    return number_of_spaces if number_of_spaces !=100 else -1

def calculate_spaces(pi, numbers, tmp):
    global number_of_spaces
    for i in range(len(pi)):
        curr_subpart = pi[0: len(pi) - i]
        rest_subpart = pi[len(pi) - i:]
        
        if curr_subpart in numbers:
            if curr_subpart == pi:
                number_of_spaces = min(number_of_spaces, tmp)
                #print(number_of_spaces)
                calculate_spaces(rest_subpart, numbers, 0)
            else: calculate_spaces(rest_subpart, numbers, tmp + 1)


pi = "3141592653589793238462643383279"
numbers = [[
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79"
  ], ["314159265358979323846264338327", "9"], [
    "3",
    "314",
    "49",
    "9001",
    "15926535897",
    "14",
    "9323",
    "8462643383279",
    "4",
    "793"
  ], ["3141592653589793238462643383279"], ["3141", "1512", "159", "793", "12412451", "8462643383279"], [
    "314159265358979323846",
    "327",
    "26433",
    "8",
    "3279",
    "9",
    "314159265",
    "35897932384626433832",
    "79"
  ], [
    "141592653589793238462643383279",
    "314159265358979323846",
    "327",
    "26433",
    "8",
    "3279",
    "9",
    "314159265",
    "35897932384626433832",
    "79",
    "3"
  ], [
    "3",
    "1",
    "4",
    "592",
    "65",
    "55",
    "35",
    "8",
    "9793",
    "2384626",
    "83279"
  ], [
    "3",
    "1",
    "4",
    "592",
    "65",
    "55",
    "35",
    "8",
    "9793",
    "2384626",
    "383279"
  ], [
    "3",
    "141",
    "592",
    "65",
    "55",
    "35",
    "8",
    "9793",
    "2384626",
    "383279"
  ], [
    "3",
    "141",
    "592",
    "65",
    "55",
    "35",
    "8",
    "9793",
    "23846264",
    "383279"
  ], [
    "3",
    "141",
    "592",
    "65",
    "55",
    "35",
    "8",
    "9793",
    "23846264",
    "3832798"
  ]]

for elem in numbers:
    number_of_spaces = 100
    print(numbersInPi(pi, elem))