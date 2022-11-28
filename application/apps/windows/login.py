from application.apps.windows.app import TopWindow

from application.module.controls import (
    TkinterLabel, TkinterEntry, TkinterButton
)

from application.config import (
    sms_login_label_settings,
    sms_login_entry_settings,
    sms_login_button_settings
)

from application.net.login import SmsLogin

from application.module.command.sms_login import (
    send_verify_code, login_login
)

from functools import partial


sms_login_func = [
    ("send_verify_code", send_verify_code),
    ("login_login", login_login)
]


class SmsLoginWindow(TopWindow):
    def __init__(self, versions, system, buvid):
        super(SmsLoginWindow, self).__init__("短信登陆", "300x130")

        self.login = SmsLogin(versions, system, buvid)

        for label_config in sms_login_label_settings:
            TkinterLabel(self, label_config)

        for name, entry_config in sms_login_entry_settings.items():
            self[f"{name}_entry"] = TkinterEntry(self, entry_config)

        for name, func in sms_login_func:
            config = sms_login_button_settings[name]
            TkinterButton(self, config, partial(func, self))

        self.captcha_key = None
        self.buvid = buvid


class PassportLoginWindow(TopWindow):
    def __init__(self, master):
        super(PassportLoginWindow, self).__init__("账密登陆", "")
