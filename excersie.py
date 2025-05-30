class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
        self.points = []
    
    def compute_length(self):
        return ((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**0.5
    
    def compute_slope(self):
        dx = self.end.x - self.start.x
        if dx == 0:
            return float('inf')  # o puedes retornar None si prefieres evitar "infinito"
        return (self.end.y - self.start.y) / dx
    
    def compute_horizontal_cross(self):
        return self.start.y * self.end.y < 0
    
    def compute_vertical_cross(self):
        return self.start.x * self.end.x < 0
    
    def discretize_line(self, n: int):
        self.points = [
            Point(
                self.start.x + i * (self.end.x - self.start.x) / (n - 1),
                self.start.y + i * (self.end.y - self.start.y) / (n - 1)
            ) for i in range(n)
        ]


class Rectangle:
    def __init__(self, method: int, width: float = None, height: float = None,
                 center: Point = None, bottom_left: Point = None, upper_right: Point = None, lines: list = None):

        if method == 1:
            if width is None or height is None or bottom_left is None:
                raise ValueError("Método 1 requiere ancho, alto y esquina inferior izquierda.")
            self.width = width
            self.height = height
            self.bottom_left = bottom_left
            self.upper_right = Point(bottom_left.x + width, bottom_left.y + height)
            self.center = Point(bottom_left.x + width / 2, bottom_left.y + height / 2)

        elif method == 2:
            if width is None or height is None or center is None:
                raise ValueError("Método 2 requiere ancho, alto y centro.")
            self.width = width
            self.height = height
            self.center = center
            self.bottom_left = Point(center.x - width / 2, center.y - height / 2)
            self.upper_right = Point(center.x + width / 2, center.y + height / 2)

        elif method == 3:
            if bottom_left is None or upper_right is None:
                raise ValueError("Método 3 requiere esquina inferior izquierda y superior derecha.")
            self.bottom_left = bottom_left
            self.upper_right = upper_right
            self.width = abs(upper_right.x - bottom_left.x)
            self.height = abs(upper_right.y - bottom_left.y)
            self.center = Point((bottom_left.x + upper_right.x) / 2, (bottom_left.y + upper_right.y) / 2)
        
        elif method == 4:
            if lines is None or len(lines) != 4:
                raise ValueError("Metodo 4 requiere una lista de 4 lineas")
            self.lines = lines
            self.bottom_left = lines[0].start
            self.upper_right = lines[2].end
            self.width = lines[0].length
            self.height = lines[1].length
            self.center = Point(
                (self.bottom_left.x + self.upper_right.x) / 2,
                (self.bottom_left.y + self.upper_right.y) / 2
            )

        else:
            raise ValueError("Método de inicialización inválido.")

    def compute_area(self):
        print(f"Área: {self.width * self.height}")

    def compute_perimeter(self):
        print(f"Perímetro: {2 * (self.width + self.height)}")

    def compute_interference_point(self, point: Point):
        x_in = (self.bottom_left.x <= point.x <= self.upper_right.x)
        y_in = (self.bottom_left.y <= point.y <= self.upper_right.y)
        print(f"¿El punto está dentro?: {x_in and y_in}")
        
    def _built_lines_from_points(self):
        bl = self.bottom_left
        ur = self. upper_right
        br = Point(ur.x, bl.y)
        ul = Point(bl.x, ur.y)
        
        self.lines = [
            Line(bl, br),
            Line(br, ur),
            Line(ur, ul),
            Line(ul, bl)
        ]
        


class Square(Rectangle):
    def __init__(self, method: int, side: float = None,
                 center: Point = None, bottom_left: Point = None, upper_right: Point = None):
        if method == 1:
            if side is None or bottom_left is None:
                raise ValueError("Método 1 requiere lado y esquina inferior izquierda.")
            super().__init__(method=1, width=side, height=side, bottom_left=bottom_left)
        elif method == 2:
            if side is None or center is None:
                raise ValueError("Método 2 requiere lado y centro.")
            super().__init__(method=2, width=side, height=side, center=center)
        elif method == 3:
            if bottom_left is None or upper_right is None:
                raise ValueError("Método 3 requiere dos esquinas.")
            width = abs(upper_right.x - bottom_left.x)
            height = abs(upper_right.y - bottom_left.y)
            if width != height:
                raise ValueError("Los puntos no forman un cuadrado.")
            super().__init__(method=3, bottom_left=bottom_left, upper_right=upper_right)
        else:
            raise ValueError("Método inválido para crear un cuadrado.")
        


# --- Interfaz de usuario ---
def solicitar_float(mensaje):
    return float(input(mensaje))


print("Elige el método para crear el rectángulo:")
print("1. Con ancho, alto y esquina inferior izquierda")
print("2. Con ancho, alto y centro")
print("3. Con esquina inferior izquierda y esquina superior derecha")
print("4. Con 4 lineas")
metodo = int(input("Ingresa el número del método (1, 2, 3 o 4): "))

if metodo == 1:
    w = solicitar_float("Ancho: ")
    h = solicitar_float("Alto: ")
    x = solicitar_float("X de la esquina inferior izquierda: ")
    y = solicitar_float("Y de la esquina inferior izquierda: ")
    rect = Rectangle(method=1, width=w, height=h, bottom_left=Point(x, y))
elif metodo == 2:
    w = solicitar_float("Ancho: ")
    h = solicitar_float("Alto: ")
    x = solicitar_float("X del centro: ")
    y = solicitar_float("Y del centro: ")
    rect = Rectangle(method=2, width=w, height=h, center=Point(x, y))
elif metodo == 3:
    x1 = solicitar_float("X de la esquina inferior izquierda: ")
    y1 = solicitar_float("Y de la esquina inferior izquierda: ")
    x2 = solicitar_float("X de la esquina superior derecha: ")
    y2 = solicitar_float("Y de la esquina superior derecha: ")
    rect = Rectangle(method=3, bottom_left=Point(x1, y1), upper_right=Point(x2, y2))
elif metodo == 4:
    print("Ingresa los 4 lados como pares de puntos")
    def leer_punto(n):
        x = solicitar_float(f"Punto {n} - x:")
        y = solicitar_float(f"Punto {n} - y ")
        return Point(x, y)
    
    p1 = leer_punto(1)
    p2 = leer_punto(2)
    p3 = leer_punto(3)
    p4 = leer_punto(4)
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    line4 = Line(p4, p1)
    lines = [line1, line2, line3, line4]
    
    rect = Rectangle(method=4, lines=lines)
    
else:
    raise ValueError("Método inválido")



rect.compute_area()
rect.compute_perimeter()