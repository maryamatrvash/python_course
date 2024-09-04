#write code here

to_do_list = {}

def menu():
    menu = """
    Activities Management System:
    1. Add Task
    2. Delete Task
    3. Update Task
    4. Display all Tasks
    5. Search Task
    6. Mark as done
    7. Display Details
    8. Help
    9. Exit"""
    print(menu) 

def calculate_duration():
    start = input("Enter start time: ").strip()
    stop = input("Enter end time: ").strip()
    start = start.split(":")
    stop = stop.split(":") 
    
    start_h = int(start[0])
    start_m = int(start[1])
    stop_h = int(stop[0])
    stop_m = int(stop[1])

    time = (stop_h*60 + stop_m) - (start_h*60 + start_m)
    time_h = time // 60
    time_m = time % 60
    duration = f"{time_h}:{time_m}" 
    return duration 

def add_task():
    task_id = input("Enter task ID: ").strip()
    if task_id in to_do_list:
        print(f"The task: {task_id} is already exist!")
        return
    name = input("Enter the name of task: ").lower()
    status = input("Have you done it? (done or undone): ").lower()
    if status == "done":
        duration = calculate_duration() 
    else:
        duration = None
    tasks = {
        "name": name,
        "status": status,
        "duration": duration  
    }
    to_do_list[task_id] = tasks 
    print("Added!") 

def remove_task(task_id):
    if task_id not in to_do_list:
        print("ID not found!")
        return
    to_do_list.pop(task_id)
    print("Removed!")

def edit_task(task_id):
    if task_id in to_do_list:
        new_name = input("Enter new name: ").lower()
        new_status = input("Enter new status: ").lower()
        new_duration = calculate_duration() 
        to_do_list[task_id]["name"] = new_name or to_do_list[task_id]["name"]
        to_do_list[task_id]["status"] = new_status or to_do_list[task_id]["status"]
        to_do_list[task_id]["duration"] = new_duration or to_do_list[task_id]["duration"] 
        print("Updated!")
        return
    print("ID not found!") 

def display_task(value):
    for k, v in value.items():
            print(f"{k}: {v}")

def display_all():
    if not to_do_list:
        print("Empty!")
        return
    
    for key , value in to_do_list.items():
        print(f"-({key})-")
        display_task(value) 
          
def search():
    search_id = input("Search by: 1.id or 2.name or 3.duration: ").strip()
    if search_id == "1":
        task_id = input("Enter ID for search: ")
        search_by_id(task_id)
    elif search_id == "2":
        name = input("Enter name for search: ")
        search_by_name(name)
    elif search_id == "3":
        start_time = input("Duration start time: ")
        stop_time = input("Duration stop time: ") 
        search_by_duration(start=start_time, stop=stop_time) 
    else:
        print("Try again!")

def search_by_id(task_id):
    if task_id in to_do_list:
        task = to_do_list[task_id]
        display_task(task) 
        return 
    print("ID not found!") 

def search_by_name(name):
    for value in to_do_list.values():
        if value["name"] == name:
            display_task(value) 
        else: 
            print("Not found!") 

def search_by_duration(start=0, stop=float('inf')):
    not_found = True
    for value in to_do_list.values():
        if start <= value["duration"] <= stop:
            not_found = False
            display_task(value)
    if not_found:
        print("Not found!") 

def mark_as_done(task_id):
    if task_id in to_do_list:
        to_do_list[task_id]["status"] = "done"
        to_do_list[task_id]["duration"] = calculate_duration()
        print("Task done!") 
        return
    print("ID not found!") 

def details():
    num_task = len(to_do_list)
    print(f"Number of tasks: {num_task}")
    
    total_time = 0
    for time in to_do_list.values():
        time["duration"] = str(time["duration"]) 
        if time["duration"] != "None":
            time_ = time["duration"].split(":") 
            time_h = int(time_[0])
            time_m = int(time_[1]) 
            total_time += time_h*60 + time_m 
    total_time_h = total_time // 60
    total_time_m = total_time % 60
    print(f"Total time: {total_time_h}:{total_time_m}")

    compeleted = 0
    uncompeleted = 0
    for value in to_do_list.values():
        if value["status"] == "done":
            compeleted += 1 
        else: 
            uncompeleted += 1
    print(f"Compeleted Tasks: {compeleted} \nUncompeleted Tasks: {uncompeleted}") 

def help():
    string = """
    Add is for appending a task to your list
    Delete is for removing a task from list
    Update is for editing a task
    Display all task will show you all the details like name, status, and duration
    Search is for find a task by name or status or duration
    Mark as done is for updating the status of a task
    Display details shows the number of tasks, hours worked, compelete or uncompeleted tasks"""
    print(string)

def main():

    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task() 
        elif choice == "2":
            task_id = input("Enter ID for delete: ").strip()
            remove_task(task_id)
        elif choice == "3":
            task_id = input("Enter ID for update: ").strip()
            edit_task(task_id)
        elif choice == "4":
            display_all() 
        elif choice == "5":
            search()
        elif choice == "6":
            task_id = input("Enter ID for mark as done: ").strip() 
            mark_as_done(task_id)
        elif choice == "7":
            details()
        elif choice == "8":
            help() 
        elif choice == "9":
            break
        elif choice == "":
            continue
        else: 
            print("Invalid option! Try again")

main() 