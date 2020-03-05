import ssl
from contextlib import closing
from urllib.request import urlopen

ssl._create_default_https_context = ssl._create_unverified_context

with closing(urlopen('https://www.baidu.com')) as page:
        print(page.read())