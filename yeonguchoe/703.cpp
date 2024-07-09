class KthLargest {
public:
    int k_value = 0;
    priority_queue<int, vector<int>, greater<int>> min_heap;

    KthLargest(int k, vector<int>& nums) {
        k_value = k;
        for (int num : nums) {
            min_heap.push(num);
        }
        while (min_heap.size() > k_value) {
            min_heap.pop();
        }
    }

    int add(int val) {
        min_heap.push(val);
        while (min_heap.size() > k_value) {
            min_heap.pop();
        }
        return min_heap.top();
    }
};
