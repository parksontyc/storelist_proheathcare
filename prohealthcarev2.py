import requests
from bs4 import BeautifulSoup
import time 
from fake_useragent import UserAgent
import csv

store_name = []
store_addr = []

page = 1

url = "http://www.prohealthcare.com.tw/store.php?"
ua = UserAgent()
header ={"User-Agent":ua.random, "Referer":"http://www.prohealthcare.com.tw/index.php"}
res = requests.get(url, headers=header, timeout=3)
print(0)
print(res.url)
print(res.status_code, "大台北地區")
html = res.text

def parse(html, page):
    print(page)
    soup = BeautifulSoup(html.replace("\n","").strip(), "html.parser")
    item_name = soup.find_all("div", class_="t13_2")
    
    for name in item_name:
        store_name.append(name.a.text.strip())
        #print(store_name)
    item_addr = soup.find_all("div", class_="t13", id="store_3")
    for addr in item_addr:
        store_addr.append(addr.text.strip())
        #print(store_addr)
    
    if page == 1:
        next_page_tp_node = soup.find("div", class_="t12b").find_next().find_next().a
        next_page_tp_url = f"http://www.prohealthcare.com.tw/{next_page_tp_node.get('href')}"
        print(next_page_tp_url)
        page += 1
        time.sleep(2)
        next_tp_res = requests.get(next_page_tp_url)
        print(next_tp_res.status_code, "大台北地p2")
        new_tp_html = next_tp_res.text
        parse(new_tp_html, page)
    elif page == 2:
        next_page_tu_node = soup.find("li", id="n2").find_next().find_next().a     #桃竹地區url
        next_page_tu_url = f"http://www.prohealthcare.com.tw/{next_page_tu_node.get('href')}"
        print(next_page_tu_url)
        page += 1
        time.sleep(2)
        next_tu_res = requests.get(next_page_tu_url)
        print(next_tu_res.status_code, "桃竹地區")
        new_tu_html = next_tu_res.text
        parse(new_tu_html, page)
    elif page == 3:
        next_page_mid_node = soup.find("li", id="n2").find_next().find_next().find_next().find_next().a     #中部地區url
        next_page_mid_url = f"http://www.prohealthcare.com.tw/{next_page_mid_node.get('href')}"
        print(next_page_mid_url)
        page += 1
        time.sleep(2)
        next_mid_res = requests.get(next_page_mid_url)
        print(next_mid_res.status_code, "中部地區")
        new_mid_html = next_mid_res.text
        parse(new_mid_html, page)
    elif page == 4:
        next_page_s_node = soup.find("li", id="n2").find_next().find_next().find_next().find_next().find_next().find_next().a     #南部地區url
        next_page_s_url = f"http://www.prohealthcare.com.tw/{next_page_s_node.get('href')}"
        print(next_page_s_url)
        page += 1
        time.sleep(2)
        next_s_res = requests.get(next_page_s_url)
        print(next_s_res.status_code, "南部地區")
        new_s_html = next_s_res.text
        parse(new_s_html, page)
    elif page == 5:
        next_page_e_node = soup.find("li", id="n2").find_next().find_next().find_next().find_next().find_next().find_next().find_next().find_next().a     #東部地區url
        next_page_e_url = f"http://www.prohealthcare.com.tw/{next_page_e_node.get('href')}"
        print(next_page_e_url)
        page += 1
        time.sleep(2)
        next_e_res = requests.get(next_page_e_url)
        print(next_e_res.status_code, "東部地區")
        new_e_html = next_e_res.text
        parse(new_e_html, page)
   

parse(html, page)
print(store_name)
print(store_addr)

with open('storelist_prohealthcare.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市名稱', '門市地址']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_name[n])
        newrow.append(store_addr[n])
        csvwriter.writerow(newrow)








