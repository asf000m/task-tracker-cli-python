import json
from pprint import pp

import repository



# ------------------------------------------------------------
# FILE
# ------------------------------------------------------------


def write_file():
    print(f"\n🟦 TEST: file_handler.py: <write_file>\n")
    
    tasks_test = {
        0: {
            "id": 0,
            "task_name": "First task", 
            "description": "This is the description of the task", 
            "status": "todo", 
            "createdAt": "Sun Feb  1 16:35:53 2026", 
            "updatedAt": "Sun Feb  1 16:35:53 2026"
        },
        1: {
            "id": 1, 
            "task_name": "2nd task", 
            "description": "description of 2nd task", 
            "status": "todo", 
            "createdAt": "Sun Feb  1 17:11:04 2026", 
            "updatedAt": "Sun Feb  1 17:11:04 2026"
        },
        2: {
            "id": 2,
            "task_name": "3rd task of the file",
            "description": "description of 3rd task of the file",
            "status": "to-do",
            "createdAt": "Sun Feb  1 17:22:48 2026",
            "updatedAt": "Sun Feb  1 17:22:48 2026"
        }
    }
    file_name_test = "data/tasks_test.json"
    repository.write_file(file_name_test, tasks_test)

    print("\n🟥 END TEST\n")

    return file_name_test



def read_file(file_path):
    print(f"\n🟦 TEST: file_handler.py: <read_file>\n")
    
    tasks = repository.read_file(file_path)
    
    print(type(tasks))
    pp(tasks)
    print("\n🟥 END TEST\n")



# ------------------------------------------------------------
# TESTS
# ------------------------------------------------------------


file_name_test = write_file()
read_file(file_name_test)