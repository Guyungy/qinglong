import requests
from datetime import datetime
import time

def fetch_bilibili_data(vmid, account_name):
    url = f"https://api.bilibili.com/x/relation/stat?vmid={vmid}&jsonp=jsonp"
    
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            followers = data['data']['follower']
            today = datetime.now().strftime("%Y-%m-%d")
            message = f"{today} {account_name}的哔哩哔哩粉丝数量：{followers}"
            print(message)
            send_notification_to_feishu(message)
            break
        else:
            print(f"Failed to fetch data for {account_name}. Retrying in 1 second...")
            time.sleep(1)

def send_notification_to_feishu(message):
    webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/*"
    payload = {
        "msg_type": "text",
        "content": {"text": message}
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("Notification sent successfully")
    else:
        print("Failed to send notification")

# 调用函数获取两个账户的数据
fetch_bilibili_data("哔哩哔哩UID1", "哔哩哔哩名字1")
fetch_bilibili_data("哔哩哔哩UID2", "哔哩哔哩名字12")
