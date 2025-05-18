#1. Create Class Line

class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        

class Line:
    def __init__(self, start:Point, end:Point):
            self.start = start
            self.end = end
            self.dx = self.end.x - self.start.x
            self.dy = self.end.y - self.start.y
            self.length = self.compute_length()
            self.slope = self.compute_slope()
    
    def compute_length(self):
        return (self.dx**2 + self.dy**2)**0.5 
       
    
    def compute_slope(self):
        if self.dx == 0:
            return float("inf")
        return self.dy / self.dx
    
    def compute_horizontal_cross(self) -> bool:
        return (self.start.y <= 0 <= self.end.y) or (self.end.y <= 0 <= self.start.y)

    def compute_vertical_cross(self) -> bool:
        return (self.start.x <= 0 <= self.end.x) or (self.end.x <= 0 <= self.start.x)

          
line1 = Line(start=Point(2, 3), end=Point(7, 7))

print("Length: ", line1.compute_length())
print("Slope: ", line1.compute_slope())
print("Horizontal cross: ", line1.compute_horizontal_cross())
print("Vertical cross: ", line1.compute_vertical_cross())

#2. Redefine rectangle

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
        
class Rectangle:
    def __init__(self, left:Line, right:Line, top:Line, bottom:Line):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
      
      
    def compute_area(self):
      return self.left.length * self.top.length
    
    def compute_perimeter(self):
        return 2 * (self.left.length + self.top.length)
    
