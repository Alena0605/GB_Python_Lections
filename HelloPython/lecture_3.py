def f(x):
    return x ** 2


g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))


# Функция lambda

def sum(x, y):
    return x + y


s = lambda x, y: x + y


def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)


# calc(sum, 5, 8)


# List Comprehension

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

ls_1 = []

for i in range(1, 101):
    if i % 2 == 0:
        ls_1.append(i)

# print(ls_1)

ls_2 = [i for i in range(1, 21)]
# print(ls_2)

ls_3 = [i for i in range(1, 21) if i % 2 == 0]
# print(ls_3)


def f_3(x):
    return x ** 3


ls_4 = [f_3(i) for i in range(1, 21) if i % 2 == 0]
# print(ls_4)


# ЗАДАЧА:
# Даны числа, нужно выбрать четные и составить список пар (число; квадрат числа).

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)

# print(res)


# Функция map

li = [x for x in range(1, 20)]

li = list(map(lambda x: x + 10, li))

# print(li)


# data = list(map(int, input().split()))
# print(data)


# ЗАДАЧА:
# Даны числа, нужно выбрать четные и составить список пар (число; квадрат числа).

def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x ** 2), res))

# print(res)


# Функция filter

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))
# print(res)


# ЗАДАЧА:
# Даны числа, нужно выбрать четные и составить список пар (число; квадрат числа).

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x ** 2), res))

# print(res)


# Функция zip

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)


# Функция enumerate

data = list(enumerate(users))
print(data)
