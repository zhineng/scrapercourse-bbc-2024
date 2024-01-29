
import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt')
response.encoding ='utf-8'
soup = BeautifulSoup(response.text,'lxml')
soup.encode('utf-8')
titles= soup.find_all('a',{'class':'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})

title_list = []
for title in titles:
    title_list.append(title.getText())

print(title_list)

