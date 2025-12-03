from getpass import getpass
from os import mkdir, rmdir, remove as rm
from src import functions as f

class reg:
    def create() -> None:
        registers = f.read("registers")
        registers = registers["registers"]
        while True:
            running = True
            while running:
                cn = input("What would be the codename of your register? (max 10 characters) ")
                if len(list(cn)) <= 10 and len(list(cn)) > 0:
                    for char in list(cn):
                        if char == " ":
                            print("Codename can't contain spaces!")
                            f.pause()
                        else:
                            running = False
                            break
                else:
                    print("The codename must be more than 0 characters and not more then 10!")
                    f.pause()
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
            registers = {"registers": registers}
            f.write("registers", registers)
            f.write(cn + "/data", regData)
        except KeyboardInterrupt:
            f.rmAll(cn)
            rmdir("data/" + cn)