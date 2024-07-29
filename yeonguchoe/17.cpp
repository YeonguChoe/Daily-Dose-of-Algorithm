// Time complexity: O(4^n * n)
// Space complexity: O(n)

unordered_map<int, vector<char>> dial_to_char = {
    {2, {'a', 'b', 'c'}},
    {3, {'d', 'e', 'f'}},
    {4, {'g', 'h', 'i'}},
    {5, {'j', 'k', 'l'}},
    {6, {'m', 'n', 'o'}},
    {7, {'p', 'q', 'r', 's'}},
    {8, {'t', 'u', 'v'}},
    {9, {'w', 'x', 'y', 'z'}}
};

void backtracking(string input_string, string current_combination, vector<string>& answers)
{
    // input_string이 "" 되면, Leaf 에 도달했다는 뜻이므로 answer 리스트에 추가하고 반환
    if (input_string.size() == 0)
    {
        answers.push_back(current_combination);
    }
    else
    {
        // input_string에서 맨 앞숫자를 떼내서 int 숫자로 만듬
        int current_number = input_string[0] - '0';
        // 해당 숫자를 키로 갖는 알파벳들을 구함
        vector<char> available_char = dial_to_char[current_number];
        string excluding_first_char = input_string.substr(1);

        // 알파벳들을 하나씩 붙였다가 뗏다가 하면서 backtracking 함수 재귀적으로 호출
        for (char c : available_char)
        {
            current_combination += c;
            backtracking(excluding_first_char, current_combination, answers);
            current_combination.pop_back();
        }
    }
}

vector<string> letterCombinations(string digits)
{
    vector<string> result;
    backtracking(digits, "", result);
    return result;
}
