from fileinput import filename
import imp
from turtle import delay
from unittest import result
import requests  # get content from page
from bs4 import BeautifulSoup  # web scraping

import re  # Regular Expression pattern matching

# from urllib.request import urlretrieve #downloading mp4
import sys  # for argument parsing
# Exception Handling
print('Please input link TED you want download: ')
link_dowload = input()
sys.argv.append(link_dowload)
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")
#url = 'https://www.ted.com/talks/lucas_joppa_how_to_fix_the_bugs_in_the_net_zero_code'
r = requests.get(url)
print("Download about to start")
soup = BeautifulSoup(r.content,'lxml')

for val in soup.find_all("script"):
    if(re.search("file", str(val))) is not None:
        result = str(val)
result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result)
if result_mp4:
    mp4_url=result_mp4.group(0)
else:
    print('No found link dowload')
    exit()

print("Downloading video from ..." + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ..."+file_name)
r = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(r.content)

# Alternate method
#urletrieve(mp4_url, file_name)
print("Download Process finished!")
delay(1000)