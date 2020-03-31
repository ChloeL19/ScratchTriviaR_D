
// THIS CODE WORKS!!!!!!!! YAYAYAYAYAY
// allows user to update the parameters of the neural network (i.e. the number of input nodes, hidden nodes, output nodes,
// and the learning rate




(function(ext) {
    // Cleanup function when the extension is unloaded
    ext._shutdown = function() {};

    // Status reporting code
    // Use this to report missing hardware, plugin or unsupported browser
    ext._getStatus = function() {
        return {status: 2, msg: 'Ready'};
    };

    ext.hello_world = function(callback) {
        // var hello_word = -1;
        // connect to api and return hello world
        
        // return "hi!";
        
        $.ajax({
              url: 'http://python-projects-chloerl.c9users.io:8080/',
              type: 'GET',
              dataType: 'json',
              crossDomain: true,
              success: function( hello_data ) {
                console.log("here");
                var hello_word = hello_data.nn_response;
                console.log(hello_word);
                callback(hello_word);
              }
         });
    };
    
    ext.get_config = function(inputs, hidden, outputs, learning_rate, callback) {
        // compile the inputs into an array
        send_data = [inputs, hidden, outputs, learning_rate]
        test_data = [1, 2, 3, 4]
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
            ['R', 'hello!', 'hello_world'],
            ['w', 'Creat neural network with %s input nodes, %s hidden nodes, %s output nodes, and a %s learning rate', 'get_config'],
            ['r', 'Response', 'get_response']
        ]
    };

    // Register the extension
    ScratchExtensions.register('Sample extension', descriptor, ext);
})({});
