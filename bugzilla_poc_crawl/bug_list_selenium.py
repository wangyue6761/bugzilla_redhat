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
        with open("bug_list_cve_summary1.json", "w") as json_file:
            json_data = json.dumps(bug_list, indent=4)
            json_file.write(json_data) 

def click_next_page(driver):
    try:
        # 使用WebDriverWait等待下一页按钮出现
        next_page_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Next')]"))
        )

        # 使用ActionChains模拟鼠标点击
        actions = ActionChains(driver)
        actions.click(next_page_button)
        actions.perform()
        time.sleep(3)
        return 1
    except Exception as e:
        print("无法点击下一页按钮:", str(e))
        return 0


def search():
    url = "https://bugzilla.redhat.com/buglist.cgi?bug_status=VERIFIED&bug_status=CLOSED&columnlist=product%2Ccomponent%2Cassigned_to%2Cstatus%2Csummary%2Clast_change_time%2Cseverity%2Cpriority&order=priority%2C%20severity%2C%20&query_format=advanced&short_desc=CVE&short_desc_type=allwordssubstr"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(15)
    page_num = 1
    flag = 1
    while(1):
        print(page_num)
        pageSource = driver.page_source
        store_bug_list(pageSource)
        flag = click_next_page(driver)
        page_num += 1
        if flag==0:
            break


if __name__ == '__main__':
    search()