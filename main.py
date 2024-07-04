from flask import Flask, request, jsonify
from flask_cors import CORS
from encrypt import encrypt

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>SafeEncrypted</p>"


@app.route("/encrypted", methods=["POST"])
def encrypted():
    if "files[]" not in request.files:
        return jsonify({"error": "No files part"}), 400

    files = request.files.getlist("files[]")
    print(len(files))

    # Guarda los archivos en memoria
    files_data = {}
    for file in files:
        file_data = file.read()
        files_data[file.filename] = file_data

    key, encrypted_files = encrypt(files_data)

    response = {
        "key": key,
        "files": {
            filename: encrypted_file
            for filename, encrypted_file in encrypted_files.items()
        },
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
