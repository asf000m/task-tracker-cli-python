import sys
import json
from datetime import datetime

from taskcli import file_handler



def addTask(task_name, description, tasks):
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



def updateTask():
    """ Change a task in the list to another """
    return 0



def deleteTask(id, tasks):
    """ Delete a task """

    # first check if the id of the task is in the list of tasks
    if id in tasks:
        task = tasks[str(id)]['task']
        task_id = tasks[str(id)]['id']

        print('\nTask deleted:\n')
        print(f'{task} (ID: {task_id})\n')

        tasks.pop(str(id))
        return tasks
    else:
        print('\nTask ID not found.\n')
        return tasks



def markTaskInProgress():
    """ Mark a task as in progress """
    return 0



def markTaskDone():
    """ Mark a task as done """
    return 0



def list_all(tasks):
    """ List all tasks. 
    
    Input:
        - tasks: list
    Output:
        - None
    """

    print('List of all tasks:\n')

    for task in tasks:
        print(
            f"ID:\t\t{task["id"]}\n"
            f"Task:\t\t{task["task_name"]}\n"
            f"Description:\t{task["description"]}\n"
            f"Status:\t\t{task["status"]}\n"
            f"Created at:\t{task["createdAt"]}\n"
            f"Updated at:\t{task["updatedAt"]}\n"
        )



def listByStatus():
    """ List tasks by status """
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
        addTask(args[0], args[1], tasks)
        file_handler.write_file(file_path, tasks)
    
    elif command == 'delete':
        deleteTask(args[0], tasks)
        file_handler.write_file(file_path, tasks)



if __name__ == '__main__':
    main()