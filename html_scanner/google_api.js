const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest


/**
 * Extract the data from result JSON.
 */
const retrieveLinks = function(query, customsearchId, APIkey, num){ //monta a mensagem url da pesquisa a ser feita, extrai os dados que queremos do JSON resultante
	var results = httpGet("https://www.googleapis.com/customsearch/v1?q=" +
						 query + "&cx=" + customsearchId + "&key=" +
						 APIkey + "&cr=countryBR&num=" + num)
	results = JSON.parse(results)	
	var resultLinks = []
	try{
		for(var result of results["items"])		
			resultLinks.push({"title": result["title"], "link": result["link"]})
	}
	catch(e) {
		console.err(e)
		resultLinks = []
	}
	
	return resultLinks;
}

/**
 * Get the query data and returns result JSON.
 */
function httpGet(theUrl) {
	const xmlHttp = new XMLHttpRequest()
	xmlHttp.open("GET", theUrl, false)
	xmlHttp.send(null)
	return xmlHttp.responseText
}

module.exports = retrieveLinks