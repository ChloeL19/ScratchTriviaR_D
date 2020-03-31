#The following code from: https://damyanon.net/getting-started-with-flask-on-cloud9/
#It's a simple hello world program
#First steps towards making api for neural network

import os
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import urlparse

# Neural net libraries
import numpy
# scipy.special for the sigmoid function expit()
import scipy.special
import matplotlib.pyplot

app = Flask(__name__)
CORS(app)

file_path = ""

def calc_length():
    training_data_file = open("mnist_train_100.csv", 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()
    
    all_values = training_data_list[0].split(',')
    row = numpy.asfarray(all_values[1:])
    file_length = len(row)
    return file_length


def summation(x, y):
    return int(x) + int(y)
# Could this be useful?
# self.send_header('Access-Control-Allow-Origin', '*')

# Neural Net
class neuralNetwork:
    
    # initialize the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where lik is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        # learning rate 
        self.lr = learningrate
        
        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)
        
        pass
    
    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layers
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)
        
        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        
        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))    
        pass
    
    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputs

# number of input, hidden, and ouptut nodes
# input_nodes = 784
# hidden_nodes = 200
# output_nodes = 10

# learning rate is 0.1
# learning_rate = 0.1

# create global variables that are updated by the "create nn" block
# these variables are then passed into the function in the training block
input_nodes = 0 
learning_rate = 0
hidden_nodes = 0
ouput_nodes = 0


#----------------Start of Function--------------
def train_neuralNet(input_nodes, hidden_nodes, output_nodes, learning_rate, file_path) :
    # def train_network(input, hidden, output)
    n = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)
    
    # load the mnist training data CSV file into a list
    training_data_file = open(file_path, 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()
    
    # load the testing data
    test_data_file = open("mnist_test.csv", 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()
    
    # train the neural network
    
    # epochs is the number of times the training data set is used for training
    epochs = 5
    
    for e in range(epochs):
        # go through all records in the training data set
        for record in training_data_list:
            # split the record by ',' commas
            all_values = record.split(',')
            # scale and shift the inputs
            inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            # create the target output values (all 0.01, except the desired output label which is 0.99)
            targets = numpy.zeros(output_nodes) + 0.01
            # all_values[0] is the target label for this record
            targets[int(all_values[0])] = 0.99
            n.train(inputs, targets)
            pass
        pass
    
    # go through all records in the training data set for record in training_data_list:
    for record in training_data_list:
        # split the record by ',' commas
        all_values = record.split(',')
        # scale and shift the inputs
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        # create the target output values (all 0.01, except the desired label which is 0.99)
        targets = numpy.zeros(output_nodes) + 0.01
        # all_values[0] is the target label for this record
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)
        pass
    
    # test the neural network
    
    # scorecard for how well the network performs, initially empty 
    scorecard = []
    
    # go through all the records in the test data set
    for record in test_data_list:
        # split the record by ',' commas
        all_values = record.split(',')
        # correct answer is first value
        correct_label = int(all_values[0])
        print(correct_label, "correct label")
        # scale and shift the inputs
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        # query the network
        outputs = n.query(inputs)
        # the index of the hightest value corresponds to the label
        label = numpy.argmax(outputs)
        print(label, "network's answer")
        if (label == correct_label):
            # network's answer matches correct answer, add 1 to scorecard
            scorecard.append(1)
        else:
            # network's answer doesn't match correct answer, add 0 to scorecard
            scorecard.append(0)
            pass
        pass
    
    # calculate the performance score, the fraction of correct answers
    scorecard_array = numpy.asfarray(scorecard)
    performance = scorecard_array.sum() / scorecard_array.size
    print("performance: {}".format(performance))
    return performance*100
#--------------End of Function

# def find_index(data, substring):
    # iterate though the data string
        # while 

# @app.route('/Hello_Test_2/api/v1.0/tasks', methods=['GET'])
# WORKING VERSION #1 (returns everything above as JSON data)
@app.route('/', methods=['GET', 'POST'])
def get_response():
    if request.method == 'GET' :
    # self.send_header('Access-Control-Allow-Origin', '*')
        file_length = calc_length()
        return jsonify({'nn_response': file_length})
    elif request.method == 'POST':
        request.get_data()
        print request.data
        return "hi!"
        # summation(request.data, )
@app.route('/put_data', methods=['PUT'])
def print_data() :
    global input_nodes, hidden_nodes, output_nodes, learning_rate 
    request.get_data()
    data  = request.data
    d = dict(urlparse.parse_qsl(data))
    print (d)
    print (d['hidden'])
    # update the values of the global input, hidden, and output variables
    input_nodes = float(d['inputs'])
    hidden_nodes = float(d['hidden'])
    output_nodes = float(d['outputs'])
    learning_rate = float(d['learning_rate'])
    # nn_response = train_neuralNet(float(d['inputs']), float(d['hidden']), float(d['outputs']), float(d['learning_rate']))
    # return (d['inputs'], d['hidden'], d['learning_rate'], d['outputs'])
    return jsonify({'response': "Neural net has been created!"})
    # return jsonify({'response': nn_response})
    
@app.route('/change_file_path', methods=['PUT'])
def change_file_path() :
    global file_path
    request.get_data()
    print(request.data)
    file_path = request.data
    efficacy = train_neuralNet(input_nodes, hidden_nodes, output_nodes, learning_rate, file_path)
    #  eventually going to call the train_neural_net function here using all of the parameters
    # eventually will return the neural network efficacy here
    return jsonify({'response': "Neural net efficacy: " + str(efficacy) + "%"})
    # filePath = 
    

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
