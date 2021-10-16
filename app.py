import hashlib
import io

import imagehash
from flask import Flask, request
from PIL import Image

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

    img = Image.open(io.BytesIO(data))
    return {
        "sha1": hashObjs["sha1"].hexdigest(),
        "sha256": hashObjs["sha256"].hexdigest(),
        "md5": hashObjs["md5"].hexdigest(),
        "average_hash": imagehash.average_hash(img).__str__(),
        "color_hash": imagehash.colorhash(img).__str__(),
        "phash": imagehash.phash(img).__str__(),
        "dhash": imagehash.dhash(img).__str__(),
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)