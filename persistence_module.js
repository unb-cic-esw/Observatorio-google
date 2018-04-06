module.exports = (fileName) => {

	var module = {};

	var fs = require('fs');

	// O proposito deste modulo eh poder trocar a forma 
	// de saida do programa sem alterar sua 'main'
	var log_writter = fs.createWriteStream(fileName, {
	  flags: 'w'
	});

	module.write = function (string) {
		log_writter.write(string);
	}

	return module;
}
