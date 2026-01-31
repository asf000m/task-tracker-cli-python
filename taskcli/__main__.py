import sys
import json
import datetime

def add(task, description, task_list):
    """ Add a new task to the list"""

    new_id = str(len(task_list) + 1)    # create id number of the new task

    now = datetime.datetime.now().strftime('%c')

    # add new task and its properties
    task_list[new_id] = {
        'task': task,
        'id': int(new_id),
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    return task_list

def update():
    """ Change a task in the list to another """
    return 0

def delete():
    """ Delete a task """
    return 0

def markInProgress():
    """ Mark a task as in progress """
    return 0

def markDone():
    """ Mark a task as done """
    return 0

def listAll():
    """ List all tasks """
    return 0

def listByStatus():
    """ List tasks by status """
    return 0

def main():

    # read JSON
    some_json = '{}'
    task_list = {}

    # define the command and arguments
    command = sys.argv[1]
    args = sys.argv[2:]

    # check for a command and execute it
    if command == 'list':
        for task in task_list:
            print(task['task'], task['description'])
    elif command == 'add':
        task_list = add(args[0], args[1], task_list)

    # write to JSON
    some_json = json.dumps(task_list)
    print(some_json)


if __name__ == '__main__':
    main()