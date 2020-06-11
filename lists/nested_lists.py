# nested_list = [[1,2,3], [4,5,6], [7,8,9]]
#print(len(nested_list))
# would return 3
# print(nested_list[0][1])
# would return 2
# print(nested_list[-1][-2])
# would return 8
# for l in nested_list:
#     for val in l:
#         print(val)
# would return:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.576]]
# one way to do it:
# for loc in coords:
#     for val in loc:
#         print(val)
# or this way:
# [[print(val) for val in loc] for loc in coords]

# print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])
# prints: [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]

# print([["*" for num in range(1,4)] for val in range(1,4)])

# ****Exercises****

# answer = [[val for val in range(0,3)] for y in range(1,4)]
# print(answer)
# would return: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]