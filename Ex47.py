import math

class Geometry():
    """docstring for Geometry."""

    def __init__(self, x ,y):
            self.x = x
            self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, m ):
        return math.sqrt(math.pow(self.x -m.get_x(), 2)+math.pow(self.y - m.get_y(),2))

    def middle(self, m):
        midx =m.get_x()-self.x
        midy =m.get_y()-self.y
        midm =Geometry(midx, midy)
        return midm

    def trianglePerimeter(self, m1, m2):
        result =self.distance(m1) + m1.distance(m2) + self.distance(m2)
        return result

    def triangleIsoscl(self ,m1 ,m2):
        if self.distance(m1)==self.distance(m2) or self.distance(m1)==m1.distance(m2) or self.distance(m2)==m1.distance(m2):
            return True
        else:
            return False


m1 = Geometry(2,5)
m2 = Geometry(-4,5)
print(f"first point :\nx= {m1.get_x()}  y= {m1.get_y()}")
print(f"Second point :\nx= {m2.get_x()}  y= {m2.get_y()}")

print(f"Distance between point 1 and 2 is : {m1.distance(m2)}")

middle =m1.middle(m2)
print(f"The middle point between the 1st point and secord is :\nx= {middle.get_x()}\ny= {middle.get_y()}\n")

m3 = Geometry(0,2)
triangle_primeter = m1.trianglePerimeter(m2,m3)
print(f"The triangle Perimeter is : {triangle_primeter}")

if m1.triangleIsoscl(m2, m3)==True:
    print("The triangle is isoscl")
else :
    print("The triangle is not isoscl")