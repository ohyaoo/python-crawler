# -*- coding: UTF-8 -*-
import urllib.request


def main():
    # 默认使用百度搜索
    url = 'http://www.baidu.com'
    response = urllib.request.urlopen(url=url)
    with open('files/baidu.html', 'wb') as fp:
        fp.write(response.read())

if __name__ == "__main__":
    main()
