import json
import glob
import os

def save_string_to_file(filepath, string_data):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(string_data)
    except IOError:
        return False
    return True

def save_json_to_file(filepath, json_data):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(json_data, file)
    except IOError:
        return False
    return True

def get_json_data_from_file(filepath):
    try:
        with open(filepath) as file:
            return json.load(file)
    except IOError:
        return False

def get_array_from_file_lines(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read().strip().split("\n")
    except:
        return False

def get_file_contents(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except:
        return False

def get_all_file_in_folder(path, file_type=""):
    if file_type != "":
        return glob.glob(path + "/*." + file_type)
    return glob.glob(path + "/*")

def get_folder_of_file(path):
    return os.path.dirname(path)

def get_filename(path):
    return os.path.basename(path)

def delete_file(filepath):
    os.remove(filepath)
    return True

def delete_folder(folderpath):
    os.rmdir(folderpath)
    return True