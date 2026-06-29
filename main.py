from endpoint import get_cpu, get_ram, get_disk, get_processes
from agent import choose_action
from logger import log_event
from analyzer import analyze_log
from detector import (
    detect_cpu_threat,
    detect_ram_threat,
    detect_disk_threat,
    detect_suspicious_process
)
print("=" * 50)
print("        Welcome to AgentShield AI")
print("=" * 50)

action = choose_action()
log_event("AI chose action: " + action)
print()
print("AI Agent decided to inspect:", action)
print()

if action == "cpu":

    cpu = get_cpu()
    print("Endpoint Report")
    print("-" * 16)

    print("CPU Usage:", cpu, "%")
    print()
    print("Threat Analysis")
    print("-" * 16)
    detect_cpu_threat(cpu)
elif action == "ram":

    ram = get_ram()
    print("Endpoint Report")
    print("-" * 16)
    print("RAM Usage:", ram, "%")
    print()
    print("Threat Analysis")
    print("-" * 16)
    detect_ram_threat(ram)

elif action == "disk":
    disk = get_disk()
    print("Endpoint Report")
    print("-" * 16)
    print("Disk Usage:", get_disk(), "%")
    print()
    print("Threat Analysis")
    print("-" * 16)
    detect_disk_threat(disk)

elif action == "processes":

    processes = get_processes()
    print("Endpoint Report")
    print("-" * 16)
    print("Processes:")

    for process in processes:
        print("-", process)
    print()
    print("Threat Analysis")
    print("-" * 16)

    detect_suspicious_process(processes)
print()
print("=" * 50)
analyze_log()
    