const persistence = require('./persistence/index.js');
const googlePuppeteer = require('./controllers/puppeteerMain.js');
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
	googlePuppeteer.getPuppeteerResults(persistence());
}
else {
	console.log ('selecione um tipo de pesquisa (scraper, api ou puppeteer)');
}