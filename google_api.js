function err(err){ //tratamento de erros: informar no terminal
	if(err)	return console.log(err);
}

function httpGet(theUrl){ //recupera os dados da query e retorna o JSON de resultado
	var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest
	var xmlHttp = new XMLHttpRequest()
	xmlHttp.open("GET", theUrl, false) // false for synchronous request
	xmlHttp.send(null)
	return xmlHttp.responseText
}

exports.retrieveLinks = function(query, customsearchId, APIkey, num){ //monta a mensagem url da pesquisa a ser feita, extrai os dados que queremos do JSON resultante
	var result = httpGet("https://www.googleapis.com/customsearch/v1?q=" + query + "&cx=" + customsearchId + "&key=" + APIkey + "&cr=countryBR&num=" + num)
	result = JSON.parse(result)	
	var resultLinks = []
	try{
		for(var i of result["items"])
			resultLinks.push({"title" : i["title"], "link" : i["link"]})
	}
	catch(e) {
		// Captura se o link retornado for nulo(Type Error)
		console.log("ex")
		resultLinks = []
	}
	// Caso tenha problema retorna apenas um vetor nulo
	return resultLinks;
}