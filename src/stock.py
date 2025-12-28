from src import functions as f
from getpass import getpass

def create(cn: str, stocktable: dict) -> dict:
    if getpass("Password: ") != f.read(cn + "/data")["pw"]:
        print("Password is incorrect!")
        f.pause()
        return stocktable
    code = input("EAN-8 code: ")
    if len(list(code)) != 8:
        print("Code not in EAN-8 format")
        f.pause()
        return stocktable
    try:
        tcode = int(code)
    except:
        print("Code not in EAN-8 format")
        f.pause()
        return stocktable
    modstocktable = stocktable
    modstocktable[code] = {}
    modstocktable[code]["name"] = input("Name: ")
    price = input("Price: ")
    try:
        price = int(price)
    except:
        print("Price entered is not valid!")
        f.pause()
        return stocktable
    modstocktable[code]["price"] = price
    modstocktable[code]["stock"] = 0
    return modstocktable
def remove(cn: str, stocktable: dict) -> dict:
    if getpass("Password: ") != f.read(cn + "/data")["pw"]:
        print("Password is incorrect!")
        f.pause()
        return stocktable
    code = input("Code: ")
    if code in stocktable:
        stocktable.pop(code)
        return stocktable
    else:
        print("Item not found!")
        f.pause()
        return stocktable
def modify(cn: str, stocktable: dict, accname: str) -> dict:
    if getpass("Password: ") != f.read(cn + "/data")["pw"]:
        print("Password is incorrect!")
        f.pause()
        return stocktable
    code = input("Code: ")
    if code in stocktable:
        while True:
            f.clear()
            print(f.read(cn + "/data")["name"])
            if accname != "":
                print(accname)
            print("------------------------------------------")
            print("1. Name\n2. Price\n3. Code\n4. Cancel")
            choice = input("Enter an action's number to take: ")
            try:
                choice = int(choice)
            except:
                print("Not an available choice!")
                f.pause()
                return stocktable
            if choice == 1:
                stocktable[code]["name"] = input("New name: ")
                return stocktable
            elif choice == 2:
                price = input("New price: ")
                try:
                    price = int(price)
                except:
                    print("Price entered is not valid!")
                    f.pause()
                    return stocktable
                stocktable[code]["price"] = price
                return stocktable
            elif choice == 3:
                ncode = input("New EAN-8 code: ")
                if len(list(ncode)) != 8:
                    print("Code not in EAN-8 format")
                    f.pause()
                    return stocktable
                try:
                    tncode = int(ncode)
                except:
                    print("Code not in EAN-8 format")
                    f.pause()
                    return stocktable
                stocktable[ncode] = stocktable[code]
                stocktable.pop(code)
                return stocktable
            elif choice == 4:
                return stocktable
            else:
                print("Not an available choice!")
                f.pause()
                return stocktable
    else:
        print("Item not found!")
        f.pause()
        return stocktable
def stockmod(cn: str, stocktable: dict) -> dict:
    code = input("Code: ")
    if getpass("Password: ") != f.read(cn + "/data")["pw"]:
        print("Password is incorrect!")
        f.pause()
        return stocktable
    if code in stocktable:
        amount = input("Amount to change ([+]/- <amount>): ")
        try:
            amount = int(amount)
        except:
            print("Not a valid amount!")
            f.pause()
            return stocktable
        stocktable[code]["stock"] += amount
        return stocktable
    else:
        print("Item not found!")
        f.pause()
        return stocktable
