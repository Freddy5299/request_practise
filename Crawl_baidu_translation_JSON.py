# ��Ϊ�ڶ���������ϰ���鿴�ٶȷ��뷵�صĽ����json����������
# 1��֪ʶ�㣬requests post����
# 2��֪ʶ�㣬json�Ľ��������ַ�������

import requests
import json


def request_baidu_translation():
    url = 'https://fanyi.baidu.com/sug'
    keyword = input('������Ҫ�����Ĺؼ��ʣ�')
    param = {
        'kw': keyword
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