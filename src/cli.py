import sys

from services import *
from repository import *



def main():

    file_path = "data/tasks_test.json"
    tasks = read_file(file_path)

    # Define the command and arguments.
    command = sys.argv[1]
    args = sys.argv[2:]

    # Check for a command and execute it.
    if command == "list":
        list_all(tasks)
    
    elif command == "add":
        if len(args) < 2:
            print("❌ Error: Missing task name or description.\n")
            return
        
        name_task = args[0]
        desc_task = args[1]
        tasks = add_task(name_task, desc_task, tasks)
    
    elif command == "delete":
        if len(args) < 1:
            print("❌ Error: Missing task ID.\n")

        id_task = args[0]
        tasks = delete_task(id_task, tasks)
    
    elif command == "update":
        if len(args) < 2:
            print("❌ Error: Missing task ID or new name.\n")

        id_task = args[0]
        new_name = args[1]
        try:
            new_description = args[2]
        except Exception:
            new_description = ""
        tasks = update_task(id_task, new_name, new_description, tasks)
    
    elif command == "mark-in-progress":
        if len(args) < 1:
            print("❌ Error: Missing task ID.\n")
        
        id_task = args[0]
        tasks = mark_in_progress(id_task)
    
    write_file(file_path, tasks)



if __name__ == '__main__':
    main()