from phone import *
from laptop import *

class Store:
    def __init__(self, name):
        self.name = name
        self.products = {
            "phones": {},
            "laptops": {} 
        }

    def add_product(self, obj):
        object = type(obj).__name__.lower() + "s" 
        self.products[object][obj.id_] = obj   
        print("Added!") 

    def remove_product(self, id_):
        for product in self.products.values():
            if id_ in product:
                del product[id_]
                print("removed") 


if __name__ == "__main__":
    s1 = Store("s1")
    l1 = Laptop("1234", "l1", 22.6, "b", "12", "p")
    p1 = Phone("123", "p1", 11.5, "c") 
    l2 = Laptop("1001", "l2", 22.6, "b", "12", "p") 
    s1.add_product(l1) 
    s1.add_product(l2) 
    s1.add_product(p1) 
    print(s1.products) 
    s1.remove_product("123") 
    print(s1.products) 
    