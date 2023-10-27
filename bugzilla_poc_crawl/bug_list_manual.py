from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import re
import os
import json

bug_list_path = "bugzillapoc"
os.makedirs(bug_list_path, exist_ok=True)

bug_list = []

def store_bug_list(pageSource):
    soup = BeautifulSoup(pageSource, 'html.parser')
    bug_table = soup.find("tbody")
    for bug_row in bug_table.contents:
        try:
            bug_info = {}
            bug_link = bug_row.find('a', class_='bz_bug_link')
            bug_info['id'] = bug_link.get('href').split('=')[-1]
            summary_element = bug_row.find('td', class_='bz_summary_column')
            bug_info['summary'] = summary_element.text
            cve_pattern = r'CVE-\d{4}-\d{4}'
            bug_info['cve_id'] = re.findall(cve_pattern, bug_info['summary'])
            bug_list.append(bug_info)
        except:
            pass 


def search():
    directory_path = "bugzillalist"
    for i in range(1,61):
        file_path = os.path.join(directory_path, 'Bug List' + str(i) + '.html')
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            store_bug_list(html_content)
            
            


if __name__ == '__main__':
    search()
    with open("bug_list_cve_summary.json", "w") as json_file:
        json_data = json.dumps(bug_list, indent=4)
        json_file.write(json_data)