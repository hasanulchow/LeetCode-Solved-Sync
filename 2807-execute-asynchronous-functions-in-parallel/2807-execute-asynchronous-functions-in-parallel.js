/**
 * @param {Array<Function>} functions - An array of functions that return promises
 * @return {Promise<any>} - A promise that resolves when all input promises resolve or rejects when any input promise rejects
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        // Array to store the results of the resolved promises
        const results = new Array(functions.length);
        // Counter to keep track of how many promises have resolved
        let count = 0;

        // Iterate over each function
        functions.forEach((fn, i) => {
            // Call the function to get the promise and handle its resolution or rejection
            fn()
                .then(val => {
                    // Store the resolved value in the correct index
                    results[i] = val;
                    count++;
                    // If all promises are resolved, resolve the main promise
                    if (count === functions.length) resolve(results);
                })
                .catch(reason => {
                    // If any promise rejects, reject the main promise
                    reject(reason);
                });
        });
    });
};

/**
 * Example usage:
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
