const puppeteerSearch = require('../utils/puppeteer_search');
const PythonShell = require('python-shell');
const date = new Date();

const pesquisasController = require('../server/controllers/pesquisas');


/**
 * Get the results only of the Puppeteer.
 */
exports.getPuppeteerResults = async(persistence) => {
    console.log ('opa, bom dia');
 //    let allDates = await readS3("all_dates.json");

 //    if(allDates == "")
 //        allDates = {"datas" : []};
 //    else
 //        allDates = JSON.parse(allDates);

	// if(allDates["datas"].indexOf(date.toLocaleDateString().replace(/\//g, '-')) <= -1){
 //        allDates["datas"].push(date.toLocaleDateString().replace(/\//g, '-'));
	// 	await persistence.rawWrite("all_dates.json", JSON.stringify(allDates));
	// }

 //    upToS3("all_dates.json");

    const queries = await persistence.read('actors/actors.json');
    const browser = await puppeteerSearch.newBrowser();
    const page = await browser.newPage();
    const usuario = process.argv[3];
    const senha = process.argv[4];
    try{
        await puppeteerSearch.loginGoogle(page, usuario, senha);
    }
    catch(e) {
        console.log("Usuario ou senha invalidos");
    }
    for (let query of queries['atores']) {
        // Pesquisa resultando nos links em '.txt e '.html'
        console.log(query);
        let data = await puppeteerSearch.googleSearch(page, query);
        let fileDest = await persistence.write('pup_' + query, ".html", data);
        data = await htmlParse(fileDest);
        data.data = date.toLocaleString();
        data.ator = query;
        data.perfil = usuario;
        //await persistence.write('pup_' + query, ".json", JSON.stringify(data));
        // escreve dados no banco
        await pesquisasController.create(data);
        process.exit(); // tirar depois
    }
    console.log(data);
    browser.close();
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
            // data = await readS3(file + ".json");
            // if(data == "")
            //     data = [];
            // else
            //     data = JSON.parse(data);
            //data.push({"horario": date.toLocaleTimeString(), "dados" : JSON.parse(res)});
            
            data = JSON.parse(res);

            resolve(data);
        });
    });
}

const readS3 = async(file) => {
    let pyshell = new PythonShell('./persistence/s3_read_file.py');

    pyshell.send(file);

    let res = "";
    pyshell.on('message', function (message) {
        res += message;
    });
    
    return new Promise(resolve => {
        pyshell.end(function (err,code,signal) {    
            if(err) throw err;
            resolve(res);
        });
    });
}

const upToS3 = async(file) => {
    let pyshell = new PythonShell('./persistence/s3_upFile.py');

    pyshell.send(file);

    pyshell.on('message', function (message) {
        console.log(message);
    });
    
    pyshell.end(function (err,code,signal) {
        if(err){
            console.log("Erro no upload do arquivo: " + file);
        }
    });
}
