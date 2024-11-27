import math


def area(r):
    """
    Возвращает площадь окружности по заданному численному радиусу.

    :param r: радиус окружности (int | float)
    :return: площадь окружности
    :rtype: float
    """
    return math.pi * r * r


def perimeter(r):
    """
    Возвращает периметр окружности по заданному численному радиусу.

    :param r: радиус окружности (int | float)
    :return: периметр окружности
    :rtype: float
    """
    return 2 * math.pi * r
