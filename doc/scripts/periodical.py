import requests
from lxml import etree
import re
# url = 'http://www.wanfangdata.com.cn/perio/page.do'

headers = {
	'Referer': 'http://www.wanfangdata.com.cn/perio/toIndex.do',
	'Origin': 'http://www.wanfangdata.com.cn',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
}


post_data = {
	'page': 3,
	'pageSize': 3,
	'selectOrder': 'affectoi',
	'fromData': 'WF',
}
post_form = {
	'page': 2,
	'pageSize': 100,
	'selectOrder': 'affectoi',
	'fmList': 'B',
	'fromData': 'WF',
}

# r = requests.post(url=url,headers=headers,data=post_data)
# r = requests.post(url=url,headers=headers,data=post_form)

# print(type(r.text))
# with open('哲学政法1.json','w',encoding='utf8') as f:
# 	f.write(r.text)
# print('OK')
# num = 70+181+294+445+9+167+535+647+1+624+193+265+111+279+0+16+181+90+869+216+0+0+199+616+373+1479
# print(num)  # 7860


url = 'http://www.wanfangdata.com.cn/perio/detail.do?perio_id=nfdwjs' # 南方电网技术
r = requests.get(url=url,headers=headers)

content = r.text

tree = etree.HTML(content)

funds = tree.xpath('//div[@class="top-rt"]/div[3]/text()')
funds_num = funds[0]
print(funds_num)
a = re.sub(r'\D','',funds_num)
print(a)
print(type(a))
# sum = 461+730+784+1655+902+1238+579+2225
# print(sum) # 8574

