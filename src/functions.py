from json import load, dumps
from os import name, system, listdir, remove

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def pause():
    if name == "nt":
        system("pause > nul")
    else:
        system("read -n 1 -s")

def create(path_name: str) -> dict:
    with open("data/" + path_name + ".json", "w") as json:
        json.write(dumps({}) + "\n")
    with open("data/" + path_name + ".json", "r") as json:
        data = load(json)
    return data
def read(path_name: str) -> dict:
    with open("data/" + path_name + ".json", "r") as json:
        data = load(json)
    return data
def write(path_name: str, data: dict) -> None:
    with open("data/" + path_name + ".json", "w") as json:
        json.write(dumps(data) + "\n")

def rmAll(path: str) -> None:
    for file in listdir("data/" + path):
        remove("data/" + path + "/" + file)