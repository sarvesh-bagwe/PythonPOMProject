# # from itertools import count
# #
# # sports = ('football', 'basketball', 'cricket', 'hockey', 'tennis', 'volleyball')
# # new_value1 = 'baseball'
# # index1 = 2
# #
# # lt = list(sports)
# #
# # lt.clear()
# #
# # lt.insert(index1, new_value1)
# # sports = tuple(lt)
#
# player_scores = {
#     'Arthur': [85, 90, 92],
#     'Bela': [75, 80, 85],
#     'Carol': [90, 92, 95],
#     'Deepak': [87, 89, 91]
# }
#
# scores = []
# for key, value in player_scores.items():
#     avg = sum(value) / len(value)
#     scores.append([key, avg])
#
# max = scores[0]
# if not len(scores) > 1:
#     print(scores)
# else:
#     max = scores[0]
#     # print(max[1])
#     # print(scores[3][1])
#     for i in range(1, len(scores)):
#         # print(max[1])
#         # print(scores[i][1])
#         print(i)
#         if scores[i][1] > max[1]:
#             print(max[1])
#             print(scores[i][1])
#             max.clear()
#             print(max)
#         #     max.clear()
#             max = scores[i]
#
# print(max)

from faker import Faker

fake = Faker()

fake.passport_number()
print(fake.items())


food_items = {
            'fruits': {
                'tropical': {
                    'mango': {
                        'color': 'orange',
                        'taste': 'sweet',
                        'nutrients': ['vitamin C', 'vitamin A', 'fiber']
                    },
                    'pineapple': {
                        'color': 'yellow',
                        'taste': 'tangy',
                        'nutrients': ['vitamin C', 'manganese', 'fiber']
                    }
                },
                'temperate': {
                    'apple': {
                        'color': 'red',
                        'taste': 'sweet',
                        'nutrients': ['vitamin C', 'fiber', 'potassium']
                    },
                    'pear': {
                        'color': 'green',
                        'taste': 'juicy',
                        'nutrients': ['vitamin C', 'fiber', 'copper']
                    }
                }
            },
            'vegetables': {
                'leafy': {
                    'spinach': {
                        'color': 'green',
                        'taste': 'earthy',
                        'nutrients': ['vitamin K', 'vitamin A', 'iron']
                    },
                    'kale': {
                        'color': 'green',
                        'taste': 'bitter',
                        'nutrients': ['vitamin K', 'vitamin A', 'calcium']
                    }
                },
                'root': {
                    'carrot': {
                        'color': 'orange',
                        'taste': 'sweet',
                        'nutrients': ['vitamin A', 'vitamin K', 'fiber']
                    },
                    'beet': {
                        'color': 'red',
                        'taste': 'earthy',
                        'nutrients': ['vitamin C', 'folate', 'iron']
                    }
                }
            }
        }


def traverse(d, col):

    if isinstance(d, dict):
        for key, value in d.items():
            # print(key)
            if isinstance(value, dict):
                if "color" in value and value["color"] == col and "taste" in value:
                    print(f"{key} is {value["taste"]}")
                else:
                    traverse(value, col)


traverse(food_items, 'red')

