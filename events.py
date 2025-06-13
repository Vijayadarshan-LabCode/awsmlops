import json
import random
import time
from datetime import datetime
 
event_types = ["ALERT", "DEPLOYMENT", "SCALE", "RECOVERY"]
 
def generate_event():
    event = {
        "timestamp": datetime.now().isoformat(),
        "type": random.choice(event_types),
        "service": random.choice(["auth-service", "checkout-service", "payment-service"]),
        "message": "",
        "severity": ""
    }
 
    if event["type"] == "ALERT":
        event["message"] = "High CPU usage detected"
        event["severity"] = "CRITICAL"
    elif event["type"] == "DEPLOYMENT":
        event["message"] = "Deployed version 2.3.1 to production"
        event["severity"] = "INFO"
    elif event["type"] == "SCALE":
        event["message"] = "Scaled checkout-service from 2 to 4 pods"
        event["severity"] = "INFO"
    elif event["type"] == "RECOVERY":
        event["message"] = "Service recovered after restart"
        event["severity"] = "NORMAL"
 
    return event
 
# Generate event logs as JSON
for _ in range(5):
    print(json.dumps(generate_event(), indent=2))
    time.sleep(2)