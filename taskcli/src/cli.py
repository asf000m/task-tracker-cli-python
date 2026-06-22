import sys

from services import *
from taskcli import file_handler



def main():

    file_path = "files/tasks_test.json"
    tasks = file_handler.read_file(file_path)

    # Define the command and arguments.
    command = sys.argv[1]
    args = sys.argv[2:]

    # Check for a command and execute it.
    if command == "list":
        list_all(tasks)
    
    elif command == "add":
        name_task = args[0]
        desc_task = args[1]
        tasks = add_task(name_task, desc_task, tasks)
    
    elif command == "delete":
        id_task = args[0]
        tasks = delete_task(id_task, tasks)
    
    elif command == "update":
        id_task = args[0]
        new_name = args[1]
        tasks = update_task(id_task, new_name, tasks)
    
    file_handler.write_file(file_path, tasks)



if __name__ == '__main__':
    main()