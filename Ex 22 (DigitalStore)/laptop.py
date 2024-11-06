from product import *

class Laptop(Product):
    def __init__(self, id_: str, name: str, price: float, 
                 brand: str, memory: str, processor: str):  
        super().__init__(id_, name, price, brand) 
        self.memory = memory
        self.processor = processor  

    def display(self):
        print(f"Laptop: {super().display()}, Memory: {self.memory}, Processor: {self.processor}") 

if __name__ == "__main__":
    l1 = Laptop("123", "l", 12.4, "c", 4, "p") 
    l2 = Laptop("123", "l2", 11.5, "a", "12", "p2") 
    l2.display() 
    l1.display()