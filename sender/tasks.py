import requests
import time
import random
import threading

RECEIVER_URL2 = "https://receiver-service-8nwe.onrender.com/api/receive/"
RECEIVER_URL = "https://expo-t2be.onrender.com/"
RECEIVER_URL3 = "https://web-modules-chpw.onrender.com"

def send_random_requests():
    while True:
        wait_time = random.randint(120, 180) 
        print(f"⏳ Waiting {wait_time} seconds...")

        time.sleep(wait_time)

        payload = {
            "service": "sender_service",
            "event": "heartbeat",
            "interval": wait_time
        }

        try:
            response = requests.post(RECEIVER_URL, json=payload, timeout=60)
            response = requests.post(RECEIVER_URL2, json=payload, timeout=60)
            response = requests.post(RECEIVER_URL3, json=payload, timeout=60)
            print("✅ Sent:", response.status_code)
        except Exception as e:
            print("❌ Error sending request:", e)


def start_background_task():
    thread = threading.Thread(target=send_random_requests, daemon=True)
    thread.start()
