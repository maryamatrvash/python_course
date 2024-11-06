from product import *

class Phone(Product):
    unique_id = [] 
    def __init__(self, id_, name, price, brand):
        id_ = Phone.is_unique_id(id_) 
        super().__init__(id_, name, price, brand)

    @classmethod
    def is_unique_id(cls, id_):
        if id_ not in cls.unique_id:
            cls.unique_id.append(id_)
            return id_
        else:
            print(f"ID: {id_} is available")  

    def display(self):
        print(f"Phone: {super().display()}")  

if __name__ == "__main__":
    phone = Phone("123", "p", 11.5, "b")
    p2 = Phone("1034", "a", 10.0, "c") 
    p2.display() 
    phone.display() 
    print(Phone.unique_id)  