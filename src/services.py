from datetime import datetime
from pprint import pp



def add_task(name_task, description, tasks):
    """ Add a new task to the list. 
    
    Input:
        - task_name: string
        - description: string
        - tasks: dictionary
    Output:
        - tasks: dictionary
    """

    # Create a new ID number for the new task.
    ids_tasks = [int(id_task) for id_task in tasks.keys()]
    max_id = max(ids_tasks)
    new_id = str(max_id + 1)
    
    # Set the date and time of the task.
    now = datetime.now().strftime('%c')    

    # Add the new task and its properties to the dictionary.
    tasks[new_id] = {
        'id': new_id,
        'task_name': name_task,
        'description': description,
        'status': 'to-do',
        'createdAt': now,
        'updatedAt': now
    }
    
    print(f"\n✔️ Task added successfully (ID: {new_id})\n")
    
    return tasks



def update_task(id_task, name_task, tasks):
    """ Change the task name of the task. """
    
    



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



def mark_todo(id_task):
    """ Mark a task as todo. """
    pass


def mark_in_progress(id_task):
    """ Mark a task as in progress. """
    pass



def mark_done(id_task):
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



def list_by_status():
    """ List tasks by status. """
    
    pass