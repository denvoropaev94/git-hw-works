import json
def read_json():
    with open("database02.json", "r") as file:
        data = json.load(file)
        return data