// Time complexity: O(n log n)
// Space complexity: O(n)

vector<vector<string>> groupAnagrams(vector<string>& strs)
{
    vector<vector<string>> output;
    unordered_map<string, vector<string>> hash_map;
    for (string word : strs)
    {
        string sorted_word = word;
        sort(sorted_word.begin(), sorted_word.end());
        hash_map[sorted_word].push_back(word);
    }
    for (const auto& pair : hash_map)
    {
        const vector<string>& anagram = pair.second;
        output.push_back(anagram);
    }
    return output;
}
