const chai = require('chai');
const expect = chai.expect;
const persistence = require('../persistence/index.js');


// Tests for persistence module.

/**
 * Tests for canOpenFile method.
*/
describe('persistence canOpenFile tests', function() {

    it('should return true if file passed exists', function() {
        const canOpenFile = persistence().canOpenFile;
        expect(canOpenFile('./listaat')).to.equal(true);
    });

    it('should return false if file passed don\'t exists', function() {
        const canOpenFile = persistence().canOpenFile;
        expect(canOpenFile('./anyfile')).to.equal(false);
    });

    it('should return false if a number is passed', function() {
        const canOpenFile = persistence().canOpenFile;
        expect(canOpenFile(20)).to.equal(false);
    });

    it('should return false if null is passed', function() {
        const canOpenFile = persistence().canOpenFile;
        expect(canOpenFile(null)).to.equal(false);
    });

    it('should return false if undefined is passed', function() {
        const canOpenFile = persistence().canOpenFile;
        expect(canOpenFile(undefined)).to.equal(false);
    });
    
});

/**
 * Tests for checkFolderExists method.
*/
describe('persistence checkFolderExists tests', function() {

    it('should return true if exists folder named test', function() {
        const checkFolderExists = persistence().checkFolderExists;
        expect(checkFolderExists('test')).to.equal(true);
    });

    it('should return true if root folder exists', function() {
        const checkFolderExists = persistence().checkFolderExists;
        expect(checkFolderExists('/')).to.equal(true);
    });

    it('should return false if not exists folder named 456', function() {
        const checkFolderExists = persistence().checkFolderExists;
        expect(checkFolderExists('456')).to.equal(false);
    });

    it('should return false if not exists folder named #$@', function() {
        const checkFolderExists = persistence().checkFolderExists;
        expect(checkFolderExists('#$@')).to.equal(false);
    });

    it('should return false if not exists folder named folder', function() {
        const checkFolderExists = persistence().checkFolderExists;
        expect(checkFolderExists('folder')).to.equal(false);
    });
    
});


/**
 * Tests for createFolder method.
*/
describe('persistence createFolder tests', function() {

    it('should return true if can create folder with letters', async function() {
        const createFolder = persistence().createFolder;
        expect(await createFolder('testFolder')).to.equal(true);
    });

    it('should return true if can create folder with numbers', async function() {
        const createFolder = persistence().createFolder;
        expect(await createFolder('123')).to.equal(true);
    });

    it('should return true if can create folder with symbols', async function() {
        const createFolder = persistence().createFolder;
        expect(await createFolder('@#$')).to.equal(true);
    });

    it('should return true if can create folder with alphanumeric characters', async function() {
        const createFolder = persistence().createFolder;
        expect(await createFolder('testFolder123')).to.equal(true);
    });
});

/**
 * Test for read method.
 */
 describe('persistence read tests', function() {

    it('should return a non-empty array for listaat', async function() {
        const read = persistence().read;
        const result = await read('listaat');
        expect(result.length).to.above(0);
    });

    it('should return null for file that not exist', async function() {
        const read = persistence().read;
        const result = await read('anyfile');
        expect(result).to.equal(null);
    });

    it('should return null for undefined passed', async function() {
        const read = persistence().read;
        const result = await read(undefined);
        expect(result).to.equal(null);
    });

    it('should return null for null passed', async function() {
        const read = persistence().read;
        const result = await read(null);
        expect(result).to.equal(null);
    });

    it('should return null for numbers passed', async function() {
        const read = persistence().read;
        const result = await read(123);
        expect(result).to.equal(null);
    });
 });