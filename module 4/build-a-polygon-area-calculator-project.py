class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        area = self.width*self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            draw = '*'
            picture = f''
            line = 1
            while line <= self.height:
                picture += f'{draw*self.width}\n'
                line += 1
            return picture
    
    def get_amount_inside(self,other):
        return int(self.get_area() / other.get_area())
    
    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def get_area(self):
        return super().get_area()
    
    def get_diagonal(self):
        return super().get_diagonal()
    
    def set_side(self, side):
        self.width = side 
        self.height = side
    
    def set_width(self, side):
        self.set_side(side)
    
    def set_height(self, side):
        self.set_side(side)
     
    def __str__(self):
        side = self.width
        side = self.height
        return f'{self.__class__.__name__}(side={side})'
       


#TESTS
rect = Rectangle(5,7)
rect.set_height(7)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
print(rect.get_area())

sq = Square(9)
sq.set_side(4)
sq.set_height(5)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
print(sq.get_area())

print(Rectangle(4,8).get_amount_inside(Rectangle(3,6)))
