import boto3
import awsgi
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/deportistas', methods=['GET'])
def deportistas():
    return jsonify(status= 200, message= 'Echo: GET')

@app.route('/deportistas', methods=['POST'])
def deportistas():
    return jsonify(status= 200, message= 'Echo: POST')

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

