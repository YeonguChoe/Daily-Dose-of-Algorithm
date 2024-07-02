/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const results = [];

  nums.sort((a, b) => a - b);
  const target = 0;

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > target) break;
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let j = i + 1;
    let k = nums.length - 1;

    while (j < k) {
      let sum = nums[i] + nums[j] + nums[k];
      if (sum === target) {
        results.push([nums[i], nums[j], nums[k]]);
        // we don't want duplicates
        while (j < k && nums[j] === nums[j + 1]) {
          j++;
        }
        while (j < k && nums[k] === nums[k - 1]) {
          k--;
        }
        j++;
        k--;
      } else if (sum < target) {
        j++;
      } else {
        k--;
      }
    }
  }
  return results;
};
