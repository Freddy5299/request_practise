# 作为第二个爬虫练习，查看百度翻译返回的结果（json），并保存
# 1、知识点，多个实战

import requests
import json
import os


def request_baidu_translation():
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    data_list = []
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    for i in range(1, 3):
        param = {
            'on': 'true',
            'page': i,
            'pageSize': 15,
            'conditionType': 1
        }
        res_all_id = requests.post(url=url, data=param, headers=header)
        data_list.append(res_all_id.json())
    print(data_list)
    if not os.path.exists('Drug_Administration_Data'):
        os.mkdir('Drug_Administration_Data')
    else:
        print("Dir exists")
    for i in data_list:
        if not os.path.exists(f'./Drug_Administration_Data/Page_{data_list.index(i)}'):
            os.mkdir(f'./Drug_Administration_Data/Page_{data_list.index(i)}')
        else:
            print("Dir exists")
        for j in range(15):
            with open(f"./Drug_Administration_Data/Page_{data_list.index(i)}/{i['list'][j]['EPS_NAME']}.json", 'wt+',
                      encoding='utf-8', errors='ignore') as f:
                json.dump(detail_crawl(i['list'][j]['ID']), fp=f, ensure_ascii=False)


def detail_crawl(ID_EPS: str):
    url_detail = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    param = {
        'id': ID_EPS,
    }
    res_all_id = requests.post(url=url_detail, data=param, headers=header)
    return res_all_id.json()


if __name__ == '__main__':
    request_baidu_translation()
