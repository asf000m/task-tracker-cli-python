import json
from pprint import pp
import file_handler



# ------------------------------------------------------------
# FILE
# ------------------------------------------------------------


def write_file():
    print(f"\n🟦 TEST: file_handler.py: <write_file>\n")
    
    tasks_test = { 
        "id": 1,
        "task": "Buy groceries",
        "description": "Items for the dinner tonight at 7pm",
        "status": "todo",
        "createdAt": "2026-13-06 14:30:00",
        "updatedAt": ""
    }
    file_name_test = "tasks_test.json"
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


