from datetime import datetime
import requests
from dotenv import load_dotenv
import os
import time


load_dotenv()
TOKEN = os.environ.get('TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

CWD = os.path.dirname(os.path.abspath(__file__))

def send_message(message):

    url_message = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    response = requests.get(url_message).json()
    return response


print(CWD)

ip = requests.get("https://api.ipify.org").text
print(f"My public IP address is: {ip}")



f = open(f"{CWD}/data/ip.txt", "r")
old_ip = f.read()

if ip == old_ip:
    print("Your IP did not change")
    # send_message("Your IP did not change")
else:
    print("Your IP changed !!!")

    # save old IP for analysis
    today = datetime.strftime(datetime.today(),"%Y-%m-%d")
    f = open(f"{CWD}/data/ip_{today}.txt", "w")
    f.write(old_ip)
    f.close()

    # save new ip
    f = open(f"{CWD}/data/ip.txt", "w")
    f.write(ip)
    f.close()

    send_message("Your IP changed!!! New IP:")
    send_message(ip)


