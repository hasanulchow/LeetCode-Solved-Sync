/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[][]}
 */
var kSmallestPairs = function (nums1, nums2, k) {
    let q = new MaxPriorityQueue();

    for (let i = 0; i < nums1.length; i++) {
        for (let j = 0; j < nums2.length; j++) {
            let sum = nums1[i] + nums2[j], pair = [nums1[i], nums2[j]];
            if (q.size() < k)
                q.enqueue(pair, sum);
            else if (q.front().priority > sum) {
                q.dequeue();
                q.enqueue(pair, sum);
            } else
                break;
        }
    }

    return q.toArray().map(e => e.element);
};