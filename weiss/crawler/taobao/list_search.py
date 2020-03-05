# -*- coding: utf-8 -*-
__author__ = "xusiwei"
__created_date__ = "2020/2/25"

# https://blog.csdn.net/weixin_36842174/article/details/91359169

import hashlib
import time

import requests


def hex_md5(s):
    m = hashlib.md5()
    m.update(s.encode('UTF-8'))
    return m.hexdigest()


def get_page(index, num):
    url = 'https://acs.m.taobao.com/h5/mtop.taobao.wsearch.h5search/1.0/'
    appKey = '12574478'
    # 获取当前时间戳
    t = str(int(time.time() * 1000))
    data = '{"q":"ipone11","tab":"all","sst":"1","n":20,"buying":"buyitnow","m":"api4h5","token4h5":"","abtest":"14","wlsort":"14","page":1}'
    params = {
        'appKey': appKey,
        'data': data,
        'jsv': '2.3.16',
        't': t,
        'sign': '1f317cfbdeef7cfff637b4b269e084b4',
        'api': 'mtop.taobao.wsearch.h5search',
        'v': '1.0',
        'H5Request': 'true',
        'ecode': 1,
        'AntiCreep': 'true',
        'AntiFlool': 'true',
        'type': 'jsonp',
        'dataType': 'jsonp',
        'callback': 'mtopjsonp2'
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'thw=cn; cna=S77bFrM5BRoCAdpLI/77ePfz; v=0; cookie2=1dd0461d3721efe57f61b82d7a54ec7d; t=632956b36cdd75952e3a2f738e255e81; _tb_token_=eb33b3e38e3e3; _samesite_flag_=true; sgcookie=Dw0krn70alXbnIg3Ac3jv; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&vt3=F8dBxd3zCJoIPTJAB50%3D&id2=VAMVcR9QW68%3D&nk2=EFeHSeB5NMg%3D; csg=a34f1b71; lgc=siwei666; dnk=siwei666; skt=f6d471936fe37b1f; existShop=MTU4MjY4MjA4Nw%3D%3D; uc4=id4=0%40VhpIhGCtnHzB5e%2BKjtRV4B2qkg%3D%3D&nk4=0%40Eo4zlDtRKl8IdzmV5KGvb2kr9Q%3D%3D; tracknick=siwei666; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; tfstk=cdfFBA6NxQj_GSwNnIOyVk9k2QbdZp6CFA8DKtAvB-mqde9hihiJSz09b3xYspf..; mt=ci=101_1; enc=dAhyJM2%2ByLNfWebGF84a0nyksLeQr2gvBjYROfwPmQ3TxIQANdIlmQNKIyXLWt%2BLhTXsyJLzgaRT699ukbhU7A%3D%3D; uc1=cookie14=UoTUOLRxVOokCg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=9b555e14d0c05eccbfa4347d87e65917_1583149063264; _m_h5_tk_enc=224e7788ae616ce5882b70e09cb807af; l=dBa9iIvuQiTp7IsaBOCwourza77OSIRAguPzaNbMi_5pL6Ls0kbOoJBbgFp6VjWfGpTB4yMnk_e9-etXiJcvEmxsHjx20xDc.; isg=BOvrv14fMW6klG2ygk5_RKA6egnVAP-CeXbcRV1oxiqB_Ate5dKd005aVjySXFd6',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    # _m_h5_tk=9b555e14d0c05eccbfa4347d87e65917_1583149063264; _m_h5_tk_enc=224e7788ae616ce5882b70e09cb807af;
    _m_h5_tk = '9b555e14d0c05eccbfa4347d87e65917_1583149063264'
    _m_h5_tk_enc = '224e7788ae616ce5882b70e09cb807af'
    token = _m_h5_tk.split('_')[0]
    u = token + '&' + t + '&' + appKey + '&' + data
    # MD5加密
    sign = hex_md5(u)
    params['sign'] = sign

    # 请求空获取cookies
    session = requests.sessions.Session()
    html = session.get(url, headers=headers, params=params)
    print(html.text)

    if html.text.find("FAIL_SYS_TOKEN_EXOIRED") != -1:
        _m_h5_tk = html.cookies['_m_h5_tk']
        _m_h5_tk_enc = html.cookies['_m_h5_tk_enc']
        token = _m_h5_tk.split('_')[0]
        u = token + '&' + t + '&' + appKey + '&' + data
        # MD5加密
        sign = hex_md5(u)
        print('秘钥：' + sign)
        # 复用 session中的cookie
        params['sign'] = sign
        html = session.get(url, params=params)
        print(html.text)


get_page(1, 20)
