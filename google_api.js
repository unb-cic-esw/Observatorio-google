function err(err){
	if(err)	return console.log(err);
}

function httpGet(theUrl){
	var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest
	var xmlHttp = new XMLHttpRequest()
	xmlHttp.open("GET", theUrl, false) // false for synchronous request
	xmlHttp.send(null)
	return xmlHttp.responseText
}

exports.retrieveLinks = function(query, customsearchId, APIkey){
	var result = httpGet("https://www.googleapis.com/customsearch/v1?q=" + query + "&cx=" + customsearchId + "&key=" + APIkey + "&cr=countryBR")
	result = JSON.parse(result)
	var resultLinks = []
	for(var i = 0; i < 10; i++)
		resultLinks.push(result["items"][i]["link"])
	console.log(resultLinks)
}