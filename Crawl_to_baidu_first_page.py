# 作为第一个爬虫练习，爬取网页并且保存为html格式
# 1、知识点，requests get方法
# 2、反爬机制，UA

import requests


def request_baidu():
    url = 'http://www.baidu.com/s'
    keyword = input('输入需要搜索的关键词：')
    param = {
        'wd': keyword
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    res = requests.get(url=url, params=param, headers=header)
    with open(f'{keyword}.html', 'wt+', encoding='utf-8', errors='ignore') as f:
        f.write(res.text)


if __name__ == '__main__':
    request_baidu()
