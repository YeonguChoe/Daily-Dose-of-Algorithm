// Time complexity: O(n)
// Space complexity: O(1)
int romanToInt(string s)
{
    int result = 0;
    int pointer = 0;
    while (pointer < s.size())
    {
        if (s[pointer] == 'I')
        {
            if (s[pointer + 1] == 'V')
            {
                pointer += 2;
                result += 4;
            }
            else if (s[pointer + 1] == 'X')
            {
                pointer += 2;
                result += 9;
            }
            else
            {
                pointer += 1;
                result += 1;
            }
        }
        else if (s[pointer] == 'X')
        {
            if (s[pointer + 1] == 'L')
            {
                pointer += 2;
                result += 40;
            }
            else if (s[pointer + 1] == 'C')
            {
                pointer += 2;
                result += 90;
            }
            else
            {
                pointer += 1;
                result += 10;
            }
        }
        else if (s[pointer] == 'C')
        {
            if (s[pointer + 1] == 'D')
            {
                pointer += 2;
                result += 400;
            }
            else if (s[pointer + 1] == 'M')
            {
                pointer += 2;
                result += 900;
            }
            else
            {
                pointer += 1;
                result += 100;
            }
        }
        else
        {
            if (s[pointer] == 'V')
            {
                pointer += 1;
                result += 5;
            }
            else if (s[pointer] == 'L')
            {
                pointer += 1;
                result += 50;
            }
            else if (s[pointer] == 'D')
            {
                pointer += 1;
                result += 500;
            }
            else if (s[pointer] == 'M')
            {
                pointer += 1;
                result += 1000;
            }
        }
    }
    return result;
}

// // Left Pass Soluion
// int romanToInt(string s)
// {
//     unordered_map<char, int> v = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
//     int result = 0;
//     int i = 0;
//     while (i < s.size())
//     {
//         if (i <= s.size() - 2 and v[s[i]] < v[s[i + 1]])
//         {
//             result += v[s[i + 1]];
//             result -= v[s[i]];
//             i += 2;
//         }
//         else
//         {
//             result += v[s[i]];
//             i += 1;
//         }
//     }
//     return result;
// }
