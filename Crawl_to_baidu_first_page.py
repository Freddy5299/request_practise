# ��Ϊ��һ��������ϰ����ȡ��ҳ���ұ���Ϊhtml��ʽ
# 1��֪ʶ�㣬requests get����
# 2���������ƣ�UA

import requests


def request_baidu():
    url = 'http://www.baidu.com/s'
    keyword = input('������Ҫ�����Ĺؼ��ʣ�')
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
