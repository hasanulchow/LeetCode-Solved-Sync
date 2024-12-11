/**
 * @param {Function} fn - The function to be executed after a delay.
 * @param {Array} args - The arguments to pass to the function `fn`.
 * @param {number} t - The delay (in milliseconds) before executing `fn`.
 * @return {Function} - A function to cancel the scheduled execution.
 */
var cancellable = function(fn, args, t) {
    // Define the cancel function
    const cancelFn = function() {
        // Clear the timeout to prevent `fn` from being executed
        clearTimeout(timer);
    };

    // Schedule the execution of `fn` with the provided arguments after the delay `t`
    const timer = setTimeout(() => {
        fn(...args); // Call `fn` with the spread arguments
    }, t);

    // Return the cancel function to allow cancellation of the scheduled execution
    return cancelFn;
};

/**
 * Example Usage:
 * 
 * const result = []; // Array to store the results
 *
 * const fn = (x) => x * 5; // A sample function to multiply input by 5
 * const args = [2], t = 20, cancelTimeMs = 50; // Arguments and delay
 *
 * const start = performance.now(); // Record the start time
 *
 * const log = (...argsArr) => {
 *     const diff = Math.floor(performance.now() - start); // Calculate elapsed time
 *     result.push({"time": diff, "returned": fn(...argsArr)}); // Log the result and time
 * }
 *       
 * const cancel = cancellable(log, args, t); // Schedule `log` execution
 *
 * const maxT = Math.max(t, cancelTimeMs); // Maximum delay for execution or cancellation
 *           
 * setTimeout(cancel, cancelTimeMs); // Cancel the execution after `cancelTimeMs`
 *
 * setTimeout(() => {
 *     console.log(result); // Logs the result array after the maximum delay
 * }, maxT + 15);
 */
