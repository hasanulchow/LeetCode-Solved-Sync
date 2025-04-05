/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    function stringifyValue(value) {
        if (typeof value === 'string') {
            return '"' + value + '"';
        } else if (Array.isArray(value)) {
            return '[' + value.map(stringifyValue).join(',') + ']';
        } else if (typeof value === 'object' && value !== null) {
            return jsonStringify(value);
        } else {
            return String(value);
        }
    }
    if (typeof object === 'object' && object !== null) {
    if (Array.isArray(object)) {
        return '[' + object.map(stringifyValue).join(',') + ']';
    } else {
        var keys = Object.keys(object);
        return '{' + keys.map(function(key) {
            return '"' + key + '":' + stringifyValue(object[key]);
        }).join(',') + '}';
    }
    } else {
        return stringifyValue(object);
    }
};