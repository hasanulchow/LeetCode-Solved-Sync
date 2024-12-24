class MedianFinder {
public:
    // Two heaps:
    // maxHeap: Stores the smaller half of the numbers (max-heap by default in C++).
    // minHeap: Stores the larger half of the numbers (min-heap using greater<int> comparator).
    priority_queue<int, vector<int>, greater<int>> minHeap;
    priority_queue<int> maxHeap;

    // Constructor
    MedianFinder() {}

    // Add a number to the data structure
    void addNum(int num) {
        // Always push the new number to maxHeap first
        maxHeap.push(num);

        // Ensure all elements in maxHeap are less than or equal to all elements in minHeap
        if (!minHeap.empty() && maxHeap.top() > minHeap.top()) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        }

        // Balance the size of the heaps so that their sizes differ by at most 1
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        }
        if (minHeap.size() > maxHeap.size() + 1) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    // Find the median of the numbers added so far
    double findMedian() {
        // If one heap has more elements, its top element is the median
        if (minHeap.size() > maxHeap.size()) return minHeap.top();
        if (maxHeap.size() > minHeap.size()) return maxHeap.top();

        // If both heaps are of equal size, the median is the average of the top elements
        return (minHeap.top() + maxHeap.top()) / 2.0;
    }
};
