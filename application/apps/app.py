from geetest.geetest import GeeTest

from application.module.decoration import error

from application.net.login import SmsLogin

from application.utils import urlQuerySplit


@error
def sms(cid: int | str, tel: int | str, versions, system) -> tuple[str, str]:
    login = SmsLogin(versions=versions, system=system)
    sms_send_res = login.sms_send(cid, tel)
    if sms_send_res.json()["code"] != 0:
        raise Exception(sms_send_res.json()["message"])

    captcha_key = sms_send_res.json()["data"]["captcha_key"]

    if not captcha_key:
        recaptcha_url = sms_send_res.json()["data"]["recaptcha_url"]
        query_dict = urlQuerySplit(recaptcha_url)

        print("完成人机验证以继续")

        gee = GeeTest(query_dict["gee_gt"], query_dict["gee_challenge"])
        gee_verify = gee.waitFinishing(time_sleep=1)

        gee_form_data = {
            "gee_challenge": gee_verify["geetest_challenge"],
            "gee_seccode": gee_verify["geetest_seccode"],
            "gee_validate": gee_verify["geetest_validate"],
            "recaptcha_token": query_dict["recaptcha_token"],
        }
        sms_send_res = login.sms_send(cid, tel, **gee_form_data)
        if sms_send_res.json()["code"] != 0:
            raise Exception(sms_send_res.json()["message"])
        captcha_key = sms_send_res.json()["data"]["captcha_key"]

    access_key, cookie = str(), str()

    while not cookie and not access_key:
        verify_code = input("输入验证码:")

        login_res = login.login_sms(cid, tel, captcha_key, verify_code)
        if login_res.json()["code"] != 0:
            print(login_res.json()["message"])
            continue
        access_key, cookie = login.extractCookie(login_res.json())

    return access_key, cookie
