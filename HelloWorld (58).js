// make some sort of xhr call to python api
// store in the variable data
// log that dat


// console.log(data);





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

    ext.get_response = function() {
        return test;
    }

    // Block and block menu descriptions
    var descriptor = {
        blocks: [
            ['R', 'Length of dataset', 'length_of'],
            ['w', 'Creat neural network with %s input nodes, %s hidden nodes, %s output nodes, and a %s learning rate', 'get_config'],
            ['r', 'Response', 'get_response']
        ]
    };

    // Register the extension
    ScratchExtensions.register('Sample extension', descriptor, ext);
})({});