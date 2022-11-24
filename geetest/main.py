from flask import Flask, render_template, request, jsonify

import json
import os

template = os.path.abspath("./template")
static = os.path.abspath("./static")

app = Flask(__name__, template_folder=template, static_folder=static)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "GET":
        login_id = request.args.get("id")
        if not os.path.exists(f"./{login_id}.json"):
            return jsonify({"code": 1, "data": None})
        with open(f"./{login_id}.json", "r", encoding="utf-8") as f:
            data = json.loads(f.read())
        f.close()
        return jsonify({"code": 0, "data": data})
    else:
        login_id = request.args.get("id")
        with open(f"./{login_id}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(request.get_json()))
        f.close()
        return jsonify({"code": 0, "message": None})


app.run("127.0.0.1", 5000)
