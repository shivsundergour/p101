import random
min_value=1
max_value=6
roll_again = "y"
while roll_again == "y":
    print("Rolling the dices...")
    value1=random.randint(min_value, max_value)
    print(value1)
    if value1 == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if value1 == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if value1 == 3:
        print("[-----]")
        print("[   0 ]")
        print("[  0  ]")
        print("[ 0   ]")
        print("[-----]")
    if value1 == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if value1 == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if value1 == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
    roll_again = input("Press 'y' to roll the dices again or press 'n' to exit ")
print("Thank you")