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
const loginGoogle = async(page, email, password) => {
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
* Creates a PDF with the resultant page of the google search of the query.
* 
* Arguments:
*  - query: Query to be made.
*/
exports.googleSearch = async (query) => {
	const browser = await puppeteer.launch({
		//headless: false,
		executablePath: '/usr/bin/google-chrome',
		args: ['--no-sandbox', '--disable-setuid-sandbox']
	});
	const page = await browser.newPage();
	
	try{
		await loginGoogle(page, "login", "senha");
	}
	catch(e){
		console.log("Login ou senha invalidos");
	}
	const baseLink = 'https://www.google.com.br/search?q=';

	await page.goto(baseLink + query);
	
	await persistence.createFolder(directory);
	await persistence.createFolder(directory + currentDate);
	
	await page.screenshot({
		path:  directory + currentDate + '/' + date.toLocaleTimeString() + '_' + query + '.png',
		fullPage : true
	});

	const html = await page.content();
	await persistence.write("_" + query + ".html", html);
	browser.close();
};

