// sort the array, check the last two elements in the array, pop last two elements if they are same, pop the last element & change the second last element as last-secondlast
// check if there's any item left in the array. if there's no elements left, return 0.
/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
  while (stones.length > 1) {
    const last = stones.length - 1;
    stones.sort(compareNumbers);

    if (stones[last] === stones[last - 1]) {
      stones.pop();
      stones.pop();
    } else {
      stones[last - 1] = stones[last] - stones[last - 1];
      stones.pop();
    }
  }

  return stones[0] ? stones[0] : 0;
};

function compareNumbers(a, b) {
  return a - b;
}

// The shift() method of Array instances removes the first element from an array and returns that removed element.
// This method changes the length of the array.
/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
  while (stones.length > 1) {
    stones.sort((a, b) => b - a);
    stones[1] = stones[0] - stones[1];
    stones.shift(); //shift the array to get rid of the 0 index
  }

  return stones[0];
};
