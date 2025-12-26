from getpass import getpass
from os import mkdir, rmdir
from src import functions as f

class reg:
    def create() -> None:
        registers = f.read("registers")["registers"]
        while True:
            cont = False
            while True:
                cn = input("What would be the codename of your register? (max 10 characters) ")
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
            regData["name"] = input("What will be the name of your register? ")
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
                        regData["accs"] = [input("What will be the name of the first account? ")]
                        break
                    mkdir("data/" + cn + "/accs")
                    f.create(cn + "/accs/" + regData["accs"][0])
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
        cn = input("What is the codename of the register you want to remove? ")
        registers = f.read("registers")["registers"]
        if cn in registers:
            regData = f.read(cn + "/data")
            if getpass("Password: ") != regData["pw"]:
                print("The password is not correct!")
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
        cn = input("What is the codename of the register you want to modify? ")
        registers = f.read("registers")["registers"]
        if cn in registers:
            regData = f.read(cn + "/data")
            if getpass("Password: ") == regData["pw"]:
                f.clear()
                print("1. Password\n2. Name\n3. Account usage\n4. Codename\n5. Cancel")
                print("------------------------------------------")
                while True:
                    choice = input("Enter the number of the action you want to take: ")
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
                            regData["name"] = input("What's the new name for this register? ")
                            print("The register's name was modified")
                            f.pause()
                            f.write(cn + "/data", regData)
                            break
                        elif choice == 3:
                            if regData["acc"]:
                                tfchoice = input("Accounts are enabled. Do you want to disable them?\nWARNING: This action will permanently delete all your accounts and their data from this register! (y/n) ")
                                while True:
                                    if tfchoice.startswith("y"):
                                        regData["acc"] = False
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
                                        input("Do you want to disable accounts? (y/n) ")
                            else:
                                regData["acc"] = True
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
                        f.write("registers", {"registers": registers})
                        break
                    except:
                        print("Unavailable choice!")
                        f.pause()
