######## 최댓값찾기
# input = [3, 5, 6, 1, 2, 4]
# 지정변수 max
# def find_max_num(array):
#     # 이 부분을 채워보세요!
#     max = 0
#     for x in input:
#         if x > max:
#             max = x
#     return max
# result = find_max_num(input)
# print(result)

# input = [3, 5, 6, 1, 2, 4]
# # 이중 for문
# def find_max_num(array):
#     # 이 부분을 채워보세요!
#     for num in array:
#         for compare_num in array:
#             if num < compare_num:
#                 break
#         else:
#             return num
#         # for - else : for문이 끝날때까지 한번도 break 안나오면 else가 실행
# result = find_max_num(input)
# print(result)


######### 글자중 최빈값찾기
# replace로 공백제거
# ord()로 아스키값 받아서 alphabet_occurrence_array 에 넣어주기
# for 문으로 alphabet_occurrence_array 돌면서 최대값 찾기

input = "hello my name is sparta"
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0]*26
    onlystring = string.replace(" ","")
    for str in onlystring:
        alphabet_occurrence_array[ord(str)-ord('a')] += 1
    max_occurred = 0
    for num in alphabet_occurrence_array:
        if num > max_occurred:
            max_occurred = num
    print(alphabet_occurrence_array)
    index_of_max_occurred = alphabet_occurrence_array.index(max_occurred)
    return chr(index_of_max_occurred + ord('a'))
result = find_max_occurred_alphabet(input)
print(result)


# input = "hello my name is sparta"


# def find_max_occurred_alphabet(string):
#     alphabet_occurrence_array = [0]*26
#     for char in string:
#         if not char.isalpha():
#             continue
#         # char 가 알파벳이 아니라면 다음으로 넘어간다
#         # continue : 반복문의 다음 인덱스로 넘어가게 하는 방법.
#         arr_index = ord(char) - ord("a")
#         alphabet_occurrence_array[arr_index] += 1
    
#     return "a"


# result = find_max_occurred_alphabet(input)
# print(result)