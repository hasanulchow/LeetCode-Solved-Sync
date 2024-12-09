/**
 * @param {Function} fn - The function to be executed only once.
 * @return {Function} - A new function that wraps `fn` and ensures it is called only once.
 */
var once = function(fn) {
    // Variable to track if the function has already been called.
    let hasBeenCalled = false;
    // Variable to store the result of the first call to the function.
    let result;
    
    // Return a new function that wraps the original function.
    return function(...args) {
        // Check if the function has not been called yet.
        if (!hasBeenCalled) {
            // Call the original function with the provided arguments and store the result.
            result = fn(...args);
            // Mark the function as called.
            hasBeenCalled = true;
            // Return the result of the first call.
            return result;
        } else {
            // If the function has already been called, return `undefined` without calling it again.
            return undefined;
        }
    };
};

/**
 * Example usage:
 * let fn = (a, b, c) => (a + b + c); // A function that sums its arguments.
 * let onceFn = once(fn); // Wrap the function to ensure it is called only once.
 *
 * onceFn(1, 2, 3); // First call: returns 6 (fn is executed).
 * onceFn(2, 3, 6); // Subsequent call: returns undefined (fn is not executed again).
 */
