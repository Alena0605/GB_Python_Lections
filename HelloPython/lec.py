# ФАЙЛЫ

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close

with open('file.txt', 'w') as data:
    data.write('LINE 1\n')
    data.write('LINE 2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


# ФУНКЦИИ И МОДУЛИ

import function_file as ff

print(ff.f(1))

print(ff.new_string('!', 5))

print(ff.concatenatio('a', 's', 'd', 'w'))  # asdw
print(ff.concatenatio('a', '1'))  # a1
# print(concatenatio(1, 2, 3, 4))  # TypeError: ...


# РЕКУРСИЯ

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


list = []
for e in range(1, 10):
    list.append(fib(e))

print(list)  # 1 1 2 3 5 8 13 21 34


# КОРТЕЖИ

a = (3, 4, 5)
print(a)
print(a[-1])

for item in a:
    print(item)


# СЛОВАРИ

dictionary = {}

dictionary = \
    {
        'up': 'w',
        'left': 'a',
        'right': 'd',
        'down': 's'
    }

print(dictionary)
print(dictionary['left'])
# типы ключей могут отличаться

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(k)

for d in dictionary:
    print(d)

dictionary['up'] = 'up'
print(dictionary)


# МНОЖЕСТВА

colors = {'red', 'green', 'blue'}
print(colors)

colors.add('gray')
print(colors)

colors.remove('red')
print(colors)

colors.discard('red')  # при попытке удаления отсутствующего элемента ошибки не будет
print(colors)

colors.clear()
print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()

u = a.union(b)           # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)    # i = {8, 2, 5}
dl = a.difference(b)     # dl = {1, 3}
dr = b.difference(a)     # dr = {13, 21}

s = frozenset(a)


# СПИСКИ

list1 = [1, 2, 3, 4, 5]
list2 = list1

list1[0] = 10
list2[1] = 20

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print(len(list1))
print(list1.pop())
print(list1)

print(list1.pop(2))
print(list1)

list1.insert(2, 11)
print(list1)
