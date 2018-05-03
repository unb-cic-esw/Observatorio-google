const puppeteer = require('puppeteer');
const date = new Date();
const persistence = require('../persistence/index')();

const currentDate = date.toLocaleDateString().replace(/\//g, '-');
const directory = "./resultados/";

/**
* Creates a PDF with the resultant page of the google search of the query.
* 
* Arguments:
*  - query: Query to be made.
*/
exports.pdfSearch = async (query) => {
	const name = await date.toLocaleDateString() + query;

	await persistence.createFolder(directory);
	await persistence.createFolder(directory + currentDate);
	
	const browser = await puppeteer.launch({ headless: true});
	const page = await browser.newPage();
	const baseLink = 'https://www.google.com/search?client=ubuntu&channel=fs&q=';

	await page.goto(baseLink + query + '&ie=utf-8&oe=utf-8');

	await page.pdf({
		path:  directory + currentDate + '/' + date.toLocaleTimeString() + '_' + query + '.pdf',
		fomat: 'A4'  
	});
	browser.close();
};

