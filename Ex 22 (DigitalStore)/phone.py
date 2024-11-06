from product import *

class Phone(Product): 
    def __init__(self, id_, name, price, brand):
        super().__init__(id_, name, price, brand)  

    def display(self):
        print(f"Phone: {super().display()}")  

if __name__ == "__main__":
    phone = Phone("123", "p", 11.5, "b")
    p2 = Phone("123", "a", 10.0, "c") 
    p2.display() 
    phone.display() 
    print(Phone.unique_id)  