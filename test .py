# test-.py
import requests  BOT_TOKEN = "8780870508:AAFpnmTHQXHp_xKTCrNCMhMBPW9C3xkQ0Kc" CHAT_ID = "455096723"  url = f"https://api.telegram.org/bot{8780870508:AAFpnmTHQXHp_xKTCrNCMhMBPW9C3xkQ0Kc}/sendMessage" data = {"chat_id": 455096723, "text": "Test Telegram OK ✅"}  requests.post(url, data=data)
