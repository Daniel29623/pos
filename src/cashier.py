from src import functions as f

class act:
    def sell(stocktable: dict, accname: str):
        cart = []
        while True:
            f.clear()
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
            if action.lower() == "x":
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

    def stock(stocktable: dict, accname: str):
        while True:
            f.clear()
            if accname != "":
                print(accname)
                print("------------------------------------------")
            print("Item no.   Stock  Price  Name")
            print("------------------------------------------")
            for itemno, itemdesc in stocktable:
                print(f"{itemno}  {itemdesc["stock"]} {' ' * (5 - len(list(itemdesc["stock"])))} {itemdesc["price"]} {' ' * (5 - len(list(itemdesc["price"])))} {itemdesc["name"]}")
            print("------------------------------------------")
            print("1. New item\n2. Modify item\n3. Remove item\n4. Exit stocktable")
            choice = input("Enter an action's number to take: ")
            try:
                choice = int(choice)
                if choice == 1:
                    pass
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    return
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
            pass
        else:
            stock = f.read(cn + "/main")
            print(data["name"])
            print("------------------------------------------")
            print("1. Make a Sale\n2. Check the Stock Table\n3. Exit the Register")
            print("------------------------------------------")
            choice = input("Enter an action's number to take: ")
            try:
                choice = int(choice)
                if choice == 1:
                    act.sell(stock, "")
                elif choice == 2:
                    act.stock(stock, "")
                elif choice == 3:
                    return
                else:
                    raise ValueError
                break
            except:
                print("Not an available choice!")
                f.pause()
