var google  = require('google')
var fsmod   = require('fs')
var persist = require('./persistence_module');

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

  google.resultsPerPage = 25
  var nextCounter = 0

  google(line, function (err, res){
    // Escreve a palavra-chave
    persist.write(line + '\n');
    if (err) {
      console.error(err)
      return
    }


    for (var i = 0; i < res.links.length; ++i) {
      var link = res.links[i]
      // Ignora links nulos
      if (link.href == null) { continue; }
      // Persiste os links no arquivo texto
      persist.write('\t' + link.href + '\n');
      persist.write('\t' + link.title + '\n');
      //persist.write('\t' + link.description + '\n');
      console.log(link.href)      
    }

    if (nextCounter < 4) {
      nextCounter += 1
      if (res.next) res.next()
    }
  })
});