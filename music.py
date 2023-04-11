# -*- coding: utf-8 -*-
"""
@Time ： 2023/4/11 16:45
@Auth ： LeWink
@File ：music.py
@IDE ：PyCharm
@Describe:酷我音乐歌单保存
"""
import json
import urllib3
#https://m.kuwo.cn/h5app/playlist/3302085519?t=plantform&from=ar
pid = 3302085519  #分享歌单时选择 复制试听链接 位于 playlist/ 之后的一串数字
page = 1
while 1:
    url = 'https://m.kuwo.cn/newh5app/wapi/api/www/playlist/playListInfo?pid=' + str(pid) + '&pn=' + str(page) + '&rn=100'
    page += 1
    http = urllib3.PoolManager()
    json_file = http.request('GET', url, headers={'Accept': 'application/json'})
    json_dict: dict = json.loads(json_file.data.decode('utf-8'))
    if len(json_dict['data']['musicList']) == 0 :
        print("\n\n【所有歌曲搜寻完毕】")
        break
    # print(json_dict)
    for index, mu in enumerate(json_dict['data']['musicList']):
        print("{}-{}".format(mu['name'], mu['artist']))
