// functions to make
// 1. choose a dataset function
// 2. upload test data function
// Create graph--automatically takes a list of data and creates a graph on the scratch stage



(function(ext) {
    // Cleanup function when the extension is unloaded
    ext._shutdown = function() {};

    // Status reporting code
    // Use this to report missing hardware, plugin or unsupported browser
    ext._getStatus = function() {
        return {status: 2, msg: 'Ready'};
    };

    ext.length_of = function(callback) {
        // var hello_word = -1;
        // connect to api and return hello world
        
        // return "hi!";
        
        $.ajax({
              url: 'http://python-projects-chloerl.c9users.io:8080/',
              type: 'GET',
              dataType: 'json',
              crossDomain: true,
              success: function( length_response ) {
                console.log("here");
                var length_of_file = length_response.nn_response;
                console.log(length_of_file);
                callback(length_of_file);
              }
         });
    };
    
    ext.get_config = function(inputs, hidden, outputs, learning_rate, callback) {
        // updating data on the server
        $.ajax({
              url: 'http://python-projects-chloerl.c9users.io:8080/put_data',
              type: 'PUT',
              data: {
                inputs,
                hidden,
                outputs,
                learning_rate
              },
              dataType: 'json',
              crossDomain: true,
              success: function( func_data ) {
                console.log("received data from put request");
                test = func_data.response;
                console.log(typeof(test));
                callback(test);
              }
         });
    };

    // ext.get_response = function() {
    //     // Will need to return a different variable--the variable returned by the query function
    //     return test;
    // };

     ext.get_efficacy = function() {
        // Returns efficacy of the neural net after training
        // for now it just reports whether or not neural net has been created successfully
        // eventually will need to return 'state'
        return state;
    };

    ext.mnist_data = function() {
        return "mnist_train_100.csv";
    };

    ext.train_with = function(data_name, callback) {
        // alert the user if there's no inputted dataset
        if (data_name == "")
        {
            return "Please input a valid dataset name."
        }
        $.ajax({
              url: 'http://python-projects-chloerl.c9users.io:8080/change_file_path',
              type: 'PUT',
              data: data_name,
              dataType: 'json',
              crossDomain: true,
              success: function( neural_response ) {
                console.log("received data from put request");
                state = neural_response.response;
                console.log(typeof(state));
                callback(state);
              }
         });
    };

    // ext.list_test = function(my_list) {
    //     return "mnist_train_100.csv";
    // };

    // Block and block menu descriptions
    var descriptor = {
        blocks: [
            ['R', 'Length of dataset', 'length_of'],
            ['w', 'Creat neural network with %s input nodes, %s hidden nodes, %s output nodes, and a %s learning rate', 'get_config'],
            ['r', 'efficacy', 'get_efficacy'],
            ['r', 'MNIST training data set', 'mnist_data'],
            ['w', 'Train the neural net with %s', 'train_with']
        ]
    };

    // Register the extension
    ScratchExtensions.register('Sample extension', descriptor, ext);
})({});