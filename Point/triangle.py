import math

class ClassError(Exception):
    pass

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice_list = [vertice1, vertice2, vertice3]
        for v in self.__vertice_list:
             if not isinstance(v, Point):
                raise ClassError ("The parameter is not a Point")
   
    def perimeter(self):
        distance_list = []
        for i in range(len(self.__vertice_list)):
            v1 = self.__vertice_list[i]
            v2 = self.__vertice_list[(i + 1) % len(self.__vertice_list)]
            distance_list.append(v1.distance_from_point(v2))
        return sum(distance_list)


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())