require('dotenv').config();

const persistence = require('./persistence/index.js');
const googlePuppeteerAWS = require('./commands/puppeteerMain.js');
const googlePuppeteerDb = require('./commands/puppeteerDb.js');
const googleApi = require('./commands/apiMain.js');
const googleScrapper = require('./commands/scraperMain.js');

/**
 * Execute the requests.
 *
 *	deve ser passado o tipo de pesquisa:
 *	'scrapper', 'api', ou 'puppeteer'
 */
const tipoPesquisa = process.argv[2];

if (tipoPesquisa == 'scraper') {
	googleScrapper.getScraperResults(persistence());
}
else if (tipoPesquisa == 'api') {
	googleApi.getAPIResults(persistence());
}
else if (tipoPesquisa == 'puppeteer') {
	googlePuppeteerDb.getPuppeteerResults(persistence());
}
else {
	console.log ('selecione um tipo de pesquisa (scraper, api ou puppeteer)');
}