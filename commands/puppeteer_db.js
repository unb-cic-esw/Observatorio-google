const Persistence = require('./../persistence/index.js')();
const PuppeteerSearch = require("../utils/puppeteer_search");
const PythonShell = require("python-shell");
const PesquisasController = require("../server/controllers").pesquisas;
const Promise = require('es6-promise').Promise;
const date = new Date();

/**
 * Calls a python script that extracts data from a html file and returns a json with the data.
 * 
 * Arguments:
 *  - file: Name of the html file.
 */
exports.getPuppeteerResults = async() => {
    const queries = await Persistence.read("actors/actors.json");
    const browser = await PuppeteerSearch.newBrowser();
    const page = await browser.newPage();
    const usuario = process.argv[3];
    const senha = process.argv[4];
    await PuppeteerSearch.loginGoogle(page, usuario, senha);
    try {
        for (let query of queries.atores) {
            let data = await PuppeteerSearch.googleSearch(page, query);
            let fileDest = await Persistence.write("pup_" + query, ".html", data);
            data = await htmlParse(fileDest);
            data.data = date.toLocaleString();
            data.ator = query;
            data.perfil = usuario;
            // escreve dados no banco
            await PesquisasController.createLocal(data);
        }
    } catch (e) {
        process.exit();
    } finally {
        browser.close();
        process.exit(); // o processo do puppeteer não tá terminando, precisamos investigar
    }
}

/**
 * Calls a python script that extracts data from a html file and returns a json with the data.
 * 
 * Arguments:
 *  - file: Name of the html file.
 */
const htmlParse = async(file) => {
    let pyshell = new PythonShell("./utils/html_parse.py");

    pyshell.send(file);

    let res = "";
    pyshell.on("message", function (message) {
        res += message;
    });

    let data;
    return new Promise(resolve => {
        pyshell.end(async (err) => {
            if (err) throw err;
            data = JSON.parse(res);
            resolve(data);
        });
    });
}