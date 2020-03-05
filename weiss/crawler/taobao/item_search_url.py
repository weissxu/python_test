import requests



response = requests.get('https://item.taobao.com/item.htm?id=613057255888')
# response.encoding = 'utf-8'
print(response.text)
