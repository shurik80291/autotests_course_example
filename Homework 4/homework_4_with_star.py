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
    sum_number = 0
    for number in str(num):
        sum_number += int(number)
    found = False
    lst_number = [number for number in str(num)]
    for index, number in enumerate(lst_number):
        for new_number in reversed(range(int(number)+1, 10)):
            sum_number += new_number - int(number)
            if sum_number % 3 == 0:
                lst_number[index] = str(new_number)
                found = True
                break
            else:
                sum_number -= new_number - int(number)
        if found:
            break
    new_num = ""
    for number in lst_number:
        new_num += number
    new_num = int(new_num)
    if new_num == num:
        if new_num % 3 == 0:
            new_num -= 3
        else:
            new_num -= 1
    return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210, 999, 988
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210, 996, 987
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
