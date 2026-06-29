def analyze_log():
    cpu_count = 0
    ram_count = 0
    disk_count = 0
    process_count = 0
    alert_count = 0
    cpu_alerts = 0
    ram_alerts = 0
    disk_alerts = 0
    process_alerts = 0
    with open("activity.log", "r") as file:
     for line in file:

        if "ALERT" in line:
            alert_count += 1

        if "cpu" in line:
            cpu_count += 1

        elif "ram" in line:
            ram_count += 1

        elif "disk" in line:
            disk_count += 1

        elif "processes" in line:
            process_count += 1
        if "High CPU Usage" in line:
           cpu_alerts += 1

        if "High RAM Usage" in line:
          ram_alerts += 1

        if "High Disk Usage" in line:
          disk_alerts += 1
        if "Suspicious Process" in line:
         process_alerts += 1
    print("\n=== AgentShield Analytics ===")
    print("CPU Checks:", cpu_count)
    print("RAM Checks:", ram_count)
    print("Disk Checks:", disk_count)
    print("Process Checks:", process_count)
    print()
    print("CPU Alerts:", cpu_alerts) 
    print("RAM Alerts:", ram_alerts)
    print("Disk Alerts:", disk_alerts)
    print("Process Alerts:", process_alerts)
    print()
    print("Security Alerts:", alert_count)
    risk_score = (
    cpu_alerts * 2 +
    ram_alerts * 2 +
    disk_alerts * 3 +
    process_alerts * 5
)
    print()
    print("Risk Score:", risk_score)

    if risk_score >= 20:
              print("Risk Level: HIGH")

    elif risk_score >= 10:
              print("Risk Level: MEDIUM")

    else:
             print("Risk Level: LOW")
    print()
    total = cpu_count + ram_count + disk_count + process_count

    if cpu_count > total / 2:
        print("Behavior Score: HIGH")
    else:
        print("Behavior Score: NORMAL")