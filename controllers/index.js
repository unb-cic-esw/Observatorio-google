const googleAPI = require('../google_api');
const googleScraper = require('google');

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
        persistence.read('listaat', getGoogleAPI);
        persistence.read('listaat', getGoogleScraper);
    }

    /**
     * Request API data for a query.
     * 
     * Arguments:
     *  - query: Query to be made.
     */
    const getGoogleAPI = function(query) {
        const response = googleAPI.retrieveLinks(query,
                "005182128650059414634%3Acpbzek4imty",
                "AIzaSyC-6UytV9d7x16YvRzM1j-gdy1W3yTV-9w",
                10);

        if (query && response) {
            persistence.write('_api.txt', query + '\n');

            response.forEach((currentValue) => {
                persistence.write('_api.txt', '\t*' + currentValue["title"] + '\n');
                persistence.write('_api.txt', '\t\t' + currentValue["link"] + '\n');
            })
        }
    }

    /**
     * Get the results using scraper for a query.
     * 
     * Arguments:
     *  - query: Query to be made.
     */
    const getGoogleScraper = function(query) {
        googleScraper.resultsPerPage = resultsPerPage;
        
        googleScraper(query, function(err, res) {
            persistence.write('_scraper.txt', query + '\n');

            if (err) {
                console.error(err);
                return;
            }

            for (var counter = 0; counter < res.links.length; counter++) {
                const link = res.links[counter];

                if (!link.href) {
                    continue;
                }

                persistence.write('_scraper.txt', '\t' + link.title + '\n');
                persistence.write('_scraper.txt', '\t\t' + link.href + '\n');
            }
        })
    }

    return module;
}

module.exports = controller;