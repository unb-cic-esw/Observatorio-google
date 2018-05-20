const puppeteerSearch = require('../utils/puppeteer_search')

/**
 * Get the results only of the Puppeteer.
 */
exports.getPuppeteerResults = async function(persistence) {
    const queries = await persistence.read('actors/actors.json');
    const browser = await puppeteerSearch.newBrowser();
    const page = await browser.newPage();

    try{
        await puppeteerSearch.loginGoogle(page, process.argv[3], process.argv[4]);
    }
    catch(e) {
        console.log("Login ou senha invalidos");
    }
    for (let query of queries['actors']) {
        // Pesquisa resultando nos links em '.txt e '.html'
        console.log(query);
        let data = await puppeteerSearch.googleSearch(page, query);

        await persistence.write('pup_' + query, data);
    }

    browser.close();
}