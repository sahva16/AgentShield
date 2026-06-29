import random

def choose_action():
    actions = [
        "cpu",
        "ram",
        "disk",
        "processes"
    ]

    return random.choice(actions)
for i in range(10):
    print(choose_action())
