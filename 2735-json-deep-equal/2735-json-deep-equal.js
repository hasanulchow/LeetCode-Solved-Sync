/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    // exception: if one input is array the other one also needs to be an array
    if (Array.isArray(o1) !== Array.isArray(o2)) {
        return false;
    }

    // If the inputs are not objects we can use the strict equality
    if (typeof o1 !== "object" || typeof o2 !== "object" || o1 === null || o2 === null) {
        return o1 === o2;
    }
  
    // Check if both objects have the same keys
    const o1Keys = Object.keys(o1);
    const o2Keys = Object.keys(o2);
    if (o1Keys.length !== o2Keys.length || !o1Keys.every(key => o2.hasOwnProperty(key))) {
        return false; // If the objects dont have the same keys we return false
    }
  
    // Recursively check if the associated values are deeply equal 
    // if all iterations return true the method every return true
    return o1Keys.every(key => areDeeplyEqual(o1[key], o2[key]));
};