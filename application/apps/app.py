from geetest.geetest import GeeTest

from application.module.decoration import error

from application.net.login import SmsLogin, PassportLogin

from application.utils import urlQuerySplit


# @error
def passport_login(name: str, passport: str, versions, system) -> tuple[str, str]:
    login = PassportLogin(versions, system)
    res_web_key = login.web_key()
    if res_web_key.json()["code"] != 0:
        raise res_web_key.json()["message"]

    rkey = res_web_key.json()["data"]["key"]
    rhash = res_web_key.json()["data"]["hash"]

    res_login = login.oauth2_login(name, passport, rkey, rhash)

    if res_login.json()["code"] != 0:
        raise res_web_key.json()["message"]

    status_code = res_login.json()["data"]["status"]
    res_login_data = res_login.json()["data"]
    if status_code != 0:
        print(res_login_data["message"])

        verify_url = res_login.json()["data"]["url"]
        verify_query = urlQuerySplit(verify_url)
        tmp_code = verify_query["tmp_token"]
        verify_query.update({"tmp_code": tmp_code})
        verify_query.pop("tmp_token", None)

        info_res = login.user_info(verify_query["tmp_code"])
        if info_res.json()["code"] != 0:
            raise info_res.json()["message"]

        captcha_pre_res = login.captcha_pre()
        if captcha_pre_res.json()["code"] != 0:
            raise captcha_pre_res.json()["message"]

        gee_dict: dict = captcha_pre_res.json()["data"]
        gee_dict.pop("recaptcha_type", None)

        print("完成人机验证以继续")

        gee = GeeTest(gee_dict["gee_gt"], gee_dict["gee_challenge"])
        gee_dict.update(gee.waitFinishing(1))

        gee_data = {
            "gee_challenge": gee_dict["gee_challenge"],
            "gee_seccode": gee_dict["geetest_seccode"],
            "gee_validate": gee_dict["geetest_validate"],
            "recaptcha_token": gee_dict["recaptcha_token"]
        }

        sms_send_res = login.sms_send(verify_query["tmp_code"], **gee_data)

        if sms_send_res.json()["code"] != 0:
            raise sms_send_res.json()["message"]

        captcha_key = sms_send_res.json()["data"]["captcha_key"]

        tel_text = info_res.json()["data"]["account_info"]["hide_tel"]
        print(f"验证码已发送到[{tel_text}]")

        code = None

        while not code:
            verify_code = input("输入验证码:")

            login_res = login.tel_verify(captcha_key, verify_code, **verify_query)
            if login_res.json()["code"] != 0:
                print(login_res.json()["message"])
                continue

            code = login_res.json()["data"]["code"]

        res_login = login.oauth2_access_token(code)
        if res_login.json()["code"] != 0:
            raise res_login.json()["message"]

    access_key, cookie = login.extractCookie(res_login.json())
    return access_key, cookie


@error
def sms_login(cid: int | str, tel: int | str, versions, system) -> tuple[str, str]:
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
