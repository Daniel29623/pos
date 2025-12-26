from src import functions as f
from src.registers import reg as r
from src.cashier import cashier

while True:
    registers = f.read("registers")["registers"]
    f.clear()
    print("Codename    Register Name")
    print("------------------------------------------")
    for reg in registers:
        print(f"{reg} {' ' * (10 - len(reg))} {f.read(reg + "/data")["name"]}")
    print("------------------------------------------")
    print("1. Enter\n2. Create\n3. Modify\n4. Remove\n5. Exit")
    choice = input("Enter an action's number to take: ")
    try:
        choice = int(choice)
        if choice == 1:
            cn = input("Codename: ")
            if cn in registers:
                cashier(cn)
            else:
                print("There is no register with this codename!")
                f.pause()
        elif choice == 2:
            r.create()
        elif choice == 3:
            r.modify()
        elif choice == 4:
            r.remove()
        elif choice == 5:
            break
        else:
            raise ValueError
    except:
        print("Not an available choice!")
        f.pause()
