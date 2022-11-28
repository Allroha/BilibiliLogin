from application.module.decoration import application_error

from application.utils import urlQuerySplit

from urllib.parse import urlsplit
from selenium import webdriver
import base64
import json
import time
import os


class GeeTest(object):
    @application_error
    def __init__(self, gt, challenge):
        """ 还得是selenium """
        super(GeeTest, self).__init__()

        self.driver = webdriver.Chrome(os.path.abspath("geetest/chromedriver.exe"))
        gee_html = os.path.abspath("./geetest/template/index.html")
        self.driver.get(gee_html + f"?gt={gt}&challenge={challenge}")

    @application_error
    def waitFinishing(self, time_sleep: int | float = 3) -> dict:
        """ 获取到极验证数据 """
        _, name = os.path.split(urlsplit(self.driver.current_url).path)
        while name != "finish.html":
            _, name = os.path.split(urlsplit(self.driver.current_url).path)
            time.sleep(time_sleep)
        query_dict = urlQuerySplit(self.driver.current_url)
        self.driver.quit()
        debase64 = base64.b64decode(query_dict["data"]).decode()
        return json.loads(debase64)
