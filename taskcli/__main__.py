import sys

def add():
    """ Add a new task """
    return 0

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
    print('in main...')

    args = sys.argv[1:]

    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    print('Hello world!')

if __name__ == '__main__':
    main()