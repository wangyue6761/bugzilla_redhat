import json
import os

pocpath = "bugzillapoc"
cve_num = 0
cve_attachment = 0

for root, dirs, files in os.walk(pocpath):
    for dir in dirs:
        if 'CVE' in dir:
            cve_num += 1
            for sub_root, sub_dirs, sub_files in os.walk(os.path.join(pocpath,dir)):
                if len(sub_files) > 1:
                    cve_attachment += 1

print(cve_num)
print(cve_attachment)
