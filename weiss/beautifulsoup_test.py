from bs4 import BeautifulSoup

# url = 'https://www.baidu.com'
# response = requests.get(url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')

html = '''
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())

print('title: ' + soup.html.head.title.string)
print('soup.title.parent.name: ' + soup.title.parent.name)
print(soup.p)
print(soup.p.text)
# 标签名为p的class内容
print(soup.p["class"])

# 标签名为a的内容
print(soup.a)
print('================')

# 查找所有的字符a
print(soup.find_all('a'))

# 查找id='link3'的内容
print(soup.find(id='link3'))
