/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let presentCount = init;  // Step 1: Initialize the counter with the value `init`

    // Step 2: Increment function
    function increment(){
        return ++presentCount;  // Increase the current value by 1 and return it
    }

    // Step 3: Decrement function
    function decrement(){
        return --presentCount;  // Decrease the current value by 1 and return it
    }

    // Step 4: Reset function
    function reset(){
        return (presentCount = init);  // Reset the counter back to its initial value and return it
    }

    // Step 5: Return an object with the three functions
    return { increment, decrement, reset};
};


/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */