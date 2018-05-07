const persistence = require('./persistence/index.js');
const controller = require('./controllers/index.js');

/**
 * Execute the requests.
 *
 *	deve ser passado o tipo de pesquisa:
 *	'scrapper', 'api', ou 'puppeteer'
 */
const tipoPesquisa = process.argv[2];
const cookieFile = process.argv[3];

if (tipoPesquisa == 'scraper') {
	controller(persistence(), undefined).getScraperResults();
}
else if (tipoPesquisa == 'api') {
	controller(persistence(), undefined).getAPIResults();
}
else if (tipoPesquisa == 'puppeteer') {
	controller(persistence(), undefined).getPuppeteerResults(cookieFile);
}
else {
	console.log ('selecione um tipo de pesquisa (scraper, api ou puppeteer)');
}
