const googleAPI = require('../utils/google_api');
const googleScraper = require('google');
const puppeteerSearch = require('../utils/puppeteer_search')

/**
 * Main controller.
 */
var controller = function(persistenceRef, viewRef) {
    // Public methods of the module.
    var module = {};
    // Reference to the persisntece module.
    const persistence = persistenceRef;
    // Reference to the view.
    const view = viewRef;
    // Results per page of the scraper.
    const resultsPerPage = 10;

    
    /**
     * Get the results of the API and Scraper.
     */
    module.getResults = function() {
        getScraperResults();
        getAPIResults();
    }

    /**
     * Get the results only of the API.
     */
    const getAPIResults = async function() {
        const queries = await persistence.read('listaat');
        var data = '';

        for (var index in queries) {
            data += await getGoogleAPI(queries[index]);
        }

        persistence.write('_api.txt', data);
    }

    /**
     * Get the results only of the Scraper.
     */
    const getScraperResults = async function() {
        const queries = await persistence.read('listaat');
        var data = '';

        for (var index in queries) {
            data += await getGoogleScraper(queries[index]);
        }

        persistence.write('_scraper.txt', data);
    }

	/**
	 * Get the results only of the Puppeteer.
	 */
	module.getPuppeteerResults = async function() {
        const queries = await persistence.read('listaat');
		const browser = await puppeteerSearch.newBrowser();
		const page = await browser.newPage();

		try{
			await puppeteerSearch.loginGoogle(page, "login", "senha");
		}
		catch(e) {
			console.log("Login ou senha invalidos");
		}
		for (let query of queries) {
            // Pesquisa resultando nos links em '.txt'
			let txt_data = await puppeteerSearch.googleSearch(page, query, "txt");
            persistence.write('_pup_' + query + '.txt', txt_data);
            // Pesquisa resultando nos html puro da página pesquisada
            let html_data = await puppeteerSearch.googleSearch(page, query, "html");
            persistence.write('_pup_' + query + '.html', html_data);
		}

		browser.close();
	}

	/**
     * Request API data for a query.
     * 
     * Arguments:
     *  - query: Query to be made.
     */
    const getGoogleAPI = async function(query) {
        const response = googleAPI(query,
                "005182128650059414634%3Acpbzek4imty",
                "AIzaSyC-6UytV9d7x16YvRzM1j-gdy1W3yTV-9w",
                10);
        var data = '';
        
        return new Promise(resolve => {
            if (query && response) {
                data += query + '\n';
    
                response.forEach((currentValue) => {
                    data += '\t*' + currentValue["title"] + '\n';
                    data += '\t\t' + currentValue["link"] + '\n';
                })
    
                data += '\n';
            }

            resolve(data);
        });
    }

    /**
	 * Get the results using scraper for a query.
	 * 
	 * Arguments:
	 *  - query: Query to be made.
	 */
	const getGoogleScraper = async function(query) {
		googleScraper.resultsPerPage = resultsPerPage;
		var data = '';

        return new Promise(resolve => {
            googleScraper(query, function(err, res) {
                data += query + '\n';
    
                if (err) {
                    console.error(err);
                    return false;
                }
    
                for (var counter = 0; counter < res.links.length; counter++) {
                    const link = res.links[counter];
    
                    if (!link.href) {
                        continue;
                    }
    
                    data += '\t' + link.title + '\n'
                    data += '\t\t' + link.href + '\n'
                }

                data += '\n';
                resolve(data);
            })
        });
	}

    module.getGoogleScraper = getGoogleScraper;
    module.getAPIResults = getAPIResults;

    return module;
}

module.exports = controller;
