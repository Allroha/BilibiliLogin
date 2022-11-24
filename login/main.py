from urllib.parse import urlencode
from urllib.parse import urlsplit
from urllib.parse import unquote

import hashlib
import httpx
import uuid
import time


versionsType = tuple[str, str]
systemType = tuple[str, str]
signType = tuple[str, str]

LOGIN_SIGN = ("783bbb7264451d82", "2653583c8873dea268ab9386918b1d65")


def buildRandomBuvid(header: str = "XY", length: int = 35) -> str:
    """ 生成buvid """
    random_text = str(uuid.uuid4()).replace("-", "")
    while len(random_text) < length:
        random_text += str(uuid.uuid4()).replace("-", "")
    return str(header + random_text[:length]).upper()


def buildSign(form_data: dict, key_and_sec: signType) -> str:
    text = urlencode(form_data) + key_and_sec[1]
    hashlib_md5 = hashlib.md5()
    hashlib_md5.update(text.encode())
    return hashlib_md5.hexdigest()


def urlQuerySplit(url: str) -> dict:
    """ 分割url query参数 """
    data: list[str] = urlsplit(url).query.split("&")
    query_dict = dict()
    for li in data:
        i = li.split("=")
        query_dict[i[0]] = "" if len(i) == 1 else unquote(i[1])
    return query_dict


class Session(httpx.Client):
    def __init__(self, versions: versionsType, system: systemType, **kwargs):
        super(Session, self).__init__(
            trust_env=kwargs.get("trust_env", False),
            proxies=kwargs.get("proxies", None),
            timeout=kwargs.get("timeout", 5)
        )

        (self.name, self.code), (self.model, self.os_ver) = versions, system
        self.channel = kwargs.get("channel", "yingyongbao")

        __statistics = '{"appId":1,"platform":3,"version":"__ver__","abtest":""}'
        __user_agent = f"Mozilla/5.0 BiliDroid/{self.name} (bbcallen@gmail" \
                       f".com) os/android model/{self.model} mobi_app/androi" \
                       f"d build/{self.code} channel/{self.channel} innerVe" \
                       f"r/{self.code} osVer/{self.os_ver} network/2"

        self.statistics = __statistics.replace("__ver__", self.name)
        self.buvid = kwargs.get("buvid", buildRandomBuvid())
        self.cookies = kwargs.get("cookies", dict())
        self.headers.update({
            "Accept-Encoding": "gzip",
            "User-Agent": __user_agent,
            "APP-KEY": "android",
            "Buvid": str(self.buvid)
        })
        self.headers.update(kwargs.get("headers", dict()))

    def sms_send_geetest(self, cid, tel, **kwargs) -> httpx.Response:
        form_data = {
            "appkey": LOGIN_SIGN[0],
            "build": self.code,
            "buvid": self.buvid,
            "channel": self.channel,
            "cid": cid,
            "gee_challenge": kwargs["gee_challenge"],
            "gee_seccode": kwargs["gee_seccode"],
            "gee_validate": kwargs["gee_validate"],
            "disable_rcmd": "0",
            "local_id": self.buvid,
            "mobi_app": "android",
            "platform": "android",
            "recaptcha_token": kwargs["recaptcha_token"],
            "statistics": self.statistics,
            "tel": tel,
            "ts": round(time.time()),
        }
        form_data.update({"sign": buildSign(form_data, LOGIN_SIGN)})
        url = "https://passport.bilibili.com/x/passport-login/sms/send"
        response = self.request("POST", url, data=form_data)
        return response

    def sms_send(self, cid: str | int, tel: str | int) -> httpx.Response:
        form_data = {
            "appkey": LOGIN_SIGN[0],
            "build": self.code,
            "buvid": self.buvid,
            "channel": self.channel,
            "cid": cid,
            "disable_rcmd": "0",
            "local_id": self.buvid,
            "mobi_app": "android",
            "platform": "android",
            "statistics": self.statistics,
            "tel": tel,
            "ts": round(time.time()),
        }
        form_data.update({"sign": buildSign(form_data, LOGIN_SIGN)})
        url = "https://passport.bilibili.com/x/passport-login/sms/send"
        response = self.request("POST", url, data=form_data)
        return response

    def login_sms(self, cid, tel, captcha: str, code: str | int) -> httpx.Response:
        device_platform = "Android" + str(self.model) + str(self.os_ver)
        form_data = {
            "appkey": LOGIN_SIGN[0],
            "build": self.code,
            "buvid": self.buvid,
            "captcha_key": captcha,
            "channel": self.channel,
            "cid": cid,
            "code": code,
            "device": "phone",
            "device_name": self.model,
            "device_platform": device_platform,
            "disable_rcmd": "0",
            "local_id": self.buvid,
            "mobi_app": "android",
            "platform": "android",
            "statistics": self.statistics,
            "tel": tel,
            "ts": round(time.time()),
        }
        form_data.update({"sign": buildSign(form_data, LOGIN_SIGN)})
        url = "https://passport.bilibili.com/x/passport-login/login/sms"
        response = self.request("POST", url, data=form_data)
        return response


class SmsLogin(Session):
    def __init__(self, *args, **kwargs):
        super(SmsLogin, self).__init__(*args, **kwargs)

        self.geetest_sever = kwargs.get("geetest_sever")
        if not self.geetest_sever:
            raise Exception("geetest_sever")

        if self.geetest_sever[-1] != "/":
            self.geetest_sever += "/"

    def run(self, cid: int | str, tel: int | str):
        sms_send_res = self.sms_send(cid, tel)
        if sms_send_res.json()["code"] != 0:
            raise Exception(sms_send_res.json()["message"])
        captcha_key = sms_send_res.json()["data"]["captcha_key"]
        if not captcha_key:
            recaptcha_url = sms_send_res.json()["data"]["recaptcha_url"]
            query_dict = urlQuerySplit(recaptcha_url)

            login_id = str(uuid.uuid4()) + str(round(time.time()))

            geetest_query = urlencode({
                "gee_gt": query_dict["gee_gt"], "id": login_id,
                "gee_challenge": query_dict["gee_challenge"],
            })

            print("-" * 50)
            print("浏览器打开:", self.geetest_sever[:-1] + f"?{geetest_query}")
            print("-" * 50)

            verify_url, params = (self.geetest_sever + "verify"), {"id": login_id}
            gee_res = self.request("GET", verify_url, params=params)

            while gee_res.json()["code"] != 0:
                gee_res = self.request("GET", verify_url, params=params)
                time.sleep(1)

            gee_kwargs: dict = gee_res.json()
            recaptcha_token = query_dict["recaptcha_token"]
            gee_kwargs.update({"recaptcha_token": recaptcha_token})
            sms_send_gee_res = self.sms_send_geetest(cid, tel, **gee_kwargs)
            if sms_send_gee_res.json()["code"] != 0:
                raise Exception("code != 0")
            captcha_key = sms_send_gee_res.json()["data"]["captcha_key"]

        verify_code = input("输入验证码:")

        login_res = self.login_sms(cid, tel, captcha_key, verify_code)
        print(login_res.json())

        return


class PasswordLogin(object):
    def __init__(self, *args, **kwargs):
        super(PasswordLogin, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    sms = SmsLogin(("7.6.0", "7060200"), ("SM-G955N", "9"), geetest_sever="http://127.0.0.1:5000")

    sms.run(cid=86, tel=2233)
