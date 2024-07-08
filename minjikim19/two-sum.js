// brutal force
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 1; j < nums.length; j++) {
      if (i === j) {
        continue;
      }
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }

  return false;
};

// using map
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    let checker = target - nums[i];
    if (map.has(checker)) {
      return [map.get(checker), i];
    }
    map.set(nums[i], i);
  }
  return [];
};
