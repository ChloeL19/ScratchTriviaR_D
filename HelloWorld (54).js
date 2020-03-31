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

    ext.hello_world = function() {
        // var hello_word = -1;
        // connect to api and return hello world
        
        // return "hi!";
        
        $.ajax({
              url: 'http://python-projects-chloerl.c9users.io:8080/',
              dataType: 'json',
              success: function( hello_data ) {
                console.log("here");
                var hello_word = JSON.parse(hello_data);
                return hello_word.nn_response;
              }
         });
    };
    
    // Block and block menu descriptions
    var descriptor = {
        blocks: [
            ['R', 'hello!', 'hello_world']
        ]
    };

    // Register the extension
    ScratchExtensions.register('Sample extension', descriptor, ext);
})({});