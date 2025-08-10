choice = int(input("What do you want to do? \n1. addition\n2. subtraction\n3. multiplication\n4. division\n>>> "))
match choice:
    case 1:
        a = int(input("Type first number: "))
        b = int(input("Type second number: "))
        print(f"{a} + {b} = {a + b}")
    case 2:
        a = int(input("Type first number: "))
        b = int(input("Type second number: "))
        print(f"{a} - {b} = {a - b}")
    case 3:
        a = int(input("Type first number: "))
        b = int(input("Type second number: "))
        print(f"{a} * {b} = {a * b}")
    case 4:
        a = int(input("Type first number: "))
        b = int(input("Type second number: "))
        print(f"{a} / {b} = {a / b}")
    case _:
        print("You typed wrong")