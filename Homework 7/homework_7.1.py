# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абсцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

class Segment:
    def __init__(self, first_dot, second_dot):
        """
        Атрибуты класса Segment
        :param first_dot: кортеж с координатами первой точки (x1, y1)
        :param second_dot: кортеж с координатами второй точки (x2, y2)
        """
        self.first_dot = first_dot
        self.second_dot = second_dot

    def length(self):
        """
        Находим длину отрезка
        :return: длина отрезка с округлением до 2 знаков после запятой
        """
        line = round(((self.first_dot[0] - self.second_dot[0])**2 +
                      (self.first_dot[1] - self.second_dot[1])**2)**0.5, 2)
        return line

    def x_axis_intersection(self):
        """
        Проверка, пересекает ли отрезок ось абсцисс
        :return: True - пересекает, False - не пересекает
        """
        if self.first_dot[1] * self.second_dot[1] <= 0:
            return True
        else:
            return False

    def y_axis_intersection(self):
        """
        Проверка, пересекает ли отрезок ось ординат
        :return: True - пересекает, False - не пересекает
        """
        if self.first_dot[0] * self.second_dot[0] <= 0:
            return True
        else:
            return False


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
