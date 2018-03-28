var google = require('google')

google.resultsPerPage = 5
var nextCounter = 0

var pages = 1
google('node.js best practices', function (err, res){
  if (err) console.error(err)

  for (var i = 0; i < res.links.length; ++i) {
    var link = res.links[i];
    // console.log(link.title + ' - ' + link.href)
    // console.log(link.description + "\n")
    console.log(link.href)
  }

  if (nextCounter < pages-1) {
    nextCounter += 1
    if (res.next) res.next()
  }
})