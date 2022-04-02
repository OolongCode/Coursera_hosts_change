from __future__ import print_function
import ctypes, sys, os
from bs4 import BeautifulSoup
import requests
import re

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


url = "https://ping.eu/action.php?atype=3"
post_data = {'host':'d3c33hcgiwev3.cloudfront.net','go':'Go'}

php_raw = requests.post(url, data=post_data)
soup = BeautifulSoup(php_raw.content,'lxml')

re_pattern = re.compile(r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*')

sc_1 = soup.select('head script')[6].string
sc_2 = soup.select('head script')[7].string
sc_3 = soup.select('head script')[8].string
sc_4 = soup.select('head script')[9].string

sc_data = [sc_1,sc_2,sc_3,sc_4]
file_data = ""
for text in sc_data:
    text = re_pattern.search(text).group()
    file_data += text +' d3c33hcgiwev3.cloudfront.net'+ '\n'

file_raw_data = ''
# with open("coursera_host.txt",'r+') as f:
#     for line in f.readlines():
#         file_raw_data += line

if is_admin():
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts",'r+', encoding='utf-8') as admin_file:
        for line in admin_file.readlines():
            if 'd3c33hcgiwev3.cloudfront.net' not in line:
                file_raw_data += line
        file_raw_data += file_data
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts",'w', encoding='utf-8') as admin_file:
        admin_file.write("\n")
        admin_file.writelines(file_raw_data)

elif sys.version_info[0] == 3:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
else:
    ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
