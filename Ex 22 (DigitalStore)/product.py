class Product:
    def __init__(self, id_: str, name: str, price: float, brand: str):  
        self.id_ = id_
        self.name = name
        self.price = price
        self.brand = brand 

    def display(self):
        return f"ID: {self.id_}, Name: {self.name}, Price: {self.price}, Brand: {self.brand}"


if __name__ == "__main__":
    p = Product("123", "p1", 22.5, "b")
    p.display() 