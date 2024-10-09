import datetime

class Task:
    def __init__(self, id_, title, description): 
        self.is_valid_id(id_) 
        self.t_id = id_
        self.title = title
        self.description = description 
        self.start_time = datetime.datetime.now() 
        self.end_time = None 
        self.status = False 

    @staticmethod
    def is_valid_id(id_):
        if not id_.isdigit():  
            raise ValueError("ID must be digit!")  
        
        
    def __str__(self):
        return f"ID: {self.t_id}, Title: {self.title}, Description: {self.description}, Start: {self.start_time.strftime('%c')}, End: {self.end_time}, Status: {self.status}" 


if __name__ == "__main__":
    t1 = Task("123", "t1", "abc")
    print(t1)   
    t2 = Task("234", "t2", "aaa")
    print(t2)    
