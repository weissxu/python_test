import requests

url = 'http://www.baidu.com'


# r = requests.get(url)
# print('get head line: %s,%s' % (r.status_code, r.reason))

# r = requests.post(url)
# print('post head line: %s,%s' % (r.status_code,r.reason))

# print('text----->' + r.content.decode('utf-8'))
# # print('text----->' + r.content.decode('utf-8'))
# print('encoding---->' + r.encoding)
# r.encoding = 'utf-8'
# print('text----->' + r.text)

def format_print(response):
    response.encoding = 'utf-8'
    print('text:' + response.text)


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5;windows NT)'
headers = {'user_agent': user_agent}
cookies = dict(name='maomi', age='3')
r = requests.get(url, headers=headers, cookies=cookies)
# format_print(r)
for cookie in r.cookies.keys():
    print(cookie + ':' + r.cookies[cookie])

s = requests.Session()
login_url = 'http://www.sina.com/login'
r = s.get(login_url, allow_redirects=True)
format_print(r)
datas = {'name': 'maomi', 'passwd': 'maomi'}
r = s.post(login_url, data=datas,datas='', allow_redirects=True,json='')
format_print(r)
