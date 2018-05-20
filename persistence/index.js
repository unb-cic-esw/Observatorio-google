const fs = require('fs');
const readline = require('readline');
const date = new Date();

/**
 * Persistence module
 */
let persistence = function() {
    // Public methods of the module.
    let module = {};
    // Directory of result folder.
    const directory = "./resultados/";
    // Directory of resources.
    const resourceDirectory = "../resources/";
    // Current time as string.
    const currentDate = date.toLocaleDateString().replace(/\//g, '-');
    // Writer of the file.
    let writer = null

    /**
     * Write data in file.
     * 
     * Arguments:
     *  - fileName: Name of the file to be written.
     *  - data: Data to be written.
     */
    module.write = async(name, data) => {
        name = name.replace(/ /g, '_');

        createFolder(directory);
        createFolder(directory + currentDate);
        createFolder(directory + currentDate + '/' + name);

        const fileDest = directory + currentDate + '/' + name + '/' + name;

        writer = fs.createWriteStream(fileDest + ".html", { flags: 'w+'});
        writer.write(data);

        let PythonShell = require('python-shell');
        let pyshell = new PythonShell('./utils/html_parse.py');
        
        pyshell.send(fileDest);

        let res = "";
        await pyshell.on('message', function (message) {
            // console.log(message);
            res += message;
        });

        pyshell.end(async (err,code,signal) => {
            if (err) throw err;
            
            data = await module.read(fileDest + ".json");
            if(data == null)
                data = [];
            data.push({"time": date.toLocaleTimeString(), "data" : JSON.parse(res)});
            
            writer = fs.createWriteStream(fileDest + ".json", { flags: 'w+'});
            writer.write(JSON.stringify(data));
        });

        pyshell = new PythonShell('./persistence/s3_upFile.py');

        pyshell.send(fileDest + ".json");

        pyshell.on('message', function (message) {
            console.log(message);
        });
        
        pyshell.end(function (err,code,signal) {
            console.log("Erro no upload do arquivo: " + fileDest + ".json");
        });
    }

    /**
     * Read data in file.
     * 
     * Arguments:
     *  - fileName: Name of the file to be written.
     */
    module.read = async function(fileName) {
        const path = /*resourceDirectory + */ fileName

        if (canOpenFile(path)) {
            return JSON.parse(fs.readFileSync(fileName, 'utf8'));
        }

        return null;
    }

    /**
     * Create folder by name passed.
     * 
     * Arguments:
     *  - folderName: Name of the folder
     */
    const createFolder = async function(folderName) {
        if (!checkFolderExists(folderName)) {
            return new Promise(resolve => {
                fs.mkdirSync(folderName, 0766, function(err) {
                    if (err) {
                        console.error(err);
                        resolve(false);
                    }
                });
                resolve(true);
            });
        }

        return true;
    }

    /**
     * Check if folder exists.
     * 
     * Arguments:
     *  - folderName: Name of the folder
     */
    const checkFolderExists = function(folderName) {
        return fs.existsSync(folderName);
    }
	
	module.createFolder = createFolder;

    /**
     * Checks if the file can be opened.
     * 
     * Arguments:
     *  - fileName: Name of the file.
     */
    const canOpenFile = function(fileName) {
        if (fs.existsSync(fileName)) {
            return true;
        } else {
            return false;
        }
    }

    module.canOpenFile = canOpenFile;
    module.createFolder = createFolder;
    module.checkFolderExists = checkFolderExists;

    return module;
}

module.exports = persistence;
