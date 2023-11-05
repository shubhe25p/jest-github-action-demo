const fib = require('./index');

describe('Test for fib function', () => {
    test('fib(0) should be 0', () => {
        expect(fib(0)).toBe(0);
    });
    
    test('fib(1) should be 1', () => {
        expect(fib(1)).toBe(1);
    });
    
    test('fib(10) should be 55', () => {
        expect(fib(10)).toBe(55);
    });
    
    test('fib(20) should be 6765', () => {
        expect(fib(20)).toBe(6765);
    });
    });