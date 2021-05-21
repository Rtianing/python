url = "https://jiadian.jd.com/"
import requests
try:
    r = requests.get(url)#就理解成get方法获取地址吧，里面呢的参数就是路径    Requests 会自动解码来自服务器的内容。大多数 unicode 字符集都能被无缝地解码
    r.raise_for_status()#使用r.encoding 属性来改变Requests的编码
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")