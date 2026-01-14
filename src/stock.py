from src import functions as f
from getpass import getpass

def main(cn: str, stocktable: dict, accname: str) -> dict:
    if getpass("Password: ") != f.read(cn + "/data")["pw"]:
        print("Password is incorrect!")
        f.pause()
        return stocktable
    while True:
        f.clear()
        print(f.read(cn + "/data")["name"])
        if accname != "":
            print(accname)
        print("------------------------------------------")
        print("Item no.  Stock  Price  Name")
        print("------------------------------------------")
        for itemno, itemdesc in stocktable.items():
            print(f"{itemno}  {itemdesc["stock"]} {' ' * (5 - len(list(str(itemdesc["stock"]))))} {itemdesc["price"]} {' ' * (5 - len(list(str(itemdesc["price"]))))} {itemdesc["name"]}")
        print("------------------------------------------")
        print("1. Modify stock\n2. Create item\n3. Modify item\n4. Remove item\n5. Exit Editing Mode")
        choice = input("Enter an action's number to take: ")
        try:
            choice = int(choice)
            if choice == 1:
                stocktable = act.stockmod(cn, stocktable)
            elif choice == 2:
                stocktable = act.create(cn, stocktable)
            elif choice == 3:
                stocktable = act.modify(cn, stocktable, accname)
            elif choice == 4:
                stocktable = act.remove(cn, stocktable)
            elif choice == 5:
                break
            else:
                raise ValueError
        except:
            print("Not a valid choice!")
            f.pause()
            continue
    return stocktable

class act:
    def create(cn: str, stocktable: dict) -> dict:
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
        if code in stocktable:
            print("An item with this code already exists in the stocktable!")
            f.pause()
            return stocktable
        modstocktable = stocktable.copy()
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
        code = input("Code: ")
        if code in stocktable:
            stocktable.pop(code)
            return stocktable
        else:
            print("Item not found!")
            f.pause()
            return stocktable
    def modify(cn: str, stocktable: dict, accname: str) -> dict:
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
