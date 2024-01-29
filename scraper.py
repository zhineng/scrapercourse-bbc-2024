
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

urls = soup.find_all('a',{'class':'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})
tag_list = []

for url in urls:
    sub_response = requests.get(url.get('href'))
    sub_soup = BeautifulSoup(sub_response.text,'lxml')
    tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e2o6ii40'})
    for tag in tags:
        tag_list.append(tag.getText())

print(tag_list)


