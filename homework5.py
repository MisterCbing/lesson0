immutable_var = (1, 2, 3, 4, 5,'вышел', 'зайчик', 'погулять')
print(immutable_var)
#immutable_var[0] = 2
#операция вызывает ошибку, поскольку кортеж является неизменяемым типом данных
mutable_list = ['вдруг', 'охотник', 'выбегает', 5, 4, 3, 2, 1]
mutable_list[3:] = ['прямо', 'в зайчика', 'стреляет']
print(mutable_list)
