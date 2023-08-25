
import requests
from lxml import etree
import os

# http://music.163.com/song/media/outer/url?id=

# 确定真实地址在Network----Doc
url = 'https://music.163.com/playlist?id=26467741'
base_url = 'http://music.163.com/song/media/outer/url?id='

# 请求（requests） 图片，视频，音频  content ｜ 字符串 text
html_str = requests.get(url).text
# print(type(html_str))       # 字符串类型


# 利用xpath筛选数据

result = etree.HTML(html_str)       # 转换类型
# print(type(result))
song_ids = result.xpath('//a[contains(@href,"/song?")]/@href')   # 歌曲id
song_names = result.xpath('//a[contains(@href,"/song?")]/text()')       # 歌名

# print(song_ids)
# print(song_names)     #列表


folder = './song'
if not os.path.exists(folder):
    os.makedirs(folder)


# 对列表进行解压
for song_id,song_name in zip(song_ids,song_names):
    # print(song_id)
    # print(song_name)
    count_id = song_id.strip('/song?id=')   # 去掉/song?id=
    # print(count_id)

    # 过滤含有“$”符号
    if ('$' in count_id) == False:
        # print(count_id)
        song_url = base_url + count_id      # 拼接url
        # print(song_url)

        mp3 = requests.get(song_url).content

        # 保存数据
        
        with open('song/{}.mp3'.format(i,song_name),'wb') as file:
            file.write(mp3)