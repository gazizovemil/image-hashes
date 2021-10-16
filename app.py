import hashlib

from flask import Flask, request

app = Flask(__name__)


@app.route("/up")
def upCheck():
    return {"message": "up"}


@app.route("/image", methods=["POST"])
def image():
    data = request.get_data()
    hashObjs = {
        "sha1": hashlib.sha1(),
        "sha256": hashlib.sha256(),
        "md5": hashlib.md5(),
    }
    for _, val in hashObjs.items():
        val.update(data)

    return {
        "sha1": hashObjs["sha1"].hexdigest(),
        "sha256": hashObjs["sha256"].hexdigest(),
        "md5": hashObjs["md5"].hexdigest(),
    }
