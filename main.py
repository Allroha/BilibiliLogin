from application.apps.app import sms

if __name__ == '__main__':
    access_key, cookie = sms(86, 2233, ("7.6.0", "7060200"), ("SM-G955N", "9"))
    print("access_key:", access_key)
    print("cookie:", cookie)
