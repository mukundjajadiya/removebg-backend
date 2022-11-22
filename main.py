from flask import Flask, request, jsonify
from removeBG import removeImageBG
from flask_cors import CORS
import io
import base64

app = Flask(__name__)
CORS(app)
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "server is running..."})


@app.route("/upload", methods=["POST"])
def upload_file():
    # check if the post request has file
    if "file" not in request.files:
        resp = jsonify({"message": "No file/image  in the request"})
        resp.status_code = 400
        return resp

    file = request.files["file"]

    if file.filename == "":
        resp = jsonify({"message": "No file/image selected for uploading"})
        resp.status_code = 400
        return resp

    if file and allowed_file(file.filename):
        rawBytes = io.BytesIO()
        file.save(rawBytes)
        resultImageByte = removeImageBG(rawBytes.getvalue())
        imgBase64 = base64.b64encode(resultImageByte)
        return jsonify({"status": "200 OK", "image": str(imgBase64)})

    else:
        resp = jsonify({"message": "Allowed file types are png, jpg, jpeg"})
        resp.status_code = 400
        return resp


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
