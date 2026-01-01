import requests
import time
import random
import threading

RECEIVER_URL2 = "http://127.0.0.1:8000/api/receive/"
RECEIVER_URL = "https://expo-t2be.onrender.com/"

def send_random_requests():
    while True:
        wait_time = random.randint(300, 400)  # 5–10 minutes
        print(f"⏳ Waiting {wait_time} seconds...")

        time.sleep(wait_time)

        payload = {
            "service": "sender_service",
            "event": "heartbeat",
            "interval": wait_time
        }

        try:
            response = requests.post(RECEIVER_URL, json=payload, timeout=2)
            response = requests.post(RECEIVER_URL2, json=payload, timeout=2)
            print("✅ Sent:", response.status_code)
        except Exception as e:
            print("❌ Error sending request:", e)


def start_background_task():
    thread = threading.Thread(target=send_random_requests, daemon=True)
    thread.start()
