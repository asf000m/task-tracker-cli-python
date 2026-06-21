import sys
import json
from datetime import datetime
from pprint import pp

from taskcli import file_handler



def add_task(task_name, description, tasks):
    """ Add a new task to the list. 
    
    Input:
        - task_name: string
        - description: string
        - tasks: dictionary
    Output:
        - tasks: dictionary
    """

    # create id number of the new task
    new_id = len(tasks) + 1
    
    # set the date and time of the task
    now = datetime.now().strftime('%c')    

    # add a new task and its properties
    tasks[new_id] = {
        'task_name': task_name,
        'id': new_id,
        'description': description,
        'status': 'to-do',
        'createdAt': now,
        'updatedAt': now
    }
    
    print(f"\n✔️ Task added successfully (ID: {new_id})\n")
    
    return tasks



def update_task():
    """ Change a task in the list to another. """
    pass



def delete_task(id, tasks):
    """ Delete a task. """

    # First check if the ID of the task is in dictionary of tasks.
    if id in tasks:
        name_task = tasks[id]["task_name"]
        id_task = tasks[id]["id"]
        print(
            "Task deleted:\n"
            f"{name_task} (ID: {id_task})\n"
        )
        tasks.pop(id)
        
        return tasks
    else:
        print(f"Task ID {id} not found.\n")
        
        return tasks



def mark_todo():
    """ Mark a task as todo. """
    pass


def mark_in_progress():
    """ Mark a task as in progress. """
    pass



def mark_done():
    """ Mark a task as done. """
    pass



def list_all(tasks):
    """ List all tasks. 
    
    Input:
        - tasks: list
    Output:
        - None
    """

    print('List of all tasks:\n')

    for task in tasks.values():
        print(
            f"ID:\t\t{task["id"]}\n"
            f"Task:\t\t{task["task_name"]}\n"
            f"Description:\t{task["description"]}\n"
            f"Status:\t\t{task["status"]}\n"
            f"Created at:\t{task["createdAt"]}\n"
            f"Updated at:\t{task["updatedAt"]}\n"
        )



def listByStatus():
    """ List tasks by status. """
    return 0



def main():

    file_path = "files/tasks_test.json"
    tasks = file_handler.read_file(file_path)

    # define the command and arguments
    command = sys.argv[1]
    args = sys.argv[2:]

    # check for a command and execute it
    if command == 'list':
        list_all(tasks)
    
    elif command == 'add':
        name_task = args[0]
        desc_task = args[1]
        
        tasks = add_task(name_task, desc_task, tasks)
        file_handler.write_file(file_path, tasks)
    
    elif command == 'delete':
        id_task = args[0]
        
        tasks = delete_task(id_task, tasks)
        file_handler.write_file(file_path, tasks)



if __name__ == '__main__':
    main()