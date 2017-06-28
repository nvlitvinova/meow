#1. Три класса - фигура, круг, квадрат.
#   Три метода:
#     1. Получить периметр
#     2. Получить площадь
import math


class figure:
    def __init__(self, radius=10):
        self.radius = radius
        self.perimetr = 1
        self.ploschad = 1
        self.pi = 3.14

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_perimetr(self):
        self.perimetr = self.pi * 100
        return self.perimetr

    def get_ploschad(self):
        self.ploschad = self.radius ** 10
        return self.ploschad


class circle(figure):
    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_perimetr(self):
        self.perimetr = 2 * self.pi * self.radius
        return self.perimetr

    def get_ploschad(self):
        self.ploschad = self.pi * self.radius ** 2
        return self.ploschad


class square(figure):
    def __init__(self, storona=10):
        self.storona = storona

    def get_storona(self):
        return self.storona

    def set_storona(self, storona):
        self.storona = storona

    def get_perimetr(self):
        self.perimetr = 4 * self.storona
        return self.perimetr

    def get_ploschad(self):
        self.ploschad = self.storona ** 2
        return self.ploschad


class trapezium(figure):
    def __init__(self):
        self.osnovaniye1 = 5
        self.osnovaniye2 = 11
        self.vysota = 4

    def get_osnovaniye1(self):
        return self.osnovaniye1

    def set_osnovaniye1(self, storona):
        self.osnovaniye1 = osnovaniye1

    def get_osnovaniye2(self):
        return self.osnovaniye2

    def set_osnovaniye2(self, storona):
        self.osnovaniye2 = osnovaniye2

    def get_vysota(self):
        return self.vysota

    def set_vysota(self, vysota):
        self.vysota = vysota

    def get_perimetr(self):
        osnovaniye = (self.osnovaniye2 - self.osnovaniye1) / 2
        self.perimetr = 2 * self.osnovaniye1 + (math.sqrt(self.vysota ** 2 + osnovaniye ** 2)) * 2 + osnovaniye * 2
        # 2 * self.osnovaniye1 + (math.sqrt(self.vysota ** 2 + osnovaniye ** 2)) + osnovaniye
        return self.perimetr

    def get_ploschad(self):
        self.ploschad = (self.osnovaniye1 + self.osnovaniye2) / 2 * self.vysota
        return self.ploschad


f = figure()
f.set_radius(8)
# f.get_radius()
# f.get_perimetr()
f.get_ploschad()