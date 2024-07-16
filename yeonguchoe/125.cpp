// Time complexity: O(n^2)
// Space complexity :O(1)

bool isPalindrome(string s)
{
    int left = 0;
    int right = s.size() - 1;
    while (left < right)
    {
        while (left < right and
            (s[left] == ',' or s[left] == ' ' or s[left] == ':' or
                s[left] == '.' or s[left] == '@' || s[left] == '#' ||
                s[left] == '_' || s[left] == '\\' || s[left] == '{' ||
                s[left] == '}' || s[left] == '[' || s[left] == ']' ||
                s[left] == '(' || s[left] == ')' || s[left] == '"' ||
                s[left] == '\'' || s[left] == '-' || s[left] == '=' ||
                s[left] == '?' || s[left] == ';' || s[left] == '|' ||
                s[left] == '/' || s[left] == '!' || s[left] == '`'))
        {
            if (left < s.size() - 1)
            {
                left++;
            }
        }
        while (left < right and
            (s[right] == ',' or s[right] == ' ' or s[right] == ':' or
                s[right] == '.' or s[right] == '@' || s[right] == '#' ||
                s[right] == '_' || s[right] == '\\' || s[right] == '{' ||
                s[right] == '}' || s[right] == '[' || s[right] == ']' ||
                s[right] == '"' || s[right] == '\'' || s[right] == '(' ||
                s[right] == ')' || s[right] == '-' || s[right] == '=' ||
                s[right] == '?' || s[right] == ';' || s[right] == '|' ||
                s[right] == '/' || s[right] == '!' || s[right] == '`'))
        {
            right--;
        }
        char left_selected = s[left];
        char right_selected = s[right];
        if (isupper(left_selected))
        {
            left_selected = tolower(left_selected);
        }
        if (isupper(right_selected))
        {
            right_selected = tolower(right_selected);
        }
        if (left_selected != right_selected)
        {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
