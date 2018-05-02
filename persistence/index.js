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
    module.read = function(fileName, callback) {
        const path = /*resourceDirectory + */ fileName

        if (canOpenFile(path)) {
            const reader = readline.createInterface({
                input: fs.createReadStream(path)
            });
            reader.on('line', callback);
        }
    }

    /**
     * Create folder by name passed.
     * 
     * Arguments:
     *  - folderName: Name of the folder
     */
    const createFolder = function(folderName,) {
        if (!fs.existsSync(folderName)) {
            fs.mkdirSync(folderName, 0766, function(err) {
                if (err) {
                    console.error(err);
                    return false;
                }
            });
        }

        return true;
    }

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