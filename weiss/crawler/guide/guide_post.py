import json

import requests

url = 'https://zone.guiderank-app.com/guiderank-web/app/specialSale/searchTBKCoupon.do?imei=1FAD6478-9BAD-4B8E-A53C-8FFCF1F357E4&role=1&model=iPhone%20XS_12.4.1&token&ver=iOS_3.20.3.6c180ed07'
headers = {
    'user-agent': 'iPhone XS,iOS 12.4.1,rank 3.20.3.6c180ed07',
    'authority': 'zone.guiderank-app.com',
    'accept-language': 'zh-cn',
    'fv': '8765F22B-DED7-41CD-85C2-38E342CCBC28',
    'fa': '1FAD6478-9BAD-4B8E-A53C-8FFCF1F357E4',
    'Content-Type': 'application/json;charset=UTF-8'
}

json_data = {'size': 10, 'sortType': 0, 'input': 'iphone11', 'page': 0}
session = requests.Session()
r = session.post(url, headers=headers, json=json_data)
# r = requests.post(url, headers=headers, json=json_data)
print('%s %s' % (r.status_code, r.reason))
for cookie in r.cookies:
    print(cookie)

json_result = json.loads(r.text)
print(type(json_result))
items = json_result['data']['coupons']

for i in items:
    print(json.dumps(i))

# file_name_src = '/Users/siwei/Documents/crawler/src/盖得%d%s' % (int(datetime.now().timestamp()), '.txt');
# print('writting to file: %s' % file_name_src)
# with open(file_name_src, "a+") as file:
#     for i in items:
#         file.write(json.dumps(i) + "\n")
