const chai = require('chai');
const expect = chai.expect;
const persistence = require('../persistence/index.js');

/**
 * Tests for persistence module.
 */
describe('persistence', function() {

    // Tests for canOpenFile method.

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

    // Tests for createFolder method.

    it('should return true if can create folder', function() {
        const createFolder = persistence().createFolder;
        expect(createFolder('testFolder123')).to.equal(true);
    });
    
});