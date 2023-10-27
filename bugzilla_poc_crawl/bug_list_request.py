import requests
import json
from time import sleep
from bs4 import BeautifulSoup

url = "https://bugzilla.redhat.com/buglist.cgi?bug_status=VERIFIED&bug_status=CLOSED&columnlist=product%2Ccomponent%2Cassigned_to%2Cstatus%2Csummary%2Clast_change_time%2Cseverity%2Cpriority&order=priority%2C%20severity%2C%20&query_format=advanced&short_desc=CVE&short_desc_type=allwordssubstr"

# //*[@id="bz_buglist"]/tbody
headers = {
    'Cookie':'cxlang = en;__gads = ID = 36484b9e05609ded - 22908ea615e400f6: T = 1695644877:RT = 1695644877:S = ALNI_MaiHciOEJMqknVvFPiZzk_tT4wZsw;__gpi = UID = 00000c53f4ce89a4: T = 1695644877:RT = 1695644877:S = ALNI_MZMEdvVz5ZFPMHNI_7T_P0TxPiMEQ',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
html = requests.get(url, headers).content.decode("utf8")
soup = BeautifulSoup(html, 'html.parser')
bug_sheet = soup.find("tbody")
# print(bug_sheet.contents)
with open("bug.html", "w") as file:
    file.write(soup.prettify())