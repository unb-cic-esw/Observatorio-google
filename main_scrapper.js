var google  = require('google')
var fsmod   = require('fs')
var persist = require('./persistence_module')(
  'resultados/' + new Date().toLocaleDateString() + '_scrapper_log.txt');

var filename = 'listaat'
if(fsmod.existsSync(__dirname + '/' + filename + '.txt')){
  filename += '.txt'
}
else if(!(fsmod.existsSync(__dirname + '/' + filename))){
  console.log('no input file/nao tem entrada')
  return
}
var lineReader = require('readline').createInterface({
  input: fsmod.createReadStream(__dirname + '/' + filename)//change path to a proper one later
});

lineReader.on('line', function (line) {

  google.resultsPerPage = 15
  var nextCounter = 0
  //console.error(line);  
  google(line, function (err, res){
    // Escreve a palavra-chave    
    persist.write(line + '\n');
    if (err) {
      console.error(err);
      return
    }

    var totalLinks = 0;
    for (var i = 0; (totalLinks < 10) && (i < res.links.length); ++i) {
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