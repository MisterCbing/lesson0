a = 'Hello, world!'
print('Первое задание: длина строки равна', end = ' ')
print(len(a))

first, second = 10, 18
summa = first + second
diff = first - second
print('Второе задание:', end = ' ')
print('Сумма равна:', str(summa) + ',', 'Разность равна:', diff)

third = 28
mean = (first + second + third) / 3
print('Третье задание: mean = ', mean)

first_string, second_string = "Вторник", "Понедельник"
print('Четвёртое задание:')
print(second_string + ',', first_string)

a, b, c = 6, 7, 8
f = ((a * b) + (a * c)) ** 3 / 2
print('Пятое задание: f = ', f)