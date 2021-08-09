# 作为第二个爬虫练习，查看百度翻译返回的结果（json），并保存
# 1、知识点，复习巩固

import requests
import json


def request_baidu_translation():
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    keyword = input('文件名字：')
    param = {
        'cname': '',
        'pid': '',
        'keyword': '郫',
        'pageIndex': 1,
        'pageSize': 10
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    res = requests.post(url=url, data=param, headers=header)
    with open(f'{keyword}.json', 'wt+', encoding='utf-8', errors='ignore') as f:
        a = json.dumps(res.json(), ensure_ascii=False)
        f.write(a)


if __name__ == '__main__':
    request_baidu_translation()
