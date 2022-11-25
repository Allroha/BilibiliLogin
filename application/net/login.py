from application.net.session import Session

from application.utils import (
    buildRandomBuvid, LOGIN_SIGN,
    sortedFormData, addSign
)

from application.module.decoration import error

from application.config import sms_login_config

import httpx
import time


class SmsLogin(Session):
    @error
    def __init__(self, versions: tuple[str, str], system: tuple[str, str]):
        super(SmsLogin, self).__init__(**sms_login_config)

        __statistics = '{"appId":1,"platform":3,"version":"__ver__","abtest":""}'

        (self.name, self.code), (self.model, self.os_ver) = versions, system
        self.channel, self.buvid = sms_login_config["channel"], buildRandomBuvid()
        self.statistics = __statistics.replace("__ver__", self.name)

        user_agent = sms_login_config["user_agent"].format(
            MODEL=self.model, OSVER=self.os_ver,
            NAME=self.name, CODE=self.code,
            CHANNEL=self.channel
        )

        self.headers.update({"User-Agent": user_agent})
        self.headers.update({"Buvid": self.buvid})

    @error
    def sms_send(self, cid, tel, **kwargs) -> httpx.Response:
        form_data = {
            "appkey": LOGIN_SIGN[0], "build": self.code,
            "buvid": self.buvid, "channel": self.channel,
            "cid": cid, "disable_rcmd": "0",
            "local_id": self.buvid, "mobi_app": "android",
            "platform": "android", "statistics": self.statistics,
            "tel": tel, "ts": round(time.time()),
        }
        form_data.update(kwargs)
        form_data = sortedFormData(form_data)
        form_data = addSign(form_data, LOGIN_SIGN)
        url = "https://passport.bilibili.com/x/passport-login/sms/send"
        response = self.request("POST", url, data=form_data)
        return response

    @error
    def login_sms(self, cid, tel, captcha: str, code: str | int) -> httpx.Response:
        device_platform = "Android" + str(self.model) + str(self.os_ver)
        form_data = {
            "appkey": LOGIN_SIGN[0], "build": self.code,
            "buvid": self.buvid, "captcha_key": captcha,
            "channel": self.channel, "cid": cid, "tel": tel,
            "code": code, "device": "phone", "ts": round(time.time()),
            "device_name": self.model, "statistics": self.statistics,
            "disable_rcmd": "0", "local_id": self.buvid,
            "mobi_app": "android", "platform": "android",
            "device_platform": device_platform,
        }
        form_data = sortedFormData(form_data)
        form_data = addSign(form_data, LOGIN_SIGN)
        url = "https://passport.bilibili.com/x/passport-login/login/sms"
        response = self.request("POST", url, data=form_data)
        return response

    @error
    def extractCookie(self, response_json: dict) -> tuple[str, str]:
        access_key = str(response_json["data"]["token_info"]["access_token"])
        cookie_list = response_json["data"]["cookie_info"]["cookies"]
        cookie_dict = {li["name"]: li["value"] for li in cookie_list}
        cookie_dict.update({"Buvid": str(self.buvid)})
        cookie_list = [f"{k}={v}" for k, v in cookie_dict.items()]
        return access_key, "; ".join(cookie_list)
