# ТИПЫ ДАННЫХ И ПЕРЕМЕННЫЕ
# int, float, boolean, str, list, None

value = None
print(type(value))

a = 123
b = 1.23

print(type(a))
print(type(b))

value = 12345
print(type(value))

s = 'hello \'world'   # обратный слэш перед символом для его вывода на экран

print(s)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s)) 
# можно поменять порядок вывода, указав индексы: 
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print(f)

lis = ['1', '2', '3']
col = ['hello', 1, 2, 4.5, True]

print(lis)
print(col)


# ВВОД И ВЫВОД ДАННЫХ
# print, input

print('Введите a: ')
a = int(input())
print('Введите b: ')
b = int(input())

print(a, ' + ', b, ' = ', a + b)
print('{} {}'.format(a, b))
print(f'{a} {b}')


# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
# +, -, *, /, %, //, **
# (), Сокращенные операции

a = 1.3123
b = 3
c = round(a * b, 5)
print(c)

a = 3
a += 5

print(a)


# ЛОГИЧЕСКИЕ ОПЕРАЦИИ
# >, >=, <, <=, ==, !=
# not, and, or
# is, is not, in, not in

f = [1, 2, 3, 4]
print(f)
print(not 2 in f)

is_odd = f[0] % 2 == 0   # ИЛИ is_odd = not f[0] % 2
print(is_odd)


# УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ
# if, if-else

a = int(input("a = "))
b = int(input("b = "))

if a > b:
    print(a)
else:
    print(b)


username = input('Введите имя: ')

if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)


# УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ
# while, while-else

original = 23
inverted = 0

while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(original)
else:
    print('Пожалуй')
    print('хватит )')

print(inverted)


# УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ
# for

for i in range(1, 10, 2):
    print(i)

for i in 'qwerty':
    print(i)


# СТРОКИ

text = 'съешь ещё этих мягких французских булок'

print(len(text))                  # 39
print('ещё' in text)              # True
print(text.isdigit())             # False
print(text.islower())             # True
print(text.replace('ещё', 'ЕЩЁ'))

for c in text:
    print(c)

print(text[0])                      # c
print(text[1])                      # ъ
# print(text[len(text)])             # IndexError
print(text[len(text)-1])            # к
print(text[-5])                     # б
print(text[:])                      # print(text)
print(text[:2])                     # съ
print(text[len(text)-2:])           # ок
print(text[2:9])                    # ешь ещё
print(text[6:-18])                  # ещё этих мягких
print(text[0:len(text):6])          # сеикакл
print(text[::6])                    # сеикакл

text = text[2:9] + text[-5] + text[:2]   # ешь ещёбсъ


# СПИСКИ: ВВЕДЕНИЕ

numbers = [1, 2, 3, 4, 5]
print(numbers) 

ran = range(1, 6)
print(type(ran))

numbers = list(ran)
print(type(numbers)) 

numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers) 

for i in numbers:
    i *= 2
    print(i) 

print(numbers) 


colors = ['red', 'green', 'blue']

for e in colors:
    print(e)
for e in colors:
    print(e * 2)   # redred greengreen blueblue

colors.append('gray') 
print(colors == ['red', 'green', 'blue', 'gray']) 

colors.remove('red')   # del colors[0]
print(colors)


# ФУНКЦИИ

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))
