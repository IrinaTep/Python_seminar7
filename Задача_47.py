# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)

# Вывод:
# ok




# # Теория, что такое анонимная функция:
# vals = [412, 12, 354]
# func = lambda x: x**2 if x % 2 == 0 else x**3 # возвести четное число в квдрат, а нечетное - в куб
# for item in vals:
#     print(func(item))

# vals = [412, 12, 354]
# for item in vals:
#     print((lambda x: x**2 if x % 2 == 0 else x**3)(item))

# map - принимает два параментра - функцию и коллекцию элементов; применить к каждому элементу
vals = [412, 12, 354]
# print(list(map(lambda x: x**2 if x % 2 == 0 else x**3, vals))) # можно превратить в кортеж (tuple) или набор (set); новая коллекция не сохранена
new = list(map(lambda x: x**2 if x % 2 == 0 else x**3, vals)) # так новая коллекция сохранена в переменую new
print(new)



transformation = lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(transformation, values))
print(transformed_values)