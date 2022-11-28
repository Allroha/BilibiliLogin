from application.module.decoration import (
    application_error, application_thread
)

from application.apps.windows.setting import SettingDeviceWindow

from application.utils import get_all_value

from application.apps.windows.login import (
    SmsLoginWindow, PassportLoginWindow
)


@application_thread
@application_error
def setting_device(master) -> None:
    SettingDeviceWindow(master)


@application_thread
@application_error
def sms_login(master) -> None:
    device = get_all_value(master, "Device_", [])
    versions = (device["VersionName"], device["VersionCode"])
    system = (device["AndroidModel"], device["AndroidBuild"])

    SmsLoginWindow(versions, system, device["Buvid"])


@application_thread
@application_error
def passwort_login(master) -> None:
    PassportLoginWindow(master)
