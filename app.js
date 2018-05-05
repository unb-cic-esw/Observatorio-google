const persistence = require('./persistence/index.js');
const controller = require('./controllers/index.js');

/**
 * Execute the requests.
 *
 *	deve ser passado o tipo de pesquisa:
 *	'scrapper', 'api', ou 'puppeteer'
 */
const tipoPesquisa = process.argv[2];

console.log(tipoPesquisa);

if (tipoPesquisa == 'scrapper') {
	controller(persistence(), undefined).getScraperResults();
}
else if (tipoPesquisa == 'api') {
	controller(persistence(), undefined).getAPIResults();
}
else if (tipoPesquisa == 'puppeteer') {
	controller(persistence(), undefined).getPuppeteerResults();
}
else {
	console.log ('selecione um tipo de pesquisa (scrapper, api ou puppeteer)');
}
