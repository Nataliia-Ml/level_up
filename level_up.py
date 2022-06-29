# fruits = ['apple', 'banana', 'cherry']
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
# print(id(fruits))
# print(id(fruits[0]))
# print(id(fruits[1]))
# print(id(fruits[2]))
# fruits.append('banana')
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
# print(id(fruits))
# print(id(fruits[0]))
# print(id(fruits[1]))
# print(id(fruits[2]))
# print(id(fruits[3]))
# fruits.pop(2)
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
# print(id(fruits))
# print(id(fruits[0]))
# print(id(fruits[1]))
# print(id(fruits[2]))
# print(fruits.index('banana'))
# dfg = [1, 2.3, 'apple', [1, 2, 3], None, True, {1:2, 3:4}]
# print("dfg: -----", dfg, ". Type of dfg is: -----", type(dfg))
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)

# fruits = ['apple', 'banana', 'cherry', 'cherry', 'pineapple']
# print("fruits[0]: -----", fruits[0], ". Type of fruits[0] is: -----", type(fruits[0]))
# print("fruits[0:3]: -----", fruits[0:3], ". Type of fruits[0:3] is: -----", type(fruits[0:3]))
# print("fruits[0:3:2]: -----", fruits[0:3:2], ". Type of fruits[0:3:2] is: -----", type(fruits[0:3:2]))
# print("fruits[:3]: -----", fruits[:3], ". Type of fruits[:3] is: -----", type(fruits[:3]))
# print("fruits[3:]: -----", fruits[3:], ". Type of fruits[3:] is: -----", type(fruits[3:]))

# fruits = ['apple', 'banana', 'cherry', 'cherry', 'pineapple']
# print("fruits[-1]: -----", fruits[-1], ". Type of fruits[-1] is: -----", type(fruits[-1]))
# print("fruits[-4:-2]: -----", fruits[-4:-2], ". Type of fruits[-4:-2] is: -----", type(fruits[-4:-2]))
# print("fruits[-4:-1:2]: -----", fruits[-4:-1:2], ". Type of fruits[-4:-1:2] is: -----", type(fruits[-4:-1:2]))
# print("fruits[-4:]: -----", fruits[-4:], ". Type of fruits[-4:] is: -----", type(fruits[-4:]))
# print("fruits[:-2]: -----", fruits[:-2], ". Type of fruits[:-2] is: -----", type(fruits[:-2]))

# in - оператор вхождения
# fruits = ['apple', 'banana', 'cherry', 'cherry', 'pineapple']
# fruits_2 = ['apple', 'banana']
# if fruits_2 in fruits:
#     print('apple is exist')
# else:
#     print('apple not exist')

# fruits = ['apple', 'banana', 'cherry', 'cherry', 'pineapple']
# dubl = []
# difs = []
# for fruit in fruits:
#     if fruit not in dubl:
#         dubl.append(fruit)
#     else:
#         difs.append(fruit)
# for dif in set(difs):
#     print(fruits.count(dif))

# Alexander Omelchenko, [12.01.22 19:03]
# numbers = [1, 2, 3, -1, -1, 4, 55, 4, 5, 6]
# duplicates = []
# for i in numbers:
#     if numbers.count(i) > 1:
#         if i not in duplicates:
#             duplicates.append(i)
#
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# fr = fruits
# print("fr: -----", fr, ". Type of fr is: -----", type(fr))
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
# print("fr: -----", id(fr))
# print("fruits: -----", id(fruits))
# print("fr[1]: -----", id(fr[1]))
# print("fruits[1]: -----", id(fruits[1]))


# fruits = ['apple', 'banana', 'melon', 'pineapple']
# fr = fruits[:]
# print("fr: -----", fr, ". Type of fr is: -----", type(fr))
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
# print("fr: -----", id(fr))
# print("fruits: -----", id(fruits))
# print("fr[1]: -----", id(fr[1]))
# print("fruits[1]: -----", id(fruits[1]))
# fruits.append('cherry')
# print("fr: -----", fr, ". Type of fr is: -----", type(fr))
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))

#
# fruits = ['apple', 'banana', 'melon', 'pineapple']
# fr = fruits.copy()
# print("fr: -----", fr, ". Type of fr is: -----", type(fr))
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
# print("fr: -----", id(fr))
# print("fruits: -----", id(fruits))
# print("fr[1]: -----", id(fr[1]))
# print("fruits[1]: -----", id(fruits[1]))
# fruits.append('cherry')
# print("fr: -----", fr, ". Type of fr is: -----", type(fr))
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))


# from copy import copy, deepcopy
# fruits = ['apple', 'banana', 'melon', 'pineapple', {1,2,3}, {1:2, 2:3, 3:4}, [1,2,3,4]]
# fr = copy(fruits)
# print("fr: -----", fr, ". Type of fr is: -----", type(fr))
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
# print("fr: -----", id(fr))
# print("fruits: -----", id(fruits))
# print("fr[5]: -----", id(fr[5]))
# print("fruits[5]: -----", id(fruits[5]))
# print("fr[6]: -----", id(fr[6]))
# print("fruits[6]: -----", id(fruits[6]))
# print("fr[6][1]: -----", id(fr[6][1]))
# print("fruits[6][1]: -----", id(fruits[6][1]))
# fruits.append('cherry')
# print("fr: -----", fr, ". Type of fr is: -----", type(fr))
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
#
# fruits = ['apple', 'banana', 'melon', 'pineapple', {1,2,3}, {1:2, 2:3, 3:4}, [1,2,3,4]]
# fr = deepcopy(fruits)
# print("fr: -----", fr, ". Type of fr is: -----", type(fr))
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
# print("fr: -----", id(fr))
# print("fruits: -----", id(fruits))
# print("fr[5]: -----", id(fr[5]))
# print("fruits[5]: -----", id(fruits[5]))
# print("fr[6]: -----", id(fr[6]))
# print("fruits[6]: -----", id(fruits[6]))
# print("fr[6][1]: -----", id(fr[6][1]))
# print("fruits[6][1]: -----", id(fruits[6][1]))
# fruits.append('cherry')
# print("fr: -----", fr, ". Type of fr is: -----", type(fr))
# print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
#
# res = [i for i in range(1, 100) if i%2 == 0]
# print(res)

bad_lists = [{'name': 'Calibri', 'len': 360}, {'name': 'Audience', 'len': 360}]
filter_list = ['Calibri', 'Bark', 'There', 'These']
result_list = [i for i in bad_lists if i['name'] in filter_list]
print("result_list: -----", result_list, ". Type of result_list is: -----", type(result_list))