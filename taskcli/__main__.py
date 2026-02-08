import sys
import json
import datetime


def addTask(task, description, task_dict):
    """ Add a new task to the list"""

    new_id = str(len(task_dict) + 1)    # create id number of the new task
    now = datetime.datetime.now().strftime('%c')    # set the date and time of the task

    # add new task and its properties
    task_dict[new_id] = {
        'task': task,
        'id': int(new_id),
        'description': description,
        'status': 'to-do',
        'createdAt': now,
        'updatedAt': now
    }
    
    print('\nTask added successfully (ID: ' + new_id + ')\n')
    
    return task_dict


def updateTask():
    """ Change a task in the list to another """
    return 0


def deleteTask(id, task_dict):
    """ Delete a task """

    # first check if the id of the task is in the list of tasks
    if id in task_dict:
        task = task_dict[str(id)]['task']
        task_id = task_dict[str(id)]['id']

        print('\nTask deleted:\n')
        print(f'{task} (ID: {task_id})\n')

        task_dict.pop(str(id))

        return task_dict
    else:
        print('\nTask ID not found.\n')
        return task_dict


def markTaskInProgress():
    """ Mark a task as in progress """
    return 0


def markTaskDone():
    """ Mark a task as done """
    return 0


def listAllTasks(task_dict):
    """ List all tasks """

    print('List of all tasks:\n')
    for task_properties in task_dict.values():
        print('Task:\t\t', task_properties['task'])
        print('Description:\t', task_properties['description'])
        print('Status:\t\t', task_properties['status'])
        print('ID:\t\t', task_properties['id'])
        print('\n')


def listByStatus():
    """ List tasks by status """
    return 0


def readFile(file_path):
    """ Handle the reading of the JSON file and convert its content into a
    dictionary """

    with open(file_path, 'rt') as file:
        json_to_dict = json.loads(file.read())

    return json_to_dict


def writeFile(file_path, data):
    """ Handle the writing of the JSON file """

    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)


def main():

    file_path = 'test.json'
    task_dict = readFile(file_path)  # read JSON

    # define the command and arguments
    command = sys.argv[1]
    args = sys.argv[2:]

    # check for a command and execute it
    if command == 'list':
        listAllTasks(task_dict)
    elif command == 'add':
        task_dict = addTask(args[0], args[1], task_dict)
        writeFile(file_path, task_dict)
    elif command == 'delete':
        task_dict = deleteTask(args[0], task_dict)
        writeFile(file_path, task_dict)


if __name__ == '__main__':
    main()