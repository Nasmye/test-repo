class Rectangle:
    """docstring for Rectangle."""

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def perimeter(self):
        return self.length*2 + self.width*2

    def area(self):
            return self.length*self.width

    def display(self):
        print(f"Rectangle \nLength: {self.length}\nWidth: {self.width}")
        print(f"Perimeter: {self.perimeter()}\nArea: {self.area()}\n\n")

class Parallelpipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

    def display_paral(self):
        print(f"Parallelpipede \nLength: {self.length}\nWidth: {self.width}\nHeight: {self.height}")
        print(f"Volume {self.volume()}")


rect1= Rectangle(2,3)
rect1.display()

paral = Parallelpipede(8,4,5)
paral.display_paral()