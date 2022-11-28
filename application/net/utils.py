from application.net.session import Session
from application.config import default_net_config


def get_versions(mod: str = "android") -> tuple[str, str]:
    """ 获取[版本号]和[版本名] """
    url = f"https://app.bilibili.com/x/v2/version"
    with Session(**default_net_config) as session:
        res = session.request("GET", url, params={"mobi_app": mod})
    code = str(res.json()["data"][0]["build"])
    name = str(res.json()["data"][0]["version"])
    return code, name
