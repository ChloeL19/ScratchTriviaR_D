(function(ext) {
    // Cleanup function when the extension is unloaded
    ext._shutdown = function() {};

    // Status reporting code
    // Use this to report missing hardware, plugin or unsupported browser
    ext._getStatus = function() {
        return {status: 2, msg: 'Ready'};
    };

    ext.get_quest = function(callback) {
        // Make an AJAX call to the jService API
        $.ajax({
              url: 'http://jservice.io/api/random',
              dataType: 'json',
              success: function( random_question ) {
                  // Got the data - parse it and return the question and the answer
                  questionWanted = random_question[0].question;
			answerWanted = random_question[0].answer;
		
                  callback(questionWanted);
			//callback(answerWanted);


              }
        });
    };

	ext.get_ans = function() {
		return answerWanted;
	};
	

    // Block and block menu descriptions
    var descriptor = {
        blocks: [
            ['R', 'get random', 'get_quest', 'question'],
		['r', 'the answer', 'get_ans'],
        ]
    };

    // Register the extension
    ScratchExtensions.register('Trivia extension', descriptor, ext);
})({});