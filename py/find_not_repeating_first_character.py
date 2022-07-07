input = "abacabade"

# 빈도수찾기
# 빈도수를 저장해야함

# def find_not_repeating_character(string):
#     alphabet_occurrence_arr = [0]*26
#     for char in string:
#         if not char.isalpha():
#             continue
#         # char 가 알파벳이 아니라면 다음으로 넘어간다
#         # continue : 반복문의 다음 인덱스로 넘어가게 하는 방법.
#         arr_index = ord(char) - ord("a")
#         alphabet_occurrence_arr[arr_index] += 1
#     return "_"

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"


result = find_not_repeating_character(input)
print(result)