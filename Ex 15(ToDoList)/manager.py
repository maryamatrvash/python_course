from task import *
class Manager:
    def __init__(self):
        self.tasks = {} 

    def create_task(self, t_id, title, description):
        new_task = Task(t_id, title, description) 
        return new_task 
    
    def add_task(self, task):
        if task.t_id not in self.tasks:
            self.tasks[task.t_id] = task
            print("Added!")
        else:
            print("ID already exist!") 

    def display(self):
        if not self.tasks:
            print("Empty!") 
        for task in self.tasks.values():
            print(task) 

    def done_task(self, t_id):
        if t_id in self.tasks: 
            task = self.tasks[t_id]
            task.status = True 
            task.end_time = datetime.datetime.now() 
            task.end_time = task.end_time.strftime("%c")   
        else:
            print("Task Not Found!")

    def summary(self):
        number_of_tasks = len(self.tasks)
        status_of_tasks = [task.status for task in self.tasks.values()]
        done = status_of_tasks.count(True) 
        undone = number_of_tasks - done 
        print(f"Number of Tasks: {number_of_tasks}, Compeleted tasks: {done}, Uncompeleted: {undone}") 
    

if __name__ == "__main__":
    t = Manager()
    task1 = t.create_task("123", "t1", "abc")
    t.add_task(task1) 
    task2 = t.create_task("143", "t2", "bbb") 
    t.add_task(task2)  
    t.done_task("123")  
    t.display() 
    t.summary() 