from src import functions as f
from src.registers import reg as r

while True:
    f.clear()
    registers = f.read("registers")["registers"]
    print("Codename    Register Name")
    print("------------------------------------------")
    for reg in registers:
        print(f"{reg}{' ' * (10 - len(reg))}  {f.read(reg + "/data")["name"]}")
    print("------------------------------------------")
    print("1. Enter\n2. Create\n3. Modify\n4. Remove\n5. Exit")
    while True:
        choice = input("Enter an action's number to take: ")
        try:
            choice = int(choice)
            break
        except:
            print("Not an available choice!")
            f.pause()
    if choice == 1:
        pass
    elif choice == 2:
        r.create()
    elif choice == 3:
        r.modify()
    elif choice == 4:
        r.remove()
    elif choice == 5:
        exit()
    else:
        print("Not an available choice!")
        f.pause()
