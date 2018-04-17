var googleAPI  = require('./google_api')
var fsmod = require('fs')
var dateLog = new Date()
var persist = require('./persistence_module')(
	dateLog.toLocaleDateString() + '_' + dateLog.toLocaleTimeString() + '_api_log.txt');

var filename = 'listaat' //bloco para decidir nome entre listaat ou listaat.txt. motivo: compatibilidade entre sistemas
if(fsmod.existsSync(__dirname + '/' + filename + '.txt')){ //se existe .txt, use
  filename += '.txt'
}
else if(!(fsmod.existsSync(__dirname + '/' + filename))){ //se nao existe nenhum, desista e avise
  console.log('no input file/nao tem entrada')
  return
}
var lineReader = require('readline').createInterface({
  input: fsmod.createReadStream(__dirname + '/' + filename)
});



lineReader.on('line', function (line) { //para cara linha de listaat, uma busca no google
  var result = googleAPI.retrieveLinks(line, "005182128650059414634%3Acpbzek4imty", "AIzaSyC-6UytV9d7x16YvRzM1j-gdy1W3yTV-9w", 10);
  if(line && result) {
    // Apenas escreve se linha e resultado são não-nulos
    persist.write(line + '\n');

    result.forEach((currentValue) => {
      persist.write('\t*' + currentValue["title"] + '\n');
      persist.write('\t\t' + currentValue["link"] + '\n');
    })
  }
  
});