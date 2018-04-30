const chai = require('chai');
const expect = chai.expect;
const controller = require('../controllers/index.js');

/**
 * Tests for controller.
 * 
 * TODO: Has to handle asynchronous function.
 */
describe('controller', function() {
    it('should return true if query is possible', function() {
        const getGoogleScraper = controller().getGoogleScraper;
        // expect(getGoogleScraper('test')).to.equal(true);
    });
});