const puppeteerSearch = require('../utils/puppeteer_search');
const PythonShell = require('python-shell');
const date = new Date();

const pesquisasController = require('../server/controllers').pesquisas;


exports.getPuppeteerResults = async(persistence) => {
    console.log ('rodando bateria de pesquisas...');
    const queries = await persistence.read('actors/actors.json');
    const browser = await puppeteerSearch.newBrowser();
    const page = await browser.newPage();
    const usuario = process.argv[3];
    const senha = process.argv[4];
    try {
        await puppeteerSearch.loginGoogle(page, usuario, senha);
    } catch(e) {
        console.log("Usuario ou senha invalidos");
    }
    try {
        for (let query of queries['atores']) {
            console.log(query);
            let data = await puppeteerSearch.googleSearch(page, query);
            let fileDest = await persistence.write('pup_' + query, ".html", data);
            data = await htmlParse(fileDest);
            data.data = date.toLocaleString();
            data.ator = query;
            data.perfil = usuario;
            // escreve dados no banco
            await pesquisasController.createLocal(data);
        }
    } catch (e) {
        console.log(e);
        process.exit();
    } finally {
        browser.close();
        process.exit(); // o processo do puppeteer não tá terminando, precisamos investigar
    }
}

const htmlParse = async(file) => {
    let pyshell = new PythonShell('./utils/html_parse.py');

    pyshell.send(file);

    let res = "";
    pyshell.on('message', function (message) {
        res += message;
    });
    let data;
    return new Promise(resolve => {
        pyshell.end(async (err,code,signal) => {
            if (err) throw err;
            data = JSON.parse(res);
            resolve(data);
        });
    });
}