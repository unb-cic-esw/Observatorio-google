var fs = require('fs');

// O proposito deste modulo eh poder trocar a forma 
// de saida do programa sem alterar sua 'main'
var log_writter = fs.createWriteStream('log.txt', {
  flags: 'w'
  // Usa-se sempre em modo 'w'(Re-escrevendo o arquivo)
});

exports.write = function (string) {
	log_writter.write(string);	
}