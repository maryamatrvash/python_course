class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def turn_on(self):
        print("Device is powered on!")

    def turn_off(self):
        print("Device is powered off!")

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}" 
    
class Laptop(Device):
    def __init__(self, brand, model, price, ram):
        super().__init__(brand, model, price)
        self.ram_size = ram

    def open_laptop(self):
        print("Laptop is opened!") 

    def __str__(self):
        return f"{super().__str__()}, Ram Size: {self.ram_size} GB" 
    
class Smartphone(Device):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera_resolution = camera

    def take_photo(self):
        print("A photo has been taken!")

    def __str__(self): 
        return f"{super().__str__()}, Camera Resolution: {self.camera_resolution} MP" 
    

l1 = Laptop("a", "12", 200, 4)
l1.open_laptop() 
print(l1) 
s1 = Smartphone("b", "20", 1000, 45)
s1.take_photo() 
s1.turn_off() 
print(s1) 