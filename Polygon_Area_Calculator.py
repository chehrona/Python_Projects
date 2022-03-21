class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, newWidth):
        self.width = newWidth
        return self.width

    def set_height(self, newHeight):
        self.height = newHeight
        return self.height

    def get_area(self):
        recArea = self.width * self.height
        return recArea

    def get_perimeter(self):
        recPerimeter = 2 * self.width + 2 * self.height
        return recPerimeter

    def get_diagonal(self):
        recDiagonal = (self.width ** 2 + self.height ** 2) ** .5
        return recDiagonal

    def __str__(self):
        printOut = "Rectangle(width={}, height={})".format(self.width, self.height)
        return printOut

    def get_picture(self):
        recRows = ""
        for row in range(0, self.height):
            if self.height > 50 or self.width > 50:
                return  "Too big for picture."
            else:
                recRows += self.width*"*" + "\n"
        return recRows

    def get_amount_inside(self, anotherShape):
        divOrNotWidth = int(self.width/anotherShape.width)
        divWithNoRemainderWidth = self.width%anotherShape.width
        divOrNotHeight = int(self.height/anotherShape.height)
        divWithNoRemainderHeight = self.height%anotherShape.height
        widthDifference = self.width - anotherShape.width
        heightDifference = self.height - anotherShape.height
        if divWithNoRemainderWidth > widthDifference or divOrNotHeight > heightDifference:
            return 0
        elif self.width < anotherShape.width and self.height < anotherShape.height:
            return 0
        else:
            return divOrNotHeight * divOrNotWidth



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, newSide):
        self.width = newSide
        self.height = newSide

    def __str__(self):
        printOut = "Square(side={})".format(self.width)
        return printOut

    def set_width(self, newSide):
        super().set_width(newSide)
        super().set_height(newSide)

    def set_height(self, newSide):
        super().set_width(newSide)
        super().set_height(newSide)

rect = Rectangle(5, 8)
rect2 = Rectangle(10, 10)
# print(rect.get_area())

# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(5)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

print(rect2.get_amount_inside(rect))
