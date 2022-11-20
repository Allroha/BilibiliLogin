import hashlib
import time

import requests
from urllib.parse import urlencode
from urllib.parse import quote


session = requests.Session()
session.headers.update({"Accept-Encoding": "gzip"})
session.headers.update({"Buvid": "XY30A9D303849C51D0D6F863F84A269E887E8"})
session.headers.update({"env": "prod"})
session.headers.update({"APP-KEY": "android"})
session.headers.update({"User-Agent": "Mozilla/5.0 BiliDroid/7.6.0 (bbcallen@gmail.com) os/android model/SM-G955N mobi_app/android build/7060200 channel/alifenfa innerVer/7060200 osVer/9 network/2"})
session.headers.update({"x-bili-trace-id": "e604d67d2efb03214bad66932a637983:4bad66932a637983:0:0"})
session.headers.update({"x-bili-aurora-eid": ""})
session.headers.update({"x-bili-mid": ""})
session.headers.update({"x-bili-aurora-zone": ""})
session.headers.update({"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"})
session.headers.update({"Host": "passport.bilibili.com"})
session.headers.update({"Connection": "Keep-Alive"})


# Content-Length

tel = ""

__statistics = '{"appId":1,"platform":3,"version":"7.6.0","abtest":""}'
data = {
    "appkey": "783bbb7264451d82",
    "build": "7060200",
    "buvid": "XY30A9D303849C51D0D6F863F84A269E887E8",
    "c_locale": "zh_CN",
    "channel": "alifenfa",
    "cid": "86",
    "device_tourist_id": "20605230970864",
    "disable_rcmd": "0",
    "local_id": "XY30A9D303849C51D0D6F863F84A269E887E8",
    "login_session_id": "e4413e7ce4d97ed505b30fb8d9ab6585",
    "mobi_app": "android",
    "platform": "android",
    "s_locale": "zh_CN",
    "spm_id": "main.my-information.my-login.0",
    "statistics": quote(__statistics),
    "tel": tel
}
data.update({"ts": str(round(time.time()))})

ddd = urlencode(data)
md5_h = hashlib.md5()
md5_h.update((ddd + "2653583c8873dea268ab9386918b1d65").encode())
form_data = ddd + "&sign=" + md5_h.hexdigest()

res = session.post("https://passport.bilibili.com/x/passport-login/sms/send", data=form_data)
print(res.text)
