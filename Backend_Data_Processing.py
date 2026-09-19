# Raw user records: (User ID, Name, Role, Is_Active, Login_Attempts)
users = [
    (101, "Alice", "admin", True, 1),
    (102, "Bob", "member", True, 4),
    (103, "Charlie", "editor", False, 0),
    (104, "Diana", "admin", False, 6),
    (105, "Evan", "member", True, 2),
    (106, "Fiona", "guest", True, 0),
]

# c. Summary Counters
active_granted_count = 0
inactive_count = 0
security_alert_count = 0

print("PROCESSING USER AUDIT...")
print("----------------------------------------")

# a. Processing User Records
for user in users:
    user_id, name, role, is_active, login_attempts = user

    # Security Audit Check (Login_Attempts >= 5)
    if login_attempts >= 5:
        print(f"[ALERT] Account {name} is LOCKED due to excessive failed logins ({login_attempts} attempts).")
        security_alert_count += 1

    # Access Rights Evaluation
    if not is_active:
        print(f"[DENIED] Account {name} is inactive.")
        inactive_count += 1
    elif role == "admin":
        print(f"[GRANT] Full system access granted to {name} (ID: {user_id})")
        active_granted_count += 1
    elif role in ["member", "editor"]:
        print(f"[GRANT] Standard access granted to {name} (ID: {user_id})")
        active_granted_count += 1
    else:
        # Optional: Handle guest or other roles if active
        print(f"[INFO] Limited access granted to {name} (ID: {user_id})")
        active_granted_count += 1

# c. Summary Report
print("\nAUDIT SUMMARY REPORT")
print("========================================")
print(f"Total Active Users Granted: {active_granted_count}")
print(f"Total Inactive Accounts:    {inactive_count}")
print(f"Total Security Alerts:      {security_alert_count}")
print("========================================")