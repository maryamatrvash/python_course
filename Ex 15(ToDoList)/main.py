from manager import *
def main():
    list1 = Manager()
    while True:
        cmd = input("Add/Mark as done/Display/Details/Exit: ").lower() 
        
        if cmd == "add":
            t_id, title, description = input("task id,title,description: ").split(",")
            task1 = list1.create_task(t_id, title, description) 
            list1.add_task(task1)  
        
        elif cmd == "mark as done":
            t_id = input("Enter ID for mark the task done: ")
            list1.done_task(t_id) 

        elif cmd == "display":
            list1.display() 

        elif cmd == "details":
            list1.summary()  

        elif cmd == "":
            continue

        elif cmd == "exit":
            break

        else:
            print(f"{cmd}: Not Found!") 

if __name__ == "__main__":
    main() 