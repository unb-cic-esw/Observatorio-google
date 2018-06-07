require('dotenv').config();

const GooglePuppeteerDb = require('./commands/puppeteer_db.js');
const perfil = process.argv[2];

/**
 * Execute the requests.
 */
if(perfil == undefined)
    console.log("Digite o nome do perfil no terminal apos o comando para executar o programa.");
else
    GooglePuppeteerDb.getPuppeteerResults();
