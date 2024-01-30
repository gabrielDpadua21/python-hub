import math

PI = 3.14159

class CircleArea:

    def solution(self, raio):
        return "A=" + "%.4f" % (PI * math.pow(raio, 2))