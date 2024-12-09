/**
 * Filters the elements of an array based on a callback function.
 * @param {number[]} arr - The input array to filter.
 * @param {Function} fn - The callback function to test each element. 
 *                        It takes two arguments: the current element and its index.
 * @return {number[]} - A new array containing elements that satisfy the callback function.
 */
var filter = function(arr, fn) {
    let fil = []; // Initialize an empty array to store the filtered elements

    // Iterate through each element in the input array
    for (let i = 0; i < arr.length; i++) {
        // Apply the callback function to the current element and its index
        if (fn(arr[i], i)) {
            // If the callback returns true, add the element to the filtered array
            fil.push(arr[i]);
        }
    }

    // Return the array containing only the elements that passed the callback test
    return fil;
};
