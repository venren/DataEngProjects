import json
import os


def getKaggleCredentials():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'kaggle.json')  # Navigate up to project and then to data
        with open(file_path, "r") as f:
            kaggle_auth = json.load(f)
            username = kaggle_auth["username"]
            key = kaggle_auth["key"]
            return(username, key)
    except FileNotFoundError:
        print(f"Json file not found")
        return(None, None)
    except json.JSONDecodeError:
        print(f"Not a valid json")