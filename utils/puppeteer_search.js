const puppeteer = require('puppeteer');

const timeout = async(ms) => {
	return new Promise(resolve => setTimeout(resolve, ms));
}

/**
* Login into a google account, only works with headless mode off.
*
* Arguments:
* - page: Page where the login must be made.
* - email: The email of the account to login.
* - password: The password correspondent to the email.
*/
exports.loadCookies = async(page, file) => {
	const cookiesArr = require("./../cookies/" + file + ".json");
	for(let cookie of cookiesArr)
		await page.setCookie(cookie);
}

/**
* Returns a html with the resultant page of the google search of the query.
* 
* Arguments:
*  - query: Query to be made.
*/

exports.googleSearch = async (page, query) => {

	const baseLink = 'https://www.google.com.br/search?q=';

	await page.goto(baseLink + query);
		
	// Retorna txt com os links
	// Results é um string com todos os links concatenados
	var results = "";
	var string = await page.content();
	let retHtml = string;
	while (string.indexOf("<h3 class=\"r\"><a href=\"") != -1) {
		// first_index delimita a primeira porção e last_index a última
		// O resultado desejado se encontra entre esses índices
		var first_index = string.indexOf("<h3 class=\"r\"><a href=\"");
		var string = string.substring(first_index + 23, string.length);
		var last_index = string.indexOf("\"");
		var final_string = string.substring(0, last_index);
		results += final_string + '\n';
	}
	return {'txt' : results, 'html' : retHtml};

};

/**
* Opens google chrome 
* 
* Arguments:
*/
exports.newBrowser = async () => {
	return await puppeteer.launch({
		//headless: false
		// executablePath: '/usr/bin/google-chrome'
		args: ['--no-sandbox', '--disable-setuid-sandbox']
	});
}
