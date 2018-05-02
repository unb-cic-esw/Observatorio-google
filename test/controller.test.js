const chai = require('chai');
const expect = chai.expect;
const controller = require('../controllers/index.js');

/**
 * Tests for controller.
 * 
 * TODO: Has to handle asynchronous function.
 */
// describe('controller', function() {
//     it('should async return true if query is possible', function(done) {
//         const getGoogleScraper = controller().getGoogleScraper;
//         expect(getGoogleScraper()).to.equal(true);
//     });
// });