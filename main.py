from application.apps.app import sms_login, passport_login


if __name__ == '__main__':
    kwargs = {
        "versions": ("7.6.0", "7060200"),
        "system": ("SM-G955N", "9")
    }

    access_key, cookie = sms_login("区号", "手机号", **kwargs)
    # access_key, cookie = passport_login("用户名", "密码", **kwargs)

    print("access_key:", access_key)
    print("cookie:", cookie)
