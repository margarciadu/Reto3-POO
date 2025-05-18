# Reto3-POO

 ```mermaid
classDiagram

class MenuItem {
  - name: str
  - price: float
  + total_price(quantity: int): float
}

class Beverage {
  - size_ml: int
  + total_price(quantity: int): float
}

class Appetizer {
  - is_fried: bool
}

class MainCourse {
  - origin: str
}

class Order {
  - order_number: int
  - items: List~Tuple[MenuItem, int]~
  + add(item: MenuItem, quantity: int)
  + total(): float
  + apply_discount(): float
  + summary()
}

MenuItem <|-- Beverage
MenuItem <|-- Appetizer
MenuItem <|-- MainCourse

Order --* MenuItem : has
