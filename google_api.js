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
	var fs = require('fs');
	query = query.replace(' ', '_')
	fs.writeFile("./" + query + ".json", result, err)
}