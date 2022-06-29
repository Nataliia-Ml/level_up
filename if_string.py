# a = 3
# if 2==a:
#     print('2=2')
# elif 3==a:
#     print('3=3')
# else:
#     print('не 2, не 3')

# current_temperature = int(input('Введите температуру: '))
# print("current_temperature: ---------", current_temperature, f"Type is: ----- {type(current_temperature)}")
# print("DIR(current_temperature): ----", dir(current_temperature))
# if current_temperature >= 5:
#     print('Не надо одевать шапку')
# else:
#     print('Одень шапку')

# current_temperature = int(input('Введите температуру: '))
# if current_temperature >= 5:
#     print('Не надо одевать шапку')
# if current_temperature<=-23:
#     print('Сиди Дома')
# if current_temperature<=5:
#     print('Одень шапку')


# current_temperature = int(input('Введите температуру: '))
# print("current_temperature: ---------", current_temperature, f"Type is: ----- {type(current_temperature)}")
# if current_temperature >= 5:
#     print('Не надо одевать шапку')
# else:
#     print('Одень шапку')


# tem = 5 if current_temperature >= 5 else None
# print(tem)
# sd = 3
# if sd is not None:
#     print(1)
# else:
#     print(2)

str_1 = ''
str_2 = ""
str_3 = """"""
str_4 = ''''''
# str_5 = 'xngfdu goirdf ugirougdpytugdfi\nogyfdihgifdugyiu sdhyfisd uygfiutywe[' \
#         'ioytwep oytpweiuyt pweuytpiwe\nuytierutye riuyteriou ' \
#         'teriouy eriuyte riotyreiutyty erioutewo uyreoiuteri oyeriougyreio'
# print(str_5)
# str_6 = """;lsdjhg;fhglirtjg;lejfpio
# fdjg;lfjh;lkfgjhgtkhj
# jksdhvlkjfdgh;lkjfghlkjf
# sdhgkljfhglkjhflkjhgl"""
# print(str_6)
# str_7 = '''рывдпxjgdlfjdghpioлорваплор'''
# str_8 = '''рывдпxjgdlfjdghpioлорваплор'''
# b = sorted(str_7)
# print("b: -----", b, ". Type of b is: -----", type(b))
# d = sorted(str_8)
# print("d: -----", d, ". Type of d is: -----", type(d))
# str_8 = ''.join(sorted(b))
# str_7 = ''.join(sorted(d))
# print(str_8 ==str_7)
# if str_8 ==str_7:
#     print(1)

# Формотирование строк
# # age = 36
# # txt = "My name is John, I am " + age
# # print(txt)
# age = 36
# txt = "My name is John, I am " + str(age)
# print(txt)

# # https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html
# age = 36
# txt = "My name is John, and I am {}"
# res = txt.format(age)
# print('res: ', res)
# age = 36
# txt = "My name is John, and I am {} years old"
# res = txt.format(age)
# print('res: ', res)

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
#
myorder = "I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price)
# print(myorder.format(quantity, itemno, price))
#
# myorder = f"I want to pay {price} dollars for {quantity} pieces of item {itemno}."
# print(myorder)
#
# print(f"I want to pay {price} dollars for {quantity} pieces of item {itemno}.")

# https://pythonworld.ru/osnovy/formatirovanie-strok-operator.html
#
myorder = "I want %s pieces of item %s for %s dollars." % (quantity, itemno, price)
# print(myorder)
# print('%d %s, %d %s' % (6, 'bananas', 10, 'lemons'))

quantity = 3
itemno = 567
price = 49.95
myorder = f"I want {quantity} pieces of item {itemno} for {price} dollars."