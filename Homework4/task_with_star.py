# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974


def max_division_by_3(num):
    num_list = []
    for character in str(num):
        num_list.append(int(character))
    list_result = []
    for index, elem in enumerate(num_list):
        for i_elem in range(0, 10):
            num_list[index] = i_elem
            if sum(num_list) % 3 == 0:
                list_result.append(num_from_list(num_list))
                num_list[index] = elem
            else:
                num_list[index] = elem
    new_num = max(list_result)
    return new_num


def num_from_list(list_of_numbers):
    list_of_numbers.reverse()
    number = 0
    for i_new_num, elem_new_num in enumerate(list_of_numbers):
        number += elem_new_num * 10 ** i_new_num
    list_of_numbers.reverse()
    return number
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
 379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
 879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
