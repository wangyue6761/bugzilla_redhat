import requests
import json
from time import sleep
from bs4 import BeautifulSoup
import os

url = 'https://bugzilla-attachments.redhat.com/attachment.cgi?id=602307'
headers = {
    'Cookie':'cxlang = en;__gads = ID = 36484b9e05609ded - 22908ea615e400f6: T = 1695644877:RT = 1695644877:S = ALNI_MaiHciOEJMqknVvFPiZzk_tT4wZsw;__gpi = UID = 00000c53f4ce89a4: T = 1695644877:RT = 1695644877:S = ALNI_MZMEdvVz5ZFPMHNI_7T_P0TxPiMEQ',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
html = requests.get(url, headers).content.decode("ISO-8859-1")

with open("attachment.txt", 'w') as file:
    file.write(html