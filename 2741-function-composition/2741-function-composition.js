/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    // If the array of functions is empty, return the identity function
    if (functions.length === 0) {
        return function(x) {
            return x;
        };
    }
    
    // Use reduceRight to compose the functions from right to left
    return functions.reduceRight(function(prevFn, nextFn) {
        return function(x) {
            return nextFn(prevFn(x)); // Call the next function with the result of the previous function
        };
    });
};

/**
 * Example usage:
 * const fn = compose([x => x + 1, x => 2 * x]);
 * console.log(fn(4)); // Output: 9
 */
