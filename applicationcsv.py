import csv
import random
from datetime import datetime, timedelta
 
# Sample log levels and messages
log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
messages = [
    "User updated payment method",
    "Login failed due to invalid credentials",
    "Service timeout error",
    "User profile updated",
    "Database connection established",
    "Security token expired",
    "Password changed",
    "Access granted to secure endpoint",
    "Account suspended due to suspicious activity"
]
 
# Open the CSV file and write the header
with open('logs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "level", "message"])
 
    # Generate one log per day for the past 365 days
    for day_offset in range(365):
        log_time = datetime.now() - timedelta(days=day_offset, hours=random.randint(0, 23), minutes=random.randint(0, 59))
        log_level = random.choice(log_levels)
        message = random.choice(messages)
        writer.writerow([log_time.isoformat(), log_level, message])