const Persistence = require('./../persistence/index.js')();
const PuppeteerSearch = require("../utils/puppeteer_search");
const PythonShell = require("python-shell");
const PesquisasController = require("../server/controllers").pesquisas;
const Promise = require('es6-promise').Promise;
let request = require('request');
const date = new Date();

/**
 * .
 * 
 * Arguments:
 */
exports.getPuppeteerResults = async() => {
    const queries = await Persistence.read("actors/actors.json");
    let browser = await PuppeteerSearch.newBrowser();
    let page = await browser.newPage();
    const usuario = process.argv[2];
    const senha = process.argv[3];
    let cont = 0;
    await PuppeteerSearch.loginGoogle(page, usuario, senha);
    try {
        for (let query of queries.atores) {
            cont++;
            if(cont == 30){
                browser.close();
                browser = await PuppeteerSearch.newBrowser();
                page = await browser.newPage();
                await PuppeteerSearch.loginGoogle(page, usuario, senha);
            	cont = 0;
			}
            let data = await PuppeteerSearch.googleSearch(page, query);
            let fileDest = await Persistence.write("pup_" + query, ".html", data);
            data = await htmlParse(fileDest);
            data.data = date.toLocaleString();
            data.ator = query;
            data.perfil = usuario;
            // escreve dados no banco
            request.post(process.env["POST_URL"], {json : data});
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
    let pyshell = new PythonShell("./html_scanner/html_scanner.py");

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
