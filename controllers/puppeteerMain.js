const puppeteerSearch = require('../utils/puppeteer_search');
const PythonShell = require('python-shell');
const date = new Date();

/**
 * Get the results only of the Puppeteer.
 */
exports.getPuppeteerResults = async(persistence) => {
    let allDates = await readS3("dates.json");

    if(allDates == "")
        allDates = {"dates" : []};
    else
        allDates = JSON.parse(allDates);

    allDates["dates"].push(date.toLocaleDateString().replace(/\//g, '-'));
    await persistence.rawWrite("allDates.json", JSON.stringify(allDates));

    upToS3("allDates.json");
    const queries = await persistence.read('actors/actors.json');
    const browser = await puppeteerSearch.newBrowser();
    const page = await browser.newPage();

    try{
        await puppeteerSearch.loginGoogle(page, process.argv[3], process.argv[4]);
    }
    catch(e) {
        console.log("Login ou senha invalidos");
    }
    for (let query of queries['actors']) {
        // Pesquisa resultando nos links em '.txt e '.html'
        console.log(query);
        let data = await puppeteerSearch.googleSearch(page, query);

        let fileDest = await persistence.write('pup_' + query, ".html", data);
        
        data = await htmlParse(fileDest);
        await persistence.write('pup_' + query, ".json", JSON.stringify(data));
        
        upToS3(fileDest + ".json");
    }

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
            data = await readS3(file + ".json");
            if(data == "")
                data = [];
            else
                data = JSON.parse(data);
            data.push({"time": date.toLocaleTimeString(), "data" : JSON.parse(res)});
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