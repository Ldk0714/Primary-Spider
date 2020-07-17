import requests as res


res_music = res.get(
    'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=69918498523518579&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%B7%B1&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# url是在XHR文件中找
json_music = res_music.json()  # 将网页数据转换成json文本
list_all = json_music['data']['song']['list']  # 文本是个列表字典互相嵌套的类型
list_music = []
for each_list in list_all[0:51]:
    name = each_list['name']
    url = each_list['url']
    time = each_list['time_public']
    list_music.append([name, time, url])
for i in list_music:
    print('歌曲名是：' + i[0] + '\t发布时间是：' + i[1] + '\n链接是：' + i[2])
    print('--------------------------------------------------------')

import csv

with open(r'C:\Users\Administrator\Desktop\music.csv', 'a', newline='') as csvfile:
    # 调用open()函数打开csv文件，传入参数：文件名“assets.csv”、追加模式“a”、newline=''。
    writer = csv.writer(csvfile, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。
    header = ['歌曲名', '发布时间', '链接']
    writer.writerow(header)
    for i in list_music:
        writer.writerow([i[0], i[1], i[2]])
