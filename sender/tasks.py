import requests
import time
import random
import threading

RECEIVER_URL = "https://receiver-service-8nwe.onrender.com/"

def send_random_requests():
    while True:
        wait_time = random.randint(60, 120)  # 5–10 minutes
        print(f"⏳ Waiting {wait_time} seconds...")

        time.sleep(wait_time)

        payload = {
            "service": "sender_service",
            "event": "heartbeat",
            "interval": wait_time
        }

        try:
            response = requests.post(RECEIVER_URL, json=payload, timeout=60)
            print("✅ Sent:", response.status_code)
        except Exception as e:
            print("❌ Error sending request:", e)


def start_background_task():
    thread = threading.Thread(target=send_random_requests, daemon=True)
    thread.start()
