/**
 * @param {Function} fn - The function to be memoized.
 * @return {Function} - A new function that caches results for identical inputs.
 */
function memoize(fn) {
    // Cache object to store results of previous function calls.
    const cache = {};

    return function(...args) {
        // Create a key for the cache based on the arguments (serialized as a JSON string).
        const key = JSON.stringify(args);
        
        // Check if the result is already in the cache.
        if (key in cache) {
            return cache[key]; // Return the cached result.
        }

        // Call the original function with the provided arguments.
        const result = fn.apply(this, args);
        
        // Store the result in the cache.
        cache[key] = result;

        return result; // Return the result.
    };
}

// Example usage:
const memoizedSum = memoize(function(a, b) {
    return a + b; // Function to sum two numbers.
});

/** 
 * Example:
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *   callCount += 1; // Track how many times the function is called.
 *   return a + b;   // Function logic.
 * });
 *
 * memoizedFn(2, 3); // First call: calculates and returns 5.
 * memoizedFn(2, 3); // Second call: retrieves 5 from the cache.
 * console.log(callCount); // Logs: 1 (the function was only executed once).
 */
