from product import *

class Laptop(Product):
    unique_id = []
    def __init__(self, id_: str, name: str, price: float, 
                 brand: str, memory: str, processor: str): 
        id_ = Laptop.is_unique_id(id_) 
        super().__init__(id_, name, price, brand) 
        self.memory = memory
        self.processor = processor 

    @staticmethod
    def is_unique_id(id_):
        if id_ not in Laptop.unique_id:
            Laptop.unique_id.append(id_) 
            return id_
        else:
            print(f"ID: {id_} is available") 

    def display(self):
        print(f"Laptop: {super().display()}, Memory: {self.memory}, Processor: {self.processor}") 

if __name__ == "__main__":
    l1 = Laptop("123", "l", 12.4, "c", 4, "p") 
    l2 = Laptop("12", "l2", 11.5, "a", "12", "p2") 
    l2.display() 
    l1.display()