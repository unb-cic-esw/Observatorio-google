const puppeteer = require('puppeteer');
const date = new Date();
const persistence = require('../persistence/index')();

const currentDate = date.toLocaleDateString().replace(/\//g, '-');
const directory = "./resultados/";

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
exports.loginGoogle = async(page, email, password) => {
	await page.goto('https://accounts.google.com/ServiceLogin')
	await timeout(3000);
	await page.click('#identifierId');
	await page.keyboard.type(email);
	await page.click('#identifierNext');
	await timeout(3000);
	await page.click('#password');
	await page.keyboard.type(password);
	await page.click('#passwordNext');
	await timeout(3000);
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
		
	// Retorna txt e html com os links
	// Results é um string com todos os links concatenados
	return await page.content();

};

/**
* Opens google chrome 
* 
* Arguments:
*/
exports.newBrowser = async () => {
	return await puppeteer.launch({
		//headless: false,
		// executablePath: '/usr/bin/google-chrome'
		args: ['--no-sandbox', '--disable-setuid-sandbox', '--user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"']
	});
}
