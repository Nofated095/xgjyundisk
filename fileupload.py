# -*- coding: utf-8 -*-
# https://banjixiaoguanjia.com/public/website/index.html#page1/1
# 你必须是班级小管家的老师角色才能使用此脚本...

import oss2
import json
import os
import uuid


def readCookie():
    with open('cookie.txt','r',encoding='utf-8') as ck:
        cookie = ck.read()
    return cookie


cookie = readCookie()
auth_info = json.loads(cookie.replace("%22", '"').replace("%2C", ","))

auth = oss2.StsAuth(
    auth_info['AccessKeyId'], auth_info['AccessKeySecret'], auth_info['SecurityToken'])
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'xgjyundisk')


def upload_file(path):
    with open(path, 'rb') as fileobj:
        _uuid = str(uuid.uuid1()).upper()
        oss_img_url = "https://xgjyundisk.oss-cn-hangzhou.aliyuncs.com/" + \
            f'63cb7c243eab49d55b481gb8/{_uuid}{os.path.splitext(path)[1]}'
        result = bucket.put_object(
            f'63cb7c243eab49d55b481gb8/{_uuid}{os.path.splitext(path)[1]}', fileobj)
        return result.status, oss_img_url


# 遍历目录包括子目录
def walk(path):
    file_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_paths.append(os.path.join(root, file))
        for dir in dirs:
            walk(os.path.join(root, dir))

    return file_paths


if __name__ == "__main__":
    file_paths = walk("cache")
    cache_info = {}
    for path in file_paths:
        print(upload_file(path))
        cache_info[path] = upload_file(path)[1]
    with open("file_cache.json", "w") as cache:
        json.dump(cache_info, cache)
