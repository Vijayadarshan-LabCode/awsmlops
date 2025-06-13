import psutil
import random
import csv
from datetime import datetime, timedelta
 
# Create CSV file to store metrics
with open('metrics365.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'cpu_percent', 'memory_percent'])
 
    # Simulate one metric entry per day for the past 365 days
    for day_offset in range(365):
        # Random time during that day
        timestamp = (datetime.now() - timedelta(days=day_offset, hours=random.randint(0, 23), minutes=random.randint(0, 59))).isoformat()
 
        # Simulated (not real-time) CPU and memory usage to mimic historical values
        cpu = round(random.uniform(5, 95), 2)  # Simulate CPU usage between 5% and 95%
        memory = round(random.uniform(20, 90), 2)  # Simulate memory usage between 20% and 90%
 
        writer.writerow([timestamp, cpu, memory])
        print(f"[{timestamp}] CPU: {cpu}%, Memory: {memory}%")