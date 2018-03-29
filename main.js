var google = require('google')
var fsmod = require('fs')

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
    if (err) {
      console.error(err)
      return
    }


    for (var i = 0; i < res.links.length; ++i) {
      var link = res.links[i]
      console.log(link.href)
      console.log(link.title)
      console.log(link.description + "\n")
    }

    if (nextCounter < 4) {
      nextCounter += 1
      if (res.next) res.next()
    }
  })
});