import boto3
import awsgi
import random
from faker import Faker  

from flask import Flask, jsonify

app = Flask(__name__)
dynamoDB = boto3.resource('dynamodb')
fake = Faker()

@app.route('/deportistas-lista', methods=['GET'])
def deportistas_lista():
    return jsonify(status= 200, message= 'Echo: GET')

@app.route('/deportistas-crear', methods=['POST'])
def deportistas_crear():
    params = {
        "TableName": "deportistas",
        "Item": {
            "identificacion": {
                "S": f"Deportista-{fake.random_int(min=1000000, max=2000000)}"
            },
            "nombre": {
                "S": fake.first_name()
            },
            "apellido": {
                "S": fake.last_name()
            },
            "edad": {
                "N": fake.random_int(min=18, max=40)
            },
            "deporte": {
                "S": fake.random_element(elements=('Futbol', 'Baloncesto', 'Voleibol', 'Natacion', 'Atletismo' 'Ciclismo'))
            }
        }
    }
    dynamoDB.put_item(**params)
    
    data = dynamoDB.put_item(**params)
    print("Respuesta de DynamoDB: ", data)
    return {
            'statusCode': 200,
            'body': data
        }

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

