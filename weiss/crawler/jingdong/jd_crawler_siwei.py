import csv

import requests
from lxml import etree


# 定义函数抓取每页前30条商品信息
def crow_first(n):
    # 构造每一页的url变化
    url = 'https://search.jd.com/Search'
    head = {'authority': 'search.jd.com',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
            }
    params = {
        'keyword': 'Apple iPhone 11 (A2223) 128GB 白色 移动联通电信4G手机 双卡双待',
        'enc': 'utf-8',
        'wq': 'Apple iPhone 11 (A2223) 128GB 白色 移动联通电信4G手机 双卡双待'
    }
    r = requests.get(url, headers=head, params=params)
    # 指定编码方式，不然会出现乱码
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    # 定位到每一个商品标签li
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    # 将抓取的结果保存到本地CSV文件中
    with open('JD_Phone_siwei.csv', 'a', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        for data in datas:
            p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            p_comment = data.xpath('div/div[5]/strong/a/text()')
            p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em')
            # 这个if判断用来处理那些价格可以动态切换的商品，比如上文提到的小米MIX2，他们的价格位置在属性中放了一个最低价
            if len(p_price) == 0:
                p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
                # xpath('string(.)')用来解析混夹在几个标签中的文本
            # write.writerow([p_name[0].xpath('string(.)'), p_price[0]])
            print(p_name[0].xpath('string(.)') + "," + p_price[0])
            print('%s,%s' % (p_name[0].xpath('string(.)'), p_price[0]))
        f.close()


if __name__ == '__main__':
    # 下面的print函数主要是为了方便查看当前抓到第几页了
    print('***************************************************')
    try:
        print('   crawling..   ' + str(0))
        crow_first(0)
        print('   Finish')
    except Exception as e:
        print(e)
    print('------------------')
