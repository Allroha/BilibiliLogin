import httpx


class Session(httpx.Client):
    def __init__(self, **kwargs):
        super(Session, self).__init__(
            trust_env=kwargs.get("trust_env", False),
            proxies=kwargs.get("proxies", None),
            timeout=float(kwargs.get("timeout", 5))
        )
        self.headers.update(kwargs.get("headers", dict()))
