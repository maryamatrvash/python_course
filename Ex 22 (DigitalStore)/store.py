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
        flag = True 
        for product in self.products.values():
            if id_ in product: 
                flag = False
                del product[id_]
                return f"ID: {id_} removed!" 
        if flag :
            print("Not Found") 

    @staticmethod
    def show_info(data, p_type):
        print(10*" "+ "*" + p_type + "*") 
        for p in data.values():
            print(p)
        if not data:
            print("Empty") 

    def display(self, product_type=None): 
        if product_type:
            try: 
                products = self.products[product_type] 
            except:
                print("Not found!") 
            else:
                self.show_info(products, product_type) 
        else:
            for k, v in self.products.items():
                self.show_info(v, k) 


if __name__ == "__main__":
    s1 = Store("s1")
    l1 = Laptop("1234", "l1", 22.6, "b", "12", "p")
    p1 = Phone("123", "p1", 11.5, "c") 
    l2 = Laptop("1001", "l2", 22.6, "b", "12", "p") 
    s1.add_product(l1) 
    s1.add_product(l2) 
    s1.add_product(p1) 
    #print(s1.products) 
    #s1.remove_product("123")  
    #print(s1.products) 
    s1.display("laptops")   