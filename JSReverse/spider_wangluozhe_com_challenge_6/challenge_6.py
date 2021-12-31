# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-12-20
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: challenge_6.py
# @Software: PyCharm
# ==================================


import execjs
import requests


challenge_api = "http://spider.wangluozhe.com/challenge/api/6"
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "session=eb2d1c7c-3179-4776-938e-f995478c1ebe.wdC8W9r38z_O97ynvrtBlSEQzPk; v=A0ljXUrQTfK4UjBNHUpAlhwCWH6glj1Yp4thXOu-xd5tGGdoM-ZNmDfacSh4",
    "Host": "spider.wangluozhe.com",
    "Origin": "http://spider.wangluozhe.com",
    "Referer": "http://spider.wangluozhe.com/challenge/6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}


def get_hexin_v():
    with open('challenge_6.js', 'r', encoding='utf-8') as f:
        wlz_js = execjs.compile(f.read())
    hexin_v = wlz_js.call("getHexinV")
    print("hexin-v: ", hexin_v)
    return hexin_v


def main():
    result = 0
    for page in range(1, 101):
        data = {
            "page": page,
            "count": 10,
        }
        headers["hexin-v"] = get_hexin_v()
        response = requests.post(url=challenge_api, headers=headers, data=data).json()
        for d in response["data"]:
            result += d["value"]
    print("结果为: ", result)


if __name__ == '__main__':
    main()
