# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

# Ввод:                                     Вывод:
# values = [0, 2, 10, 6]                    same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


def same_by(characteristic, objects):
    # return True if len(set(map(characteristic, objects))) == 1 else False # если результат для всех делений будет одинаковый, то в set будет всего одно число!
# можно даже еще легче:
    # return len(set(map(characteristic, objects))) in [0, 1] # и добавили условие in [0, 1]

# два условия можно поставить в тернарный оператор (условное выражение)
    return True if len(set(map(characteristic, objects))) == 1 else (True if len(set(map(characteristic, objects))) == 0 else False)

values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")

print("same" if same_by(lambda x: x % 2, values) else "different")



# Пример фильтра (как map приниает функцию (необязательно lambda) и набор элементов, но в отличии от map длины входящего и исходящего массивов могут различаться)
lst = [1, 2, 3, 4, 5]

print(list(filter(lambda x: x > 2, lst)))

# Пример enumerate (добавляет индексы), превращает в кортеж
lst = [1, 2, 3, 4, 5]

for x in enumerate(lst):
    print(x)

# Пример zip (можно передать несколько коллекций элементов) - поэлементно соединяет в пары; если количество элементов не совпадает, соединит те, что сможет
lst1 = [412, 1213, 124, 144, 125]
lst2 = [346, 426, 3124, 235]
lst3 = [412, 413]

for x in zip(lst1, lst2, lst3):
    print(x)
