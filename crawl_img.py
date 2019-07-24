import requests
import os
url = 'http://imgsrc.baidu.com/forum/pic/item/30c475cf36d3d5392fd958803d87e950342ab0b9.jpg'
root = 'D:/data2'
path = root+url.split('/')[-1]
try:
    r=requests.get(url)
    r.raise_for_status()
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
