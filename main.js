var google = require('google')
var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream(__dirname + '/' + 'listaat')//change path to a proper one later
});

lineReader.on('line', function (line) {

  google.resultsPerPage = 25
  var nextCounter = 0

  google(line, function (err, res){
    if (err) console.error(err)

    for (var i = 0; i < res.links.length; ++i) {
      var link = res.links[i];
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