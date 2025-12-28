from src import functions as f
from src.registers import acc
from src import stock
from getpass import getpass

class act:
    def sell(stocktable: dict, name: str, accname: str) -> None:
        cart = []
        while True:
            f.clear()
            print(name)
            if accname != "":
                print(accname)
            print("------------------------------------------")
            print("Cart:")
            if len(cart) == 0:
                print("                  EMPTY")
            else:
                print("Amount  Item Name")
                for item in cart:
                    print(f"{item["amount"]} {' ' * 6 - len(list(item["amount"]))} {stocktable[item["code"]]["name"]}")
            print("------------------------------------------")
            print("Any number below or equal to 1000 will count as an amount specifier\nLeave the field empty to get the total\nPut X if you want to go back!")
            action = input()
            if action == "":
                total = 0
                for item in cart:
                    total += stocktable[item["code"]]["price"] * item["amount"]
                print(f"The total is {total}")
                while True:
                    cont = False
                    cash = input("Money given: ")
                    try:
                        cash = float(cash)
                    except:
                        print("Invalid amount!")
                        f.pause()
                        cont = True
                        break
                    if cash < total:
                        print("Paid money not enough!")
                        f.pause()
                        cont = True
                        break
                    print(f"The change is {cash - total}")
                    return
                if cont:
                    continue
            elif action.lower() == "x":
                return
            try:
                action = int(action)
                if action <= 1000:
                    code = input()
                    if code <= 1000:
                        print("This is not a valid item code!")
                        f.pause()
                        continue
                    code = str(code)
                    if code in stocktable:
                        for item in cart:
                            if item["code"] == code:
                                cart[cart.index(item)]["amount"] += action
                                continue
                        cart.append({"code": str(code), "amount": action})
                    else:
                        print("There is no item in the stocktable with this code!")
                        f.pause()
                else:
                    if action in stocktable:
                        for item in cart:
                            if item["code"] == code:
                                cart[cart.index(item)]["amount"] += 1
                                continue
                        cart.append({"code": str(action), "amount": 1})
                    else:
                        print("There is no item in the stocktable with this code!")
                        f.pause()
            except:
                print("Not a valid value!")
                f.pause()
    def stock(stocktable: dict, cn: str, accname: str) -> dict:
        while True:
            f.clear()
            print(f.read(cn + "/data")["name"])
            if accname != "":
                print(accname)
            print("------------------------------------------")
            print("Item no.   Stock  Price  Name")
            print("------------------------------------------")
            for itemno, itemdesc in stocktable:
                print(f"{itemno}  {itemdesc['stock']} {' ' * (5 - len(list(itemdesc['stock'])))} {itemdesc['price']} {' ' * (5 - len(list(itemdesc['price'])))} {itemdesc['name']}")
            print("------------------------------------------")
            print("1. Modify stock\n2. New item\n3. Modify item\n4. Remove item\n5. Exit stocktable")
            choice = input("Enter an action's number to take: ")
            try:
                choice = int(choice)
                if choice == 1:
                    return stock.stockmod(cn, stocktable)
                elif choice == 2:
                    return stock.create(cn, stocktable)
                elif choice == 3:
                    return stock.modify(cn, stocktable, accname)
                elif choice == 4:
                    return stock.remove(cn, stocktable)
                elif choice == 5:
                    return stocktable
                else:
                    raise ValueError
            except:
                print("Not an available choice")
                f.pause()

def cashier(cn: str) -> None:
    while True:
        f.clear()
        data = f.read(cn + "/data")
        if data["acc"]:
            print(data["name"])
            print("------------------------------------------")
            for accno in range(len(data["accs"])):
                print(f"{accno + 1}. {f.read(cn + "/accs/" + data["accs"][accno])["name"]}")
            print("------------------------------------------")
            print(f"{accno + 2}. Manage Accounts\n{accno + 3}. Exit Register")
            choice = input("Enter an action's number to take: ")
            try:
                choice = int(choice)
                if choice == accno + 2:
                    if getpass("Password: ") == data["pw"]:
                        while True:
                            f.clear()
                            print(data["name"])
                            print("------------------------------------------")
                            print("1. Create an Account\n2. Delete an Account\n3. Cancel")
                            choice = input("Enter an action's number to take: ")
                            try:
                                choice = int(choice)
                                if choice == 1:
                                    acc.create(cn)
                                    break
                                elif choice == 2:
                                    acc.remove(cn)
                                    break
                                elif choice == 3:
                                    break
                                else:
                                    raise ValueError
                            except:
                                print("Not an available choice!")
                                f.pause()
                elif choice == accno + 3:
                    return
                elif choice > 0 and choice < accno + 2:
                    while True:
                        f.clear()
                        print(data["name"])
                        print(f.read(cn + "/accs/" + data["accs"][choice - 1])["name"])
                        print("------------------------------------------")
                        print("1. Make a Sale\n2. Check the Stocktable\n3. Exit the Account")
                        secchoice = input("Enter an action's number to take: ")
                        try:
                            secchoice = int(secchoice)
                            if secchoice == 1:
                                act.sell(f.read(cn + "/accs/" + data["accs"][choice - 1])["stock"], data["name"], f.read(cn + "/accs/" + data["accs"][choice - 1])["name"])
                            elif secchoice == 2:
                                f.write(cn + "/accs/" + data["accs"][choice - 1], {"name": f.read(cn + "/accs/" + data["accs"][choice - 1])["name"], "stock": act.stock(f.read(cn + "/accs/" + data["accs"][choice - 1])["stock"], cn, f.read(cn + "/accs/" + data["accs"][choice - 1])["name"])})
                            elif secchoice == 3:
                                break
                            else:
                                raise ValueError
                        except:
                            print("Not an available choice!")
                            f.pause()
            except:
                print("Not an available choice!")
                f.pause()
        else:
            print(data["name"])
            print("------------------------------------------")
            print("1. Make a Sale\n2. Check the Stocktable\n3. Exit the Register")
            choice = input("Enter an action's number to take: ")
            try:
                choice = int(choice)
                if choice == 1:
                    act.sell(f.read(cn + "/main"), data["name"], "")
                elif choice == 2:
                    f.write(cn + "/main", act.stock(f.read(cn + "/main"), cn, ""))
                elif choice == 3:
                    return
                else:
                    raise ValueError
            except:
                print("Not an available choice!")
                f.pause()
