from flask import Blueprint, render_template, request, jsonify, send_file
import os
from .utils import model_predict
import uuid

home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')


UPLOAD_DIR = "./app/static/uploads/images/"


@home.route('/', methods=['GET'])
@home.route('/home', methods=['GET'])
def index():
    if request.args.get('predict'):
        predict = request.args.get('predict')
        image_name = request.args.get('image_name')
        image_url = request.url_root + f'/image/{image_name}'
        return render_template('view.html', predict=predict, image_url=image_url)
    return render_template('index.html')


@home.route('/predict', methods=['POST'])
def predict():
    # get the image file from the request
    image_file = request.files.get('image')

    print(image_file)

    if image_file:
        image_name = f"{uuid.uuid4()}.jpg"
        image_path = os.path.join(UPLOAD_DIR, image_name)
        # save the image file to disk
        image_file.save(image_path)

        get_predict = model_predict(image_path=image_path)

        # return a response
        return jsonify({
            'predict': get_predict,
            'image_name': image_name
        })
    else:
        return "error", 400


@home.route('/image/<image_name>', methods=['GET'])
def image(image_name):

    image_path = os.path.join(UPLOAD_DIR, image_name).replace('/app', '')

    return send_file(image_path, mimetype='image/jpg'), 200
