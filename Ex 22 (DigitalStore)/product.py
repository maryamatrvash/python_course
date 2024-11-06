class Product:
    unique_id = [] 
    def __init__(self, id_: str, name: str, price: float, brand: str): 
        id_ = Product.is_unique_id(id_) 
        self.id_ = id_
        self.name = name
        self.price = price
        self.brand = brand 

    @classmethod
    def is_unique_id(cls, id_):
        if id_ not in cls.unique_id:
            cls.unique_id.append(id_)
            return id_
        else:
            print(f"ID: {id_} is available") 

    def display(self):
        return f"ID: {self.id_}, Name: {self.name}, Price: {self.price}, Brand: {self.brand}"


if __name__ == "__main__":
    p = Product("123", "p1", 22.5, "b")
    p1 = Product("123", "p", 11.5, "b") 
    p.display() 
    p1.display() 