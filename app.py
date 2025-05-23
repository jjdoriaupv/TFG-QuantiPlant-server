from flask import Flask, request
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
