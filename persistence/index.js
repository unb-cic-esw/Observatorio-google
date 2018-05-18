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
    module.write = function(name, extension, data) {
        name = name.replace(/ /g, '_');
        const fileName = name + extension;

        createFolder(directory);
        createFolder(directory + currentDate);
        createFolder(directory + currentDate + '/' + name);

        const fileDest = directory + currentDate + '/' + name + '/' + fileName;

        writer = fs.createWriteStream(fileDest, { flags: 'a+'});
        
        if(extension == '.json'){
            data = JSON.parse(data);
            data = {'time' : date.toLocaleTimeString(), 'data' : data};
            data = JSON.stringify(data);
        }
        
        writer.write(data);

        if(extension == '.json'){
            var PythonShell = require('python-shell');
            var pyshell = new PythonShell('./persistence/s3_upFile.py');

            pyshell.send(fileDest);

            pyshell.on('message', function (message) {
              console.log(message);
            });
            
            pyshell.end(function (err,code,signal) {
              if (err) throw err;
            });
        }
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
