module.exports = (fileName) => {
	var outputFolder = 'resultados';
	var dirName = __dirname + '/' + outputFolder;

	var module = {};

	var fs = require('fs');
	if(!fs.existsSync(dirName)){
    	fs.mkdirSync(dirName, 0766, function(err){
        	if(err){
            	console.log(err);
            	response.send("diretorio nao pode ser criado.\n");
        	}
    	});
	}

	// O proposito deste modulo eh poder trocar a forma 
	// de saida do programa sem alterar sua 'main'
	var log_writter = fs.createWriteStream(outputFolder + '/' + fileName, {
	  flags: 'w'
	});

	module.write = function (string) {
		log_writter.write(string);
	}

	return module;
}
