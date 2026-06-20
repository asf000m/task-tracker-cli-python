import json
from pprint import pp

import file_handler
from __main__ import *



# ------------------------------------------------------------
# FILE
# ------------------------------------------------------------


def write_file():
    print(f"\n🟦 TEST: file_handler.py: <write_file>\n")
    
    tasks_test = [
        {
            "task_name": "First task", 
            "id": 1, 
            "description": "This is the description of the task", 
            "status": "todo", 
            "createdAt": "Sun Feb  1 16:35:53 2026", 
            "updatedAt": "Sun Feb  1 16:35:53 2026"
        },
        {
            "task_name": "2nd task", 
            "id": 2, 
            "description": "description of 2nd task", 
            "status": "todo", 
            "createdAt": "Sun Feb  1 17:11:04 2026", 
            "updatedAt": "Sun Feb  1 17:11:04 2026"
        }, 
        {
            "task_name": "3rd task of the file", 
            "id": 3, 
            "description": "description of 3rd task of the file", 
            "status": "to-do", 
            "createdAt": "Sun Feb  1 17:22:48 2026", 
            "updatedAt": "Sun Feb  1 17:22:48 2026"
        }
    ]
    file_name_test = "files/tasks_test.json"
    file_handler.write_file(tasks_test, file_name_test)

    print("\n🟥 END TEST\n")

    return file_name_test


file_name_test = write_file()


def read_file(file_path):
    print(f"\n🟦 TEST: file_handler.py: <read_file>\n")
    
    tasks = file_handler.read_file(file_path)
    
    print(type(tasks))
    pp(tasks)
    print("\n🟥 END TEST\n")


read_file(file_name_test)


# ------------------------------------------------------------
# CRUD
# ------------------------------------------------------------

