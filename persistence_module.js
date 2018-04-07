module.exports = (fileName) => {
	var outputFolder = 'resultados'; //para facilitar mudar o path de resposta
	var dirName = __dirname + '/' + outputFolder; //para verificar de existe

	var module = {};

	var fs = require('fs');
	if(!fs.existsSync(dirName)){ //verifica a existencia da pasta de respostas
    	fs.mkdirSync(dirName, 0766, function(err){ //se nao existe, cria a pasta
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
