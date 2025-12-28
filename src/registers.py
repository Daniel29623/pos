from getpass import getpass
from os import mkdir, rmdir, remove
from src import functions as f

class acc:
    def create(cn: str) -> None:
        regData = f.read(cn + "/data")
        while True:
            cont = False
            acccn = input("New account codename: ")
            for char in list(acccn):
                if char == " ":
                    print("Account codename can't contain spaces!")
                    f.pause()
                    cont = True
                    break
            if cont:
                continue
            break
        regData["accs"].append(acccn)
        f.create(cn + "/accs/" + acccn)
        f.write(cn + "/accs/" + acccn, {"name": input("Account name: "), "stock": {}})
        f.write(cn + "/data", regData)
    def remove(cn: str) -> None:
        regData = f.read(cn + "/data")
        if len(regData["accs"]) == 1:
            print("At least 1 account must remain in the register!\nIf you want to delete this one too, go to the main menu and disable accounts in this register.")
            f.pause()
            return
        acccn = input("Account codename: ")
        if acccn in regData["accs"]:
            remove("data/" + cn + "/accs/" + acccn + ".json")
            regData["accs"].pop(regData["accs"].index(acccn))
        f.write(cn + "/data", regData)

class reg:
    def create() -> None:
        registers = f.read("registers")["registers"]
        while True:
            cont = False
            while True:
                cn = input("Codename: ")
                if len(list(cn)) <= 10 and len(list(cn)) > 0:
                    for char in list(cn):
                        if char == " ":
                            print("Codename can't contain spaces!")
                            f.pause()
                            cont = True
                            break
                    if cont:
                        continue
                else:
                    print("The codename must be more than 0 characters and no more then 10!")
                    f.pause()
                break
            try:
                mkdir("data/" + cn)
                break
            except FileExistsError:
                print("A register with this codename already exists!")
                f.pause()
        regData = f.create(cn + "/data")
        try:
            regData["name"] = input("Name: ")
            while True:
                pw = getpass("New password: ")
                pwa = getpass("Password again: ")
                if pw == pwa:
                    regData["pw"] = pw
                    break
                else:
                    print("Password's don't match!")
                    f.pause()
            while True:
                acc = input("Will you be using accounts in this register? (y/n) ")
                if acc.lower().startswith("y"):
                    regData["acc"] = True
                    while True:
                        cont = False
                        acccn = input("Account codename: ")
                        for char in list(acccn):
                            if char == " ":
                                print("Account codename can't contain spaces!")
                                f.pause()
                                cont = True
                                break
                        if cont:
                            continue
                        regData["accs"] = [acccn]
                        break
                    mkdir("data/" + cn + "/accs")
                    f.create(cn + "/accs/" + regData["accs"][0])
                    f.write(cn + "/accs/" + regData["accs"][0], {"name": input("Account name: "), "stock": {}})
                    break
                elif acc.lower().startswith("n"):
                    regData["acc"] = False
                    f.create(cn + "/main")
                    break
                else:
                    print("Please enter a valid answer!")
                    f.pause()
            registers.append(cn)
            f.write("registers", {"registers": registers})
            f.write(cn + "/data", regData)
        except KeyboardInterrupt:
            f.rmAll(cn)
            rmdir("data/" + cn)
    def remove() -> None:
        cn = input("Codename: ")
        registers = f.read("registers")["registers"]
        if cn in registers:
            regData = f.read(cn + "/data")
            if getpass("Password: ") != regData["pw"]:
                print("The password is incorrect!")
                f.pause()
                return
            if regData["acc"]:
                f.rmAll(cn + "/accs")
                rmdir("data/" + cn + "/accs")
            f.rmAll(cn)
            rmdir("data/" + cn)
            registers.pop(registers.index(cn))
            f.write("registers", {"registers": registers})
        else:
            print("There is no register with this codename!")
            f.pause()
    def modify() -> None:
        cn = input("Codename: ")
        registers = f.read("registers")["registers"]
        if cn in registers:
            regData = f.read(cn + "/data")
            if getpass("Password: ") == regData["pw"]:
                while True:
                    f.clear()
                    print("1. Password\n2. Name\n3. Account usage\n4. Codename\n5. Cancel")
                    print("------------------------------------------")
                    choice = input("Enter an action's number to take: ")
                    try: 
                        choice = int(choice)
                        if choice == 1:
                            while True:
                                pw = getpass("New password: ")
                                pwa = getpass("Password again: ")
                                if pw == pwa:
                                    regData["pw"] = pw
                                    print("Password has been changed!")
                                    f.pause()
                                    break
                                else:
                                    print("Password's don't match!")
                                    f.pause()
                                f.write(cn + "/data", regData)
                                break
                        elif choice == 2:
                            regData["name"] = input("New name: ")
                            print("The register's name has been modified")
                            f.pause()
                            f.write(cn + "/data", regData)
                            break
                        elif choice == 3:
                            if regData["acc"]:
                                tfchoice = input("Accounts are enabled. Do you want to disable them?\nWARNING: This action will permanently delete all your accounts and their data from this register! (y/n) ")
                                while True:
                                    if tfchoice.startswith("y"):
                                        regData["acc"] = False
                                        regData.pop("accs")
                                        f.rmAll(cn + "/accs")
                                        rmdir("data/" + cn + "/accs")
                                        f.create(cn + "/main")
                                        print("Accounts are now disabled")
                                        f.pause()
                                        break
                                    elif tfchoice.startswith("n"):
                                        print("Canceled")
                                        f.pause()
                                        break
                                    else:
                                        print("Not a valid choice!")
                                        f.pause()
                                        tfchoice = input("Do you want to disable accounts? (y/n) ")
                            else:
                                regData["acc"] = True
                                while True:
                                    cont = False
                                    acccn = input("New account's codename: ")
                                    for char in list(acccn):
                                        if char == " ":
                                            print("Account codename can't contain spaces!")
                                            f.pause()
                                            cont = True
                                            break
                                    if cont:
                                        continue
                                    regData["accs"] = [acccn]
                                    break
                                remove("data/" + cn + "/main.json")
                                mkdir("data/" + cn + "/accs")
                                f.create(cn + "/accs/" + regData["accs"][0])
                                f.write(cn + "/accs/" + regData["accs"][0], {"name": input("Account name: "), "stock": {}})
                                print("Accounts are now enabled")
                                f.pause()
                            f.write(cn + "/data", regData)
                            break
                        elif choice == 4:
                            cont = False
                            while True:
                                ncn = input("New codename: ")
                                if len(list(ncn)) <= 10 and len(list(ncn)) > 0:
                                    for char in list(ncn):
                                        if char == " ":
                                            print("Codename can't contain spaces!")
                                            f.pause()
                                            cont = True
                                            break
                                    if cont:
                                        continue
                                else:
                                    print("The codename must be more than 0 characters and no more then 10!")
                                    f.pause()
                                break
                            registers[registers.index(cn)] = ncn
                            try:
                                mkdir("data/" + ncn)
                            except:
                                print("Codename occupied!")
                                f.pause()
                                continue
                            if regData["acc"]:
                                mkdir("data/" + ncn + "/accs")
                                for acc in regData["accs"]:
                                    f.create(ncn + "/accs/" + acc)
                                    f.write(ncn + "/accs/" + acc, f.read(cn + "/accs/" + acc))
                                f.rmAll(cn + "/accs")
                                rmdir("data/" + cn + "/accs")
                            else:
                                f.create(ncn + "/main")
                                f.write(ncn + "/main", f.read(cn + "/main"))
                            f.create(ncn + "/data")
                            f.write(ncn + "/data", f.read(cn + "/data"))
                            f.rmAll(cn)
                            rmdir("data/" + cn)
                        elif choice == 5:
                            return
                        else:
                            print("Not an available choice!")
                            f.pause()
                            continue
                        f.write("registers", {"registers": registers})
                        break
                    except:
                        print("Unavailable choice!")
                        f.pause()
            else:
                print("The password is incorrect!")
                f.pause()
        else:
            print("There is no register with this codename!")
            f.pause()
