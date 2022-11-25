from application.net.session import Session

from application.utils import (
    buildRandomBuvid, LOGIN_SIGN,
    sortedFormData, addSign,
    rsaPassport
)

from application.module.decoration import error

from application.config import login_config

import httpx
import time


class PassportLogin(Session):
    @error
    def __init__(self, versions: tuple[str, str], system: tuple[str, str]):
        super(PassportLogin, self).__init__(**login_config)

        __statistics = '{"appId":1,"platform":3,"version":"__ver__","abtest":""}'

        (self.name, self.code), (self.model, self.os_ver) = versions, system
        self.channel, self.buvid = login_config["channel"], buildRandomBuvid()
        self.statistics = __statistics.replace("__ver__", self.name)

        self.cookies = {"Buvid": self.buvid}

        user_agent = login_config["user_agent"].format(
            MODEL=self.model, OSVER=self.os_ver,
            NAME=self.name, CODE=self.code,
            CHANNEL=self.channel
        )

        self.headers.update({"User-Agent": user_agent})
        self.headers.update({"Buvid": self.buvid})

    @error
    def web_key(self) -> httpx.Response:
        params = {
            "appkey": LOGIN_SIGN[0], "build": self.code,
            "buvid": self.buvid, "channel": self.channel,
            "disable_rcmd": "0", "local_id": self.buvid,
            "mobi_app": "android", "platform": "android",
            "statistics": self.statistics,
            "ts": round(time.time())
        }
        params = sortedFormData(params)
        params = addSign(params, LOGIN_SIGN)
        url = "https://passport.bilibili.com/x/passport-login/web/key"
        res = self.request("GET", url, params=params)
        return res

    @error
    def oauth2_login(self, username: str, passport: str, key: str, rhash: str):
        device_platform = "Android" + str(self.os_ver) + str(self.model)
        form_data = {
            "appkey": LOGIN_SIGN[0], "build": self.code,
            "buvid": self.buvid, "channel": self.channel,
            "device": "phone", "device_name": self.model,
            "disable_rcmd": "0", "local_id": self.buvid,
            "mobi_app": "android", "platform": "android",
            "password": rsaPassport(passport, key, rhash),
            "device_platform": device_platform,
            "statistics": self.statistics,
            "ts": round(time.time()),
            "username": username
        }
        form_data = sortedFormData(form_data)
        form_data = addSign(form_data, LOGIN_SIGN)
        url = "https://passport.bilibili.com/x/passport-login/oauth2/login"
        response = self.request("POST", url, data=form_data)
        return response

    @error
    def captcha_pre(self) -> httpx.Response:
        form_data = {
            "appkey": LOGIN_SIGN[0],
            "disable_rcmd": "0",
            "statistics": self.statistics,
            "ts": round(time.time())
        }
        form_data = sortedFormData(form_data)
        form_data = addSign(form_data, LOGIN_SIGN)
        url = "https://passport.bilibili.com/x/safecenter/captcha/pre"
        response = self.request("POST", url, data=form_data)
        return response

    def sms_send(self, tmp_code: str, **kwargs) -> httpx.Response:
        form_data = {
            "appkey": LOGIN_SIGN[0], "disable_rcmd": "0",
            "sms_type": "loginTelCheck", "tmp_code": tmp_code,
            "statistics": self.statistics, "ts": round(time.time())
        }
        kwargs.pop("recaptcha_type", None)
        form_data.update(kwargs)
        form_data = sortedFormData(form_data)
        form_data = addSign(form_data, LOGIN_SIGN)
        url = "https://passport.bilibili.com/x/safecenter/common/sms/send"
        response = self.request("POST", url, data=form_data)
        return response

    def user_info(self, tmp_code: str) -> httpx.Response:
        params = {
            "appkey": LOGIN_SIGN[0],
            "disable_rcmd": "0",
            "statistics": self.statistics,
            "tmp_code": tmp_code,
            "ts": round(time.time())
        }
        params = sortedFormData(params)
        params = addSign(params, LOGIN_SIGN)
        url = "https://passport.bilibili.com/x/safecenter/user/info"
        response = self.request("GET", url, params=params)
        return response

    def tel_verify(self, captcha_key: str, code: str | int, **kwargs) -> httpx.Response:
        device_platform = "Android" + str(self.os_ver) + str(self.model)
        form_data = {
            "appkey": LOGIN_SIGN[0], "build": self.code,
            "buvid": self.buvid, "captcha_key": captcha_key,
            "code": code, "device_name": self.model,
            "device_platform": device_platform,
            "disable_rcmd": "0", "local_id": self.buvid,
            "source": "risk", "statistics": self.statistics,
            "ts": round(time.time()), "type": "loginTelCheck"
        }
        form_data.update(kwargs)
        form_data = sortedFormData(form_data)
        form_data = addSign(form_data, LOGIN_SIGN)
        url = "https://passport.bilibili.com/x/safecenter/login/tel/verify"
        response = self.request("POST", url, data=form_data)
        return response

    def oauth2_access_token(self, code: str) -> httpx.Response:
        device_platform = "Android" + str(self.os_ver) + str(self.model)
        form_data = {
            "appkey": LOGIN_SIGN[0], "build": self.code,
            "buvid": self.buvid, "channel": self.channel,
            "device_name": self.model, "device": "phone",
            "device_platform": device_platform,
            "disable_rcmd": "0", "local_id": self.buvid,
            "grant_type": "authorization_code",
            "mobi_app": "android", "platform": "android",
            "statistics": self.statistics, "code": code,
            "ts": round(time.time())
        }
        form_data = sortedFormData(form_data)
        form_data = addSign(form_data, LOGIN_SIGN)
        url = "https://passport.bilibili.com/x/passport-login/oauth2/access_token"
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


class SmsLogin(Session):
    @error
    def __init__(self, versions: tuple[str, str], system: tuple[str, str]):
        super(SmsLogin, self).__init__(**login_config)

        __statistics = '{"appId":1,"platform":3,"version":"__ver__","abtest":""}'

        (self.name, self.code), (self.model, self.os_ver) = versions, system
        self.channel, self.buvid = login_config["channel"], buildRandomBuvid()
        self.statistics = __statistics.replace("__ver__", self.name)

        user_agent = login_config["user_agent"].format(
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
        device_platform = "Android" + str(self.os_ver) + str(self.model)
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
