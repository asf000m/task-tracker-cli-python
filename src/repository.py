from pathlib import Path
import json



def write_file(file_path, tasks):
    """ Write the contentes to the JSON file. 
    
    Input:
        file_path: string
    Output:
        None
    """

    root_path = Path(__file__).resolve().parent.parent
    file_path_ = root_path / file_path

    try:
        with open(file_path_, "w", encoding="utf-8") as file:
            json.dump(tasks, file)
            print(f"✅ Sucess: {file_path} written.\n")
    except Exception as ex:
        print(f"❌ Error: {ex}")
        exit()



def read_file(file_path):
    """ Read the JSON file and convert its content into a
    dictionary. 
    
    Input: 
        file_path: string
    Output:
        json_to_dict: dictionary
    """

    root_path = Path(__file__).resolve().parent.parent
    file_path_ = root_path / file_path

    try:
        with open(file_path_, 'rt', encoding="utf-8") as file:
            json_to_dict = json.load(file)
            print(f"✅ Sucess: {file_path} read.\n")
            
            return json_to_dict
    except Exception as ex:
        print(f"❌ Error: {ex}")
        exit()
