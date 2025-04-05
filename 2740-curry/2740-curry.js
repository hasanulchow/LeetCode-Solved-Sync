/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    return function curried(...args) {
        // accumulate argument
        if (args.length < fn.length) { 
            return (...next) => curried(...args, ...next);
        }
        // call function 
        else {
            return fn(...args);
        }
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */