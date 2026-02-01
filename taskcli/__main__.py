import sys
import json
import datetime


def add(task, description, task_list):
    """ Add a new task to the list"""

    new_id = str(len(task_list) + 1)    # create id number of the new task
    now = datetime.datetime.now().strftime('%c')    # set the date and time of the task

    # add new task and its properties
    task_list[new_id] = {
        'task': task,
        'id': int(new_id),
        'description': description,
        'status': 'to-do',
        'createdAt': now,
        'updatedAt': now
    }
    
    print('Task added successfully (ID: ' + new_id + ')')
    
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


def listAll(task_dict):
    """ List all tasks """

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
    task_dict = readFile(file_path)     # read JSON

    # define the command and arguments
    command = sys.argv[1]
    args = sys.argv[2:]

    # check for a command and execute it
    if command == 'list':
        listAll(task_dict)
    elif command == 'add':
        task_dict = add(args[0], args[1], task_dict)
        writeFile(file_path, task_dict)


if __name__ == '__main__':
    main()