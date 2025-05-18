import random

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def total_price(self, quantity: int) -> float:
        return self.price * quantity


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size_ml: int):
        super().__init__(name, price)
        self.size_ml = size_ml

    def total_price(self, quantity: int) -> float:
        tax = 0.1  # 10% impuesto
        return super().total_price(quantity) * (1 + tax)


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, is_fried: bool):
        super().__init__(name, price)
        self.is_fried = is_fried


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, origin: str):
        super().__init__(name, price)
        self.origin = origin


class Order:
    def __init__(self):
        self.order_number = random.randint(1000, 9999)
        self.items = []  # Lista de tuplas (item, cantidad)

    def add(self, item: MenuItem, quantity: int):
        self.items.append((item, quantity))

    def total(self) -> float:
        return sum(item.total_price(qty) for item, qty in self.items)

    def apply_discount(self) -> float:
        subtotal = self.total()
        discount = 0.0
        if subtotal > 80000:
            discount = 0.15
        elif subtotal > 50000:
            discount = 0.10
        elif subtotal > 30000:
            discount = 0.05
        return subtotal * (1 - discount)

    def summary(self):
        print(f"\n Pedido #{self.order_number}")
        print("Resumen del pedido:")
        for item, qty in self.items:
            print(f" - {item.name} x{qty} = ${item.total_price(qty):,.2f}")
        print(f"\nSubtotal: ${self.total():,.2f}")
        print(f"Total con descuento: ${self.apply_discount():,.2f}")


# ---------- Elementos del Menú ----------

# Bebidas
coca_cola = Beverage("CocaCola", 5000, 350)
lemonade = Beverage("Limonada", 4000, 300)
beer = Beverage("Cerveza", 7000, 330)
water = Beverage("Agua", 2000, 500)

# Aperitivos
arepa_rellena = Appetizer("Arepa Rellena", 6000, True)
empanada = Appetizer("Empanada", 2500, True)
patacon = Appetizer("Patacón", 3000, True)
nachos = Appetizer("Nachos", 5500, False)

# Platos Fuertes
spaguetti = MainCourse("Spaguetti", 18000, "Italiana")
beef = MainCourse("Carne Asada", 25000, "Colombiana")
pork_loin = MainCourse("Lomo de Cerdo", 23000, "Internacional")
hamburger = MainCourse("Hamburguesa", 20000, "Americana")
bandeja_paisa = MainCourse("Bandeja Paisa", 30000, "Colombiana")

#Pedido
if __name__ == "__main__":
    order = Order()
    order.add(coca_cola, 2)
    order.add(nachos, 1)
    order.add(spaguetti, 1)
    order.add(bandeja_paisa, 1)
    order.add(empanada, 3)
    order.summary()
