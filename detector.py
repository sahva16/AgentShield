from logger import log_event

def detect_cpu_threat(cpu):
    if cpu > 80:
        print("⚠ ALERT: High CPU Usage Detected")
        print("Severity: MEDIUM")
        log_event("ALERT: High CPU Usage Detected")
    else:
        print("✅ No threats detected.")

def detect_ram_threat(ram):
    if ram > 85:
        print("⚠ ALERT: High RAM Usage Detected")
        print("Severity: MEDIUM")
        log_event("ALERT: High RAM Usage Detected")
    else:
        print("✅ No threats detected.")

def detect_disk_threat(disk):
    if disk > 90:
        print("⚠ ALERT: High Disk Usage Detected")
        print("Severity: HIGH")
        log_event("ALERT: High Disk Usage Detected")
    else:
        print("✅ No threats detected.")

def detect_suspicious_process(processes):

    found = False

    for process in processes:

        if process == "malware.exe":

            found = True

            print("⚠ ALERT: Suspicious Process Detected")
            print("Severity: CRITICAL")

            log_event("ALERT: Suspicious Process Detected")

    if not found:
        print("✅ No threats detected.")