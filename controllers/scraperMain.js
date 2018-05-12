const googleScraper = require('google');

// Results per page of the scraper.
const resultsPerPage = 10;

/**
* Get the results only of the Scraper.
*/
exports.getScraperResults = async function(persistence) {
    const queries = await persistence.read('actors/actors.json');
    let data = '';

    for (let index in queries) {
       data += await getGoogleScraper(queries[index]);
    }

    persistence.write('scraper', '.txt', data);
}


/**
* Get the results using scraper for a query.
* 
* Arguments:
*  - query: Query to be made.
*/
const getGoogleScraper = async function(query) {
    googleScraper.resultsPerPage = resultsPerPage;
    let data = '';

    return new Promise(resolve => {
        googleScraper(query, function(err, res) {
            data += query + '\n';

            if (err) {
                console.error(err);
                return false;
            }

            for (let counter = 0; counter < res.links.length; counter++) {
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