
class Shape:
    def __init__(self, side):
        self._side = side

    def getArea(self):
        return -1

    def getCircumference(self):
        return -1

    def printInfo(self):
        area = self.getArea()
        circ = self.getCircumference()
        print("The area is %f and the circumference is %f" % (area, circ))


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self._width = width

    def getArea(self):
        return self._side * self._width

    def getCircumference(self):
        return 2 * (self._side + self._width)


class Square(Shape):
    def __init__(self, side):
        super().__init__(side)

    def getArea(self):
        return self._side * self._side

    def getCircumference(self):
        return 4 * self._side


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def getArea(self):
        return 3.14 * self._side * self._side

    def getCircumference(self):
        return 3.13 * 2 * self._side


def test():
    s1 = Shape(10)
    s1.printInfo()

    r1 = Rectangle(10, 2)
    r2 = Rectangle(3, 5)
    s1 = Square(4)
    s2 = Square(2)
    c1 = Circle(5)

    #totalArea = r1.getArea() + r2.getArea() + s1.getArea() + s2.getArea() + c1.getArea()
    #totalCircumference = r1.getCircumference() + r2.getCircumference() + s1.getCircumference() + s1.getCircumference() + c1.getCircumference()
    #print("totalArea %f" % (totalArea))
    #print("totalCircumference %f" % (totalCircumference))

    shapeList = []
    shapeList.append(r1)
    shapeList.append(r2)
    shapeList.append(s1)
    shapeList.append(s2)
    shapeList.append(c1)

    totalArea = 0
    totalCircumference = 0

    for shape in shapeList:
        totalArea = totalArea + shape.getArea()
        totalCircumference = totalCircumference + shape.getCircumference()

    print("totalArea %f" % (totalArea))
    print("totalCircumference %f" % (totalCircumference))


def main():
    test()


main()
