const googleAPI = require('../api/google_api');
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
     * Get the results only of the API.
     */
    module.getAPIResults = function() {
        persistence.read('listaat', getGoogleAPI);
    }

    /**
     * Get the results only of the Scraper.
     */
    module.getScraperResults = function() {
        persistence.read('listaat', getGoogleScraper);
    }

    /**
     * Request API data for a query.
     * 
     * Arguments:
     *  - query: Query to be made.
     */
    const getGoogleAPI = function(query) {
        const response = googleAPI(query,
                "005182128650059414634%3Acpbzek4imty",
                "AIzaSyC-6UytV9d7x16YvRzM1j-gdy1W3yTV-9w",
                10);
        var data = '';
        
        if (query && response) {
            data += query + '\n';

            response.forEach((currentValue) => {
                data += '\t*' + currentValue["title"] + '\n';
                data += '\t\t' + currentValue["link"] + '\n';
            })

            persistence.write('_api.txt', data);
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
        var data = '';

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

            persistence.write('_scraper.txt', data);
        })

        return true;
    }

    module.getGoogleScraper = getGoogleScraper;

    return module;
}

module.exports = controller;