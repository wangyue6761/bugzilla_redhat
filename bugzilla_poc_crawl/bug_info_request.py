import requests
import json
from time import sleep
from bs4 import BeautifulSoup
import os
import re

poc_path = "bugzillapoc"
os.makedirs(poc_path, exist_ok=True)

def download_attachment(attachment_list, dirname):
    for attchment_link in attachment_list:
        url = attchment_link
        attachment_id =  re.search(r'id=(\d+)', url).group(1)
        headers = {
            'Cookie':'cxlang = en;__gads = ID = 36484b9e05609ded - 22908ea615e400f6: T = 1695644877:RT = 1695644877:S = ALNI_MaiHciOEJMqknVvFPiZzk_tT4wZsw;__gpi = UID = 00000c53f4ce89a4: T = 1695644877:RT = 1695644877:S = ALNI_MZMEdvVz5ZFPMHNI_7T_P0TxPiMEQ',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        try:
            data = requests.get(url, headers).content.decode("utf8")
        except:
            data = requests.get(url, headers).content.decode("ISO-8859-1")
        with open(os.path.join(poc_path, dirname, "attachment" + attachment_id + '.txt'), 'w') as file:
            file.write(data)

def bug_crawler(bugrow):
    url = 'https://bugzilla.redhat.com/show_bug.cgi?id=' + bugrow['id']   # https://bugzilla.redhat.com/show_bug.cgi?id=617578
    # url = 'https://bugzilla.redhat.com/show_bug.cgi?id=601901'  # 比较好的样例
    headers = {
    'Cookie':'cxlang = en;__gads = ID = 36484b9e05609ded - 22908ea615e400f6: T = 1695644877:RT = 1695644877:S = ALNI_MaiHciOEJMqknVvFPiZzk_tT4wZsw;__gpi = UID = 00000c53f4ce89a4: T = 1695644877:RT = 1695644877:S = ALNI_MZMEdvVz5ZFPMHNI_7T_P0TxPiMEQ',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    html = requests.get(url, headers).content.decode("utf8")
    soup = BeautifulSoup(html, 'html.parser')

    # bug info
    table = soup.find('table', class_="edit_form")
    bug_info_dict = {}
    bug_info_dict['bugid'] = bug_row['id']
    bug_info_dict['cveid'] = bug_row['cve_id']
    bug_info_dict['summary'] = bug_row['summary']
    bug_info_dict['alias'] = table.find('th', id='field_label_alias').next_sibling.next_sibling.get_text(strip=True)
    bug_info_dict['product'] = table.find('td', id='field_container_product').get_text(strip=True)
    bug_info_dict['hardware'] = table.find('th', id="field_label_rep_platform").next_sibling.next_sibling.get_text(strip=True)
    bug_info_dict['os'] = table.find('th', id="field_label_op_sys").next_sibling.next_sibling.get_text(strip=True)
    try: 
        bug_info_dict['url'] = table.find('span', id="bz_url_input_area").a['href']
    except:
        bug_info_dict['url'] = ''
    bug_info_dict['reported_date'] = table.find('td', id='bz_show_bug_column_2').table.tr.td.get_text(strip=True)
    
    # attachment
    attachment_table = soup.find('table', id='attachment_table')
    attachment_list = []
    for attachment_row in attachment_table.contents:
        try:
            if attachment_row['class']== ['bz_contenttype_text_plain']:
                attachment_link = "https://bugzilla-attachments.redhat.com/" + attachment_row.find('a')['href']
                attachment_list.append(attachment_link)
        except:
            pass
    bug_info_dict['attachment'] = attachment_list

    # comment 也就是文本描述, 可以将第一条作为文本部分
    comment_list = []
    comment_table = soup.find('table', class_="bz_comment_table")
    for comment_row in comment_table.tr.td.contents:
        try:
            if comment_row['class'] == ['bz_comment', 'bz_first_comment'] or comment_row['class'] == ['bz_comment']:
                comment_list.append(comment_row.find('pre', class_="bz_comment_text").get_text(strip=True))
        except:
            pass
    bug_info_dict['comment'] = comment_list

    # 保存
    try:
        dirname = bug_info_dict['cveid'][0] + '_' + bug_info_dict['bugid']
    except:
        dirname = 'None_' + bug_info_dict['bugid']
    os.makedirs(os.path.join(poc_path, dirname), exist_ok=True)
    with open(os.path.join(poc_path, dirname, dirname + '.json'), 'w') as json_file:
        json_data = json.dumps(bug_info_dict, indent=4)
        json_file.write(json_data)
    
    # 下载附件
    download_attachment(attachment_list, dirname)

if __name__ == '__main__':
    with open("bug_list_cve_summary.json", 'r') as file:
        bug_list = json.load(file)
    bug_count = 0 
    bug_sum = len(bug_list)
    for bug_row in bug_list:
        if bug_count < 47642:   # 中断点
            bug_count += 1
            continue
        bug_crawler(bug_row)
        bug_count += 1
        print("进度：{}/{} bugID:{}".format(bug_count, bug_sum, bug_row['id']))  