import os, httpx

NOTIF_URL = os.getenv("NOTIFICATION_SERVICE_URL")

def send_mail(to: str, message: str):
    if not NOTIF_URL:
        print("[notification] URL not set, skipping send")
        return
    try:
        httpx.post(NOTIF_URL, json={"to": to, "message": message}, timeout=5)
    except Exception as e:
        print("[notification] error:", e)
