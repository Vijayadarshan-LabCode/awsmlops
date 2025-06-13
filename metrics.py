from prometheus_client import start_http_server, Gauge
import random
import time
 
# Define sample metrics
cpu_usage = Gauge('cpu_usage_percent', 'Simulated CPU usage')
api_latency = Gauge('api_latency_ms', 'Simulated API Latency')
 
def update_metrics():
    while True:
        cpu_usage.set(random.uniform(20, 95))
        api_latency.set(random.uniform(100, 900))
        time.sleep(5)
 
if __name__ == "__main__":
    start_http_server(8000)  # Prometheus can scrape from this
    print("Metrics server running on http://localhost:8000")
    update_metrics()