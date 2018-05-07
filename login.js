const puppeteer = require('puppeteer');
const fs = require('fs');
const persistence = require('./persistence/index');

const directory = "./cookies/"; 

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
loginGoogle = async(page, email, password) => {
	await page.goto('https://accounts.google.com/ServiceLogin')
	await timeout(3000);
	await page.click('#identifierId');
	await page.keyboard.type(email);
	await page.click('#identifierNext');
	await timeout(3000);
	await page.click('#password');
	await page.keyboard.type(password);
	await page.click('#passwordNext');
	await timeout(6000);

	// Save session cookies
	const cookiesObject = await page.cookies()
	const json = JSON.stringify(cookiesObject);
	await persistence().createFolder(directory);
	writer = fs.createWriteStream(directory + email + ".json", { flags: 'a+'});
	writer.write(json);

}

const login = process.argv[2];
const password = process.argv[3];

(async() => {
	const browser = await puppeteer.launch({
		headless: false,
		executablePath: '/usr/bin/google-chrome'
	});

	const page = await browser.newPage();

	await loginGoogle(page, login, password);
	browser.close();
})()
