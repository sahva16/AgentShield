import random

def get_cpu():
    return random.randint(1,100)

def get_ram():
    return random.randint(1,100)

def get_disk():
    return random.randint(1,100)


def get_processes():
    return [
        "chrome.exe",
        "python.exe",
        "spotify.exe",
        "malware.exe"
    ]
