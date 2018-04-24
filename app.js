const persistence = require('./persistence/index.js');
const controller = require('./controllers/index.js');

/**
 * Execute the requests.
 */
controller(persistence(), undefined).getResults();