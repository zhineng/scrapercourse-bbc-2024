
import sys,time
sys.stdout.reconfigure(encoding='utf-8')
import gevent
from gevent import monkey
monkey.patch_all()
import requests,grequests
from bs4 import BeautifulSoup

start_time = time.time()
links = [f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt/page/{page}' for page in range(1,4)]
reqs = (grequests.get(link) for link in links)
resps = grequests.imap(reqs,grequests.Pool(3))
for index,resp in enumerate(resps):
    #response = requests.get(f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt/page/{page}')
    #response.encoding ='utf-8'
    soup = BeautifulSoup(resp.text,'lxml')
    soup.encode('utf-8')
    titles= soup.find_all('a',{'class':'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})

    title_list = []
    for title in titles:
        title_list.append(title.getText())

    urls = soup.find_all('a',{'class':'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})

    sub_links = [url.get('href') for url in urls]
    sub_reqs = (grequests.get(sub_link) for sub_link in sub_links)
    sub_resps = grequests.imap(sub_reqs,grequests.Pool(10))

    tag_list = []

    for sub_resp in sub_resps:
        #sub_response = requests.get(url.get('href'))
        sub_soup = BeautifulSoup(sub_resp.text,'lxml')
        tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e2o6ii40'})
        for tag in tags:
            tag_list.append(tag.getText())

    print(f"This is Page {index + 1}")
    print(title_list)
    print(tag_list)

end_time = time.time()
print(f"Total time {end_time - start_time} second")
