// Time complexity: O(n)
// Space complexity: O(1)
public int removeElement(int[] nums, int val) {
    int readPointer = 0;
    int writePointer = 0;

    while (readPointer < nums.length) {
        if (nums[readPointer] == val) {
            // 이번 num이 val인 경우
            readPointer += 1;
        } else {
            // 이번 num이 val과 다른 경우
            nums[writePointer] = nums[readPointer];
            readPointer += 1;
            writePointer += 1;
        }
    }
    return writePointer;
}
