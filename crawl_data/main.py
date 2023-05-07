import requests
from bs4 import BeautifulSoup

cookies = {
    '__51cke__': '',
    'Hm_lvt_b9075b197cfe7b55eccdb05b64116349': '1683288630',
    'PHPSESSID': 'tdvbtj3h0tri4366dsg2k64t52',
    '__tins__21564427': '%7B%22sid%22%3A%201683288629571%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201683290790091%7D',
    '__51laig__': '4',
    'Hm_lpvt_b9075b197cfe7b55eccdb05b64116349': '1683288990',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://www.kangtemu.com/top.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': '__51cke__=; Hm_lvt_b9075b197cfe7b55eccdb05b64116349=1683288630; PHPSESSID=tdvbtj3h0tri4366dsg2k64t52; __tins__21564427=%7B%22sid%22%3A%201683288629571%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201683290790091%7D; __51laig__=4; Hm_lpvt_b9075b197cfe7b55eccdb05b64116349=1683288990',
}

response = requests.get('http://www.kangtemu.com/', cookies=cookies, headers=headers, verify=False)
print(response.text)

# 匹配内容
content = 'body > div.container > div > div:nth-child(1) > div.col-lg-5.col-md-6.col-sm-12.p-0 > div.clearfix.hidden-xs > div.box-video-text-list.clearfix'
response.encoding='utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

fo = open("./微博热搜.txt", 'a', encoding="utf-8")
a = soup.select(selector=content)
for i in range(0, len(a)):
    a[i] = a[i].text
    fo.write(a[i] + '\n')
fo.close()
