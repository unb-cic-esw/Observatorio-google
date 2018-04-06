var googleAPI  = require('./google_api')
var fsmod = require('fs')
var persist = require('./persistence_module')(
	'resultados/' + new Date().toLocaleDateString() + '_api_log.txt');

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
  var result = googleAPI.retrieveLinks(line, "005182128650059414634%3Acpbzek4imty", "AIzaSyC-6UytV9d7x16YvRzM1j-gdy1W3yTV-9w");
  persist.write(line + '\n');
  result.forEach((currentValue) => {
  	persist.write('\t' + currentValue + '\n');
  })
});