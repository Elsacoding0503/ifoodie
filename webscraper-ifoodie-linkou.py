# ifoodie-Linkou
import requests
import time, random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import pandas as pd


ua = UserAgent()

headers = {
    'User-Agent': ua.random
}


res_name = []
res_rate = []
res_time = []
res_addr = []
res_tag = []

for i in range(1,17):
    url_ifoodie = f"https://ifoodie.tw/explore/%E6%96%B0%E5%8C%97%E5%B8%82/list/%E6%9E%97%E5%8F%A3%E5%8D%80?opening=true&sortby=popular&page={i}"
    response_ifoodie = requests.get(url=url_ifoodie, headers=headers)
    obj_ifoodie = bs(response_ifoodie.text, 'lxml')
    name = obj_ifoodie.find_all("a", "jsx-1156793088 title-text")
    rate = obj_ifoodie.find_all("div", "jsx-2373119553 text")
    run_time = obj_ifoodie.find_all("div", "jsx-1156793088 info")
    addr = obj_ifoodie.find_all("div", "jsx-1156793088 address-row")
    
    tags = obj_ifoodie.find_all("div", "jsx-1156793088 category-row")
    for ele in tags:
        listoftag=""
        tag_each = ele.find_all("a", "jsx-1156793088 category")
        for each_ele in range(1,len(tag_each)):
            listoftag += tag_each[each_ele].text + ","
        res_tag.append(listoftag)
    
    for j in name:
        res_name.append(j.text)
        
    for k in rate:
        res_rate.append(k.text)
    
    for m in run_time:
        res_time.append(m.text)
        
    for n in addr:
        res_addr.append(n.text)
        
    time.sleep(random.uniform(2,5))

    
df = {}
df["name"] = res_name
df["rate"] = res_rate
df["time"] = res_time
df["addr"] = res_addr
df["tags"] = res_tag

df_ifoodie = pd.DataFrame(df)

print(df_ifoodie)
