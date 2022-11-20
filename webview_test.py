

import webview
import threading
import time
from flask import Flask, render_template, redirect, request


def flask_app(tem, sta, gee_gt, gee_challenge):
    app = Flask(__name__, template_folder=tem, static_folder=sta)

    @app.route("/")
    def index():
        if len(request.args) == 0:
            return redirect(f"/?gt={gee_gt}&challenge={gee_challenge}")
        return render_template("index.html")

    return app


app_url = flask_app(
    './web/geetest_validator/template', './web/geetest_validator/static',
    "ac597a4506fee079629df5d8b66dd4fe", "4e20a40c66305feb7ea468ed59fd2376"
)


def quit_window():
    while True:
        time.sleep(3)
        print(web.get_current_url())


web = webview.create_window("test", url=app_url)


t = threading.Thread(target=quit_window)
t.start()

webview.start()
