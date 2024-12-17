/**
 * Joins two arrays of objects based on their `id` property.
 * If objects in `arr2` have the same `id` as objects in `arr1`, their properties are merged.
 * If the same property exists in both objects, the value from `arr2` will overwrite the value from `arr1`.
 * 
 * @param {Array} arr1 - The first array of objects.
 * @param {Array} arr2 - The second array of objects.
 * @return {Array} - An array of merged objects based on the `id` property.
 */
var join = function(arr1, arr2) {
    const result = {}; // Dictionary to store objects indexed by their `id`.
    
    // Add all objects from `arr1` to the `result` dictionary using their `id` as the key.
    for (let i = 0; i < arr1.length; i++) {
        result[arr1[i].id] = arr1[i];
    }
    
    // Iterate through `arr2` to merge objects or add new ones.
    for (let i = 0; i < arr2.length; i++) {
        if (result[arr2[i].id]) {
            // If an object with the same `id` exists in `result`, merge their properties.
            for (const key in arr2[i]) {
                result[arr2[i].id][key] = arr2[i][key]; // Overwrite or add properties from `arr2`.
            }
        } else {
            // If no object with the same `id` exists, add the object from `arr2`.
            result[arr2[i].id] = arr2[i];
        }
    }
    
    // Convert the `result` dictionary back into an array of objects.
    return Object.values(result);
};
