from pathlib import Path
import json



def write_file(data, file_path):  #✅
    """ Write the contentes to the JSON file. 
    
    Input:
        file_path: string
    Output:
        None
    """

    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            json.dump(data, file)
            print(f"✅ Sucess: {file_path} written.")
    except Exception as ex:
        print(f"❌ Error: {ex}")
        exit()



def read_file(file_path):  #✅
    """ Read the JSON file and convert its content into a
    dictionary. 
    
    Input: 
        file_path: string
    Output:
        json_to_dict: dictionary
    """

    try:
        with open(file_path, 'rt', encoding="utf-8") as file:
            json_to_dict = json.load(file)
            print(f"✅ Sucess: {file_path} read.")
            return json_to_dict
    except Exception as ex:
        print(f"❌ Error: {ex}")
        exit()
