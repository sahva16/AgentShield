def log_event(message):
    with open("activity.log", "a") as file:
        file.write(message + "\n")
