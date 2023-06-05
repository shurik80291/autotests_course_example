# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open("test_file/task_3.txt", 'r', encoding='utf-8') as file:
    purchase = 0
    purchase_list = []
    for price in file.readlines():
        if price != '\n':
            purchase += int(price)
        else:
            purchase_list.append(purchase)
            purchase = 0
    purchase_list.sort(reverse=True)
    three_most_expensive_purchases = sum(purchase_list[:3])

assert three_most_expensive_purchases == 202346
