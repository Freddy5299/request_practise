# ��Ϊ������������ϰ����̬��ȡ�������а�
# 1��֪ʶ�㣬�����������

import requests
import json


def request_baidu_translation():
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': 24,
        'interval_id': '100:90',
        'action': '',
        'start': 0,
        'limit': 100
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    res = requests.get(url=url, params=param, headers=header)
    print(res.json())
    return res.json()


def write_json(res_json):
    keyword = input('����洢���ļ����ƣ�')
    with open(f'{keyword}.json', 'wt+', encoding='utf-8', errors='ignore') as f:
        a = json.dumps(res_json, ensure_ascii=False)
        f.write(a)


if __name__ == '__main__':
    res_json = request_baidu_translation()
    write_json(res_json=res_json)