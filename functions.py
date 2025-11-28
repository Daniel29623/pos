from json import load, dumps
from os import name, system

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

def read(path_name: str) -> dict:
    with open(path_name + ".json", "r") as json:
        data = load(json)
    return data
def write(path_name: str, data: dict) -> None:
    with open(path_name + ".json", "w") as json:
        json.write(dumps(data) + "\n")
