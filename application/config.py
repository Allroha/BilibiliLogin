from application.utils import reader

default_net_config = reader("./settings/net/default.json")
login_config = reader("./settings/net/login.json")

main_button_settings = reader("./settings/controls/main/button.json")

setting_label_settings = reader("./settings/controls/setting/label.json")
setting_entry_settings = reader("./settings/controls/setting/entry.json")
setting_button_settings = reader("./settings/controls/setting/button.json")

sms_login_entry_settings = reader("./settings/controls/sms_login/entry.json")
sms_login_label_settings = reader("./settings/controls/sms_login/label.json")
sms_login_button_settings = reader("./settings/controls/sms_login/button.json")
