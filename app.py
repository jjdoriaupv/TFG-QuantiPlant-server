from flask import Flask, request, send_from_directory, jsonify
from datetime import datetime
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files.get('image')
    if not file:
        return 'No image received', 400

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"photo_{timestamp}.jpg"
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    print(f"[+] Foto recibida y guardada como {filename}")
    return 'OK', 200

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/list')
def list_images():
    files = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)
    return jsonify(files)

@app.route('/uploads/<filename>', methods=['DELETE'])
def delete_image(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(path):
        os.remove(path)
        return 'Deleted', 200
    else:
        return 'Not Found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
