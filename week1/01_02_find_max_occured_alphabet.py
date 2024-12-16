print(ord('a')) # 문자(아스키)를 숫자로
print(chr(97)) # 숫자를 문자(아스키)로
def find_max_occurred_alphabet(string):

    alphabet_array = find_alphabet_occurrence_array(string)
    max_occurred_alphabet = 0
    max_occurred_alphabet_index = 0

    for index in range(len(alphabet_array)):
        alphabet_occurrence = alphabet_array[index]

        if alphabet_occurrence > max_occurred_alphabet:
            max_occurred_alphabet = alphabet_occurrence
            max_occurred_alphabet_index = index

    return chr(max_occurred_alphabet_index + ord('a'))



def find_alphabet_occurrence_array(string) :
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1
    return alphabet_occurrence_array


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))