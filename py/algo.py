# input = [0, 3, 5, 6, 1, 2, 4]


# def find_max_plus_or_multiply(array):
#     # 이 부분을 채워보세요!
#     sum = 0
#     for x in array:
#         if sum == 0 or sum ==1:
#             sum = sum+x
#         elif x == 0 or x ==1 :
#             sum = sum + x
#         else:
#             sum = sum * x
        
#     return sum


# result = find_max_plus_or_multiply(input)
# print(result)

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    sum = 0
    for x in array:
        if x<=1 or sum<=1:
            sum += x
        else:
            sum *= x
    return sum


result = find_max_plus_or_multiply(input)
print(result)