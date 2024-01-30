
import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

try:
    response = requests.get('https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt', headers=headers,timeout=5)
    response.encoding ='utf-8'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'lxml')
        soup.encode('utf-8')
        titles= soup.find_all('a',{'class':'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})

        if titles:
            title_list = []
            for title in titles:
                title_list.append(title.getText())
            print(title_list)
        else:
            print(f"Element not find!!")
    else:
        print(f'This webstite not accessable!!')
except Exception as e:
    print(str(e))