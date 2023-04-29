import math


class Trigonometry:
    @staticmethod
    def cos(degrees):
        radians = Trigonometry.degrees_to_radians(degrees)
        return math.cos(radians)

    @staticmethod
    def sin(degrees):
        radians = Trigonometry.degrees_to_radians(degrees)
        return math.sin(radians)

    @staticmethod
    def tan(degrees):
        radians = Trigonometry.degrees_to_radians(degrees)
        return math.tan(radians)

    @staticmethod
    def asin(value):
        radians = math.asin(value)
        return Trigonometry.radians_to_degrees(radians)

    @staticmethod
    def acos(value):
        radians = math.acos(value)
        return Trigonometry.radians_to_degrees(radians)

    @staticmethod
    def atan(value):
        radians = math.atan(value)
        return Trigonometry.radians_to_degrees(radians)

    @staticmethod
    def degrees_to_radians(degrees):
        return degrees * math.pi / 180

    @staticmethod
    def radians_to_degrees(radians):
        return radians * 180 / math.pi


print("sin(45): ", '\t', Trigonometry.sin(45))
print("cos(0): ", '\t', Trigonometry.cos(0))
print("tan(45): ", '\t', Trigonometry.tan(45))
print("asin(1): ", '\t', Trigonometry.asin(1))
print("acos(1): ", '\t', Trigonometry.acos(1))
print("atan(1): ", '\t', Trigonometry.atan(1))
print("degress_to_radians(180): ", '\t', Trigonometry.degrees_to_radians(180))
