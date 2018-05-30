require('dotenv').config();

const GooglePuppeteerDb = require('./commands/puppeteer_db.js');

/**
 * Execute the requests.
 */
GooglePuppeteerDb.getPuppeteerResults();
