import os
import cv2
import config
from datetime import datetime
import numpy as np
from flask import Flask, jsonify
import requests

app = Flask(__name__)

def create_timestamp():
    now = datetime.now()
    now = now.strftime("%Y-%m-%d_%H-%M-%S")
    print(now)
    return now

@app.route('/monitor', methods=['GET'])
def monitor():
    response = requests.get(config.api_camera_service)
    #https://brightdata.com/faqs/json/extract-json-response-python
    timestamp = create_timestamp()
    img = response.json()["img"]
    data = {"img":img}
    response = requests.post(config.api_ai_service_obj, json=data)
    response = response.json()
    ai_img = np.array(response["ai"]).astype(np.uint8)
    raw_img = np.array(img).astype(np.uint8)
    cv2.imwrite(os.path.join(config.path_save_raw_dir,f"{timestamp}.png"), raw_img)
    cv2.imwrite(os.path.join(config.path_save_ai_dir, f"{timestamp}.png"), ai_img)
    response["raw"] = raw_img.tolist()
    return jsonify(response), 200


@app.route('/test_ai', methods=['GET'])
def test_ai():
    response = requests.get("http://localhost:6665/strawberry") 
    timestamp = create_timestamp()
    img = response.json()["img"]
    data = {"img":img}
    response = requests.post(config.api_ai_service_obj, json=data)
    response = response.json()
    ai_img = np.array(response["ai"]).astype(np.uint8)
    raw_img = np.array(img).astype(np.uint8)
    cv2.imwrite(os.path.join(config.path_save_raw_dir, f"{timestamp}.png"), raw_img)
    cv2.imwrite(os.path.join(config.path_save_ai_dir, f"{timestamp}.png"), ai_img)
    response["raw"] = raw_img.tolist()
    return jsonify(response), 200


if __name__ == "__main__":
    config.reload_config()
    app.run(debug=True, port=8501)
