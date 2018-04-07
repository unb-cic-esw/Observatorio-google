var google  = require('google')
var fsmod   = require('fs')
var dateLog = new Date()
var persist = require('./persistence_module')(
  dateLog.toLocaleDateString() + '_' + dateLog.toLocaleTimeString() + '_scrapper_log.txt');

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

  google.resultsPerPage = 15
  var nextCounter = 0
  //console.error(line);  
  google(line, function (err, res){ // busca uma linha
    // Escreve a palavra-chave    
    persist.write(line + '\n');
    if (err) { //retorna em caso de erro (exemplo, google bloqueou a pesquisa)
      console.error(err);
      return
    }

    var totalLinks = 0;
    for (var i = 0; (totalLinks < 10) && (i < res.links.length); ++i) { //coleta os 10 primeiros links do resultado
      var link = res.links[i]
      // Ignora links nulos
      if (link.href == null) {
        continue; 
      }
      // Persiste os links no arquivo texto
      persist.write('\t' + link.href + '\n');
      totalLinks += 1;
      //persist.write('\t' + link.title + '\n');
      //persist.write('\t' + link.description + '\n'); 
    }
  })
});