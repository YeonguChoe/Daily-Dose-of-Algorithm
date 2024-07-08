// the last element is at the value of the array's length property minus 1.
// array.at(-1) === last element

/**
 * each new value adding time check min top val greater than this or not if yes push it on the stack(expect the case of first value)
 * and when pop the value from stack check min values is that value
 * or not if yes pop from both stack
 */

var MinStack = function () {
  this.stack = [];
  this.minstack = [];
};

/**
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
  this.stack[this.stack.length] = val;
  if (this.minstack.length === 0 || this.minstack.at(-1) >= val) {
    this.minstack[this.minstack.length] = val;
  }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
  if (!this.stack.length === 0) {
    return null;
  }

  if (this.minstack.at(-1) === this.stack.at(-1)) {
    this.minstack.length--;
  }
  this.stack.length--;
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
  if (this.stack.length === 0) {
    return null;
  }

  return this.stack.at(-1);
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
  if (this.minstack.length === 0) {
    return null;
  }
  return this.minstack.at(-1);
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
