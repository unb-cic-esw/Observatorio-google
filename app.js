require('dotenv').config();

const persistence = require('./persistence/index.js');
const googlePuppeteerAWS = require('./controllers/puppeteerMain.js');
const googlePuppeteerDb = require('./controllers/puppeteerDb.js');
const googleApi = require('./controllers/apiMain.js');
const googleScrapper = require('./controllers/scraperMain.js');

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
	process.env.PERSISTENCIA == 'db' ?
	googlePuppeteerDb.getPuppeteerResults(persistence()) :
	googlePuppeteerAWS.getPuppeteerResults(persistence())
}
else {
	console.log ('selecione um tipo de pesquisa (scraper, api ou puppeteer)');
}