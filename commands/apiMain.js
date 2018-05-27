const googleAPI = require('../utils/google_api');

/**
* Get the results only of the API.
*/
exports.getAPIResults = async function(persistence) {
    const queries = await persistence.read('actors/actors.json');
    let data = '';

    for (let index in queries) {
        data += await getGoogleAPI(queries[index]);
    }

    persistence.write('api', '.txt', data);
}

/**
* Request API data for a query.
* 
* Arguments:
*  - query: Query to be made.
*/
const getGoogleAPI = async function(query) {
    const resolveesponse = googleAPI(query,
                                    "005182128650059414634%3Acpbzek4imty",
                                    "AIzaSyC-6UytV9d7x16YvRzM1j-gdy1W3yTV-9w",
                                    10);
    let data = '';

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
