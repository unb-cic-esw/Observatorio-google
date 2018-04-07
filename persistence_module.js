module.exports = (fileName) => {
	var dirName = __dirname + '/resultados';

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
	var log_writter = fs.createWriteStream(fileName, {
	  flags: 'w'
	});

	module.write = function (string) {
		log_writter.write(string);
	}

	return module;
}
