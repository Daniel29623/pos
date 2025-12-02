from getpass import getpass
from os import mkdir, rmdir, remove as rm
import functions as f

class reg:
    def create() -> None:
        registers = f.read("registers")
        while True:
            cn = input("What would be the codename of your register? (max 10 characters) ")
            if len(list(cn)) <= 10:
                break
        mkdir("data/" + cn)
        regData = f.create(cn + "/data")
        regData["name"] = input("What will be the name of your register? ")
        while True:
            pw = getpass("New password: ")
            pwa = getpass("Password again: ")
            if pw == pwa:
                regData["pw"] = pw
                break
        while True:
            acc = input("Will you be using accounts in this register? (y/n) ")
            if acc.lower().startswith("y"):
                regData["acc"] = True
                while True:
                    regData["accs"] = [input("What will be the name of the first account? ")]
                    if regData["accs"][0] != "main":
                        break
                f.create(cn + "/accs/" + regData["accs"][0])
                mkdir("data/" + cn + "/accs")
                break
            elif acc.lower().startswith("n"):
                regData["acc"] = False
                f.create(cn + "/main")
                break