names = ["walter", "white"]
phones = ["696969", "787878"]
emails = ["walter.junior@white.com", "white.walter@junior.com"]

def choice():
    choose = int(input("What do u want to do?\n1. Look entries\n2. Add entries\n3. Remove entries\n>>> "))
    if choose == 1:
        look_up_entries()
    elif choose == 2:
        add_entries()
    elif choose == 3:
        remove_entries()
    else:
        print("Wrong number")
def look_up_entries(is_removing = False):
    for i in range(0, len(names)):
        print(f"{i + 1}. name: {names[i]} phone: {phones[i]} email: {emails[i]}")
    if not is_removing:
        choice()
def add_entries():
    names.append(input("What's your name?\n>>> "))
    phones.append(input("What's your phone number?\n>>> "))
    emails.append(input("What's your email?\n>>> "))
    choice()
def remove_entries():
    look_up_entries(True)
    entry_to_remove = int(input("Which entry do you want to remove?\n>>> "))
    del names[entry_to_remove - 1]
    del phones[entry_to_remove - 1]
    del emails[entry_to_remove - 1]
    choice()
choice()

#TODO simplify code and add csv saving