// Time complexity: O(log n)
// Space complexity: O(log n)

int reverse(int x) {

        vector<int> digit;
        int current_number = x;
        bool is_positive = true;

        if (x < 0) {
            is_positive = false;
            if (current_number < (INT_MAX * -1)) {
                return 0;
            }

            current_number *= -1;
        }
        while (current_number > 0) {
            int right_most_digit = current_number % 10;
            digit.push_back(right_most_digit);
            current_number /= 10;
        }
        int size = digit.size();
        int result = 0;
        for (int i = 0; i < size; i++) {
            if (is_positive) {

                if (result > INT_MAX - (digit[i] * pow(10, size - i - 1))) {
                    return 0;
                }
                result += (digit[i] * pow(10, size - i - 1));
            } else {
                if (result < INT_MIN + (digit[i] * pow(10, size - i - 1))) {
                    return 0;
                }
                result -= (digit[i] * pow(10, size - i - 1));
            }
        }
        return result;
    }
