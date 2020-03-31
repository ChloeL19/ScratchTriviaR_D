#The following code from: https://damyanon.net/getting-started-with-flask-on-cloud9/
#It's a simple hello world program
#First steps towards making api for neural network

import os
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

nn_response = "hi!"
def summation(x, y):
    return x + y
# Could this be useful?
# self.send_header('Access-Control-Allow-Origin', '*')


# @app.route('/Hello_Test_2/api/v1.0/tasks', methods=['GET'])
# WORKING VERSION #1 (returns everything above as JSON data)
@app.route('/', methods=['GET', 'POST'])
def get_response():
    if request.method == 'GET' :
    # self.send_header('Access-Control-Allow-Origin', '*')
        return jsonify({'nn_response': nn_response})
    elif request.method == 'POST':
        request.get_data()
        print request.data
        return "hi!"
        # summation(request.data, )
    
# @app.route('/hello', methods=['POST'])
# def say_input():
#     request.get_data()
#     print request.data
#     return "yay it worked!"

#VERSION #2
# @app.route('/', methods=['GET'])
# def get_task():
#     task = [task for task in tasks if task['id'] == 1]
#     # if len(task) == 0:
#     #     abort(404)
#     return jsonify({'task': task[0]})

# if __name__ == '__main__':
#     # app.run(debug=True)
#     app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
