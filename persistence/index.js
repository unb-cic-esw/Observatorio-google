const fs = require('fs');
const readline = require('readline');
const date = new Date();

/**
 * Persistence module
 */
var persistence = function() {
    // Public methods of the module.
    var module = {};
    // Directory of result folder.
    const directory = "./resultados/";
    // Directory of resources.
    const resourceDirectory = "../resources/";
    // Current time as string.
    const currentDate = date.toLocaleDateString().replace(/\//g, '-');
    // Writer of the file.
    var writer = null


    /**
     * Write data in file.
     * 
     * Arguments:
     *  - fileName: Name of the file to be written.
     *  - data: Data to be written.
     */
    module.write = function(fileName, data) {
        const name = date.toLocaleTimeString() + fileName;

        createFolder(directory);
        createFolder(directory + currentDate);

        writer = fs.createWriteStream(directory + currentDate +
                                        '/' + name, { flags: 'a+'});

        writer.write(data);
    }

    /**
     * Read data in file.
     * 
     * Arguments:
     *  - fileName: Name of the file to be written.
     *  - callback: Callback for every line readed.
     */
    module.read = async function(fileName) {
        const path = /*resourceDirectory + */ fileName

        if (canOpenFile(path)) {
            var lines = [];
            const reader = readline.createInterface({
                input: fs.createReadStream(path)
            });

            return new Promise(resolve => {
                reader.on('line', (input) => {
                    lines.push(input);
                });
                reader.on('close', function() {
                    resolve(lines);
                });
            })
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