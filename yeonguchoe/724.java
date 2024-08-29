// Time complexity: O(n)
// Space complexity: O(1)
public int pivotIndex(int[] nums) {
    int rightSum = 0;
    for (int n : nums) {
        rightSum += n;
    }
    int leftSum = 0;
    for (int i = 0; i < nums.length; i++) {
        rightSum -= nums[i];
        if (leftSum == rightSum) {
            return i;
        }
        // 다음 단계에 대한 준비
        leftSum += nums[i];
    }
    return -1;
}
