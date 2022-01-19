# Цикл while
# i = 30
# ii = 0
# while ii < i:
#     print(ii)
#     ii += 1

# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# list_f = []
# for leter in txt:
#     if leter == 'f':
#         list_f.append(leter)
# print('list_f: ', list_f)

# res = ''
# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isalpha():
#         res += leter
# print('res: ', res)

# Oператор break досрочно прерывает цикл.
txt = '546f2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
for leter in txt:
    if leter.isalpha():
        break
    print(leter * 2)


