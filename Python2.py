class Point:
    def __init__ (self, x = 0, y = 0):
        self.x = x;
        self.y = y;
        #self.z = z;

    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "({0.x}, {0.y})".format(self)
    
    def distance(self, other):
        import math as m
        sqrx = (self.x - other.x) * (self.x - other.x)
        sqry = (self.y - other.y) * (self.y - other.y)
        return m.sqrt(sqrx + sqry)

class Rectangle(Point):
    def __init__(self, line, x1=0, y1=0, x2=0, y2=0):
        self.line = line
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
       
    def __str__(self):
        return  "%d, p1%s, p2%s" %(self.line, str(self.p1), str(self.p2))

    def area(self):
        line2 = self.p1.distance(self.p2)
        print "edge1 = %d\nedge2 = %2.1f" %(self.line, line2)
        print("The area of the rectangle: ")
        return self.line * line2

    
class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        Point.__init__(self, x, y)       

    def __eq__(self, other):
        return self.radius == other.radius and Point.__eq__(other)

    def __str__(self):
        return "r = {0.radius}, center: ({0.x}, {0.y})".format(self)

    def area(self):
        from math import pi
        print("The area of the circle: ")
        return self.radius * self.radius * pi

    def circumference(self):
        from math import pi
        return 2 * pi * self.radius

a = Circle(4,5,6)
print "Circle a: ", str(a)
print a.area()
print
b = Rectangle(3,1,2,3,4)
print "Rectangle b: ", str(b)
print b.area()
print
c = b
print "Rectangle c: ", str(c)
print c.area()