# #
# # print((47-21)%(6-3))
# #
# # print((47-21)//(6-3))
# # x = 4
# # y = 16
# # for i in range(x,y+1,x):
# #     print(x,y, x*2, i)
#
#
#
# s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
# d = 18
# m = 7
#
# ways = []
#
# for i in range(len(s)):
#
#     count = 0
#     if i + m <= len(s):
#         print(s)
#
#         for j in range(i, i + m):
#             print(i, j, s[j], len(s), m)
#             count += s[j]
#
#         print("-----------")
#
#     if count == d:
#         ways.append(count)
#
# print(len(ways))

arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

set_arr = set(arr)


arr_dict = {a : str(arr).count(str(a)) for a in set_arr}

print(arr_dict)

# d = {1:2, 2:2,3:3, 4:3,5:1}

max_value = max(arr_dict.values())

min_key = min([key for key, val in arr_dict.items() if val == max_value])
print(min_key)

