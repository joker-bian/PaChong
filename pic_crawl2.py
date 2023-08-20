import time
import requests
from lxml import etree    #这是导入xpath模块
import os


headers= {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Cookie': '__yjs_duid=1_79ad12e0fc9a0f9915bc01c5c688af461692375275139; Hm_lvt_c59f2e992a863c2744e1ba985abaea6c=1692375276,1692454803; PHPSESSID=v5sjb0fn6a3u80ag0i3vhcqi54; zkhanmlusername=qq104564169245; zkhanmluserid=7164815; zkhanmlgroupid=1; zkhanmlrnd=6jLWXye1DXtGOeHe5LJY; zkhanmlauth=6e5fadab864d1d0e9bde168b482d176b; Hm_lpvt_c59f2e992a863c2744e1ba985abaea6c=1692455200',
}


def get_pic(url, headers):
    resp=requests.get(url=url,headers=headers)
    # main_text = resp.content.decode('gbk')
    # print(main_text)

    resp.encoding="gbk"
    tree=etree.HTML(resp.text)

    if not os.path.exists("./img") :    #创建文件夹
        os.mkdir("./img")

    tu_list = tree.xpath('//div[@class="slist"]//li')
    for tu in tu_list:
        tu_html = 'https://pic.netbian.com/' + tu.xpath("./a/img/@src")[0]   #循环获取图片的url
        name = tu.xpath("./a/img/@alt")[0]  #获取图片名称
        tu_get = requests.get(url=tu_html, headers=headers).content   #进行持久化存储

        name_path = "img/" + name.replace(" ", "_") + '.jpg'

        with open(name_path,"wb") as f:
            f.write(tu_get)
            print(name , "下载完成")



for i in range(1,6):
    if i == 1:
        url = "https://pic.netbian.com/4kdongman/index.html"
    else:
        url = "https://pic.netbian.com/4kdongman/index_{}.html".format(i)
    print('开始爬取第'+str(i)+"页数据")
    get_pic(url, headers)
    print('第'+str(i)+"页数据爬取完成")
    time.sleep(2)

print('finished!')
