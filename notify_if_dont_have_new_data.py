import requests
import time
from datetime import datetime
import urllib

def try_to_access_host():
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return True
    except:
        return False

def ck_bot_notify(mess):
    try:
        bot_noti_url = "https://api.telegram.org/bot0000000000:XXXXXXXXXXXX/sendMessage?chat_id=-0000000000&text="
        requests.get(bot_noti_url + urllib.parse.quote(mess))
        return True
    except:
        return False

def notify_when_something_wrong(timedone_stamp):
    if not try_to_access_host():
        ck_bot_notify("Hosting is Down, please check!")
    if time.time() - timedone_stamp > 600:
        ck_bot_notify("Last data not found !")

url = "http://127.0.0.1/timedone.html"
timedone_stamp = float(requests.get(url).text)

notify_when_something_wrong(timedone_stamp)



