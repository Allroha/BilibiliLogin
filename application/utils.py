import hashlib
import base64
import json
import uuid
import time
import os

from urllib.parse import urlencode
from urllib.parse import urlsplit
from urllib.parse import unquote


ReaderMode_Setting = "setting"
ReaderMode_Content = "content"

LOGIN_SIGN = ("783bbb7264451d82", "2653583c8873dea268ab9386918b1d65")


def reader(path: str, mode=ReaderMode_Setting) -> list | dict | bytes | None:
    with open(os.path.abspath(path), "rb") as file:
        file_data = file.read()
    file.close()
    if mode == ReaderMode_Setting:
        return json.loads(file_data.decode())
    elif mode == ReaderMode_Content:
        return file_data
    else:
        return None


def buildRandomBuvid(header: str = "XY", length: int = 35) -> str:
    """ 生成buvid """
    random_text = str(uuid.uuid4()).replace("-", "")
    while len(random_text) < length:
        random_text += str(uuid.uuid4()).replace("-", "")
    return str(header + random_text[:length]).upper()


def addSign(form_data: dict, key_and_sec=LOGIN_SIGN) -> dict:
    """ 添加sign """
    text = urlencode(form_data) + key_and_sec[1]
    hashlib_md5 = hashlib.md5()
    hashlib_md5.update(text.encode())
    form_data.update({"sign": hashlib_md5.hexdigest()})
    return form_data


def urlQuerySplit(url: str) -> dict:
    """ 分割url query参数 """
    data: list[str] = urlsplit(url).query.split("&")
    query_dict = dict()
    for li in data:
        i = li.split("=")
        query_dict[i[0]] = "" if len(i) == 1 else unquote(i[1])
    return query_dict


def sortedFormData(form_data: dict):
    """ 表单排序 """
    return_form_data = dict()
    form_data_keys = sorted(form_data)
    for key in form_data_keys:
        return_form_data[key] = form_data[key]
    return return_form_data

