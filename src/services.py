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
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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



def update_task(id_task, new_name, new_description, tasks):
    """ Change the task name of the task. """
    
    task = tasks[id_task]
    task["task_name"] = new_name
    task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if new_description:
        task["description"] = new_description
    print(f"✅ Sucess: task updated (ID: {id_task}).\n")

    return tasks



def delete_task(id_task, tasks):
    """ Delete a task. """

    # First check if the ID of the task is in dictionary of tasks.
    if id_task in tasks:
        name_task = tasks[id_task]["task_name"]
        id_task = tasks[id_task]["id"]
        tasks.pop(id_task)
        
        print(
            "Task deleted:\n"
            f"{name_task} (ID: {id_task})\n"
        )
        
        return tasks
    else:
        print(f"Task ID {id_task} not found.\n")
        
        return tasks



def mark_todo(id_task, tasks):
    """ Change the status of a task as 'todo'. """
    pass


def mark_in_progress(id_task, tasks):
    """ Change the status of a task as 'in-progress'. """
    
    if id_task in tasks:
        task = tasks[id_task]
        task["status"] = "in-progress"
    else:
        print("❌ Error: task ID not found.\n")
    
    return tasks



def mark_done(id_task, tasks):
    """ Change the status of a task as 'done'. """
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
