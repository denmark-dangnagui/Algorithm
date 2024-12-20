def find_max_occurred_alphabet(string):

    alphbet_array = find_alphabet_occurrence_array(string)
    max_index = 0
    max_alphabet_occurrence = 0

    for index in range(len(alphbet_array)):
        if alphbet_array[index] > max_alphabet_occurrence:
            max_alphabet_occurrence = alphbet_array[index]
            max_index = index

    return chr(max_index + ord('a'))


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a') # a 일때는 97-97 이니까 인덱스 0의 값이 +1 되는 것.
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


