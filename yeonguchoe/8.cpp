int myAtoi(string s)
{
    stack<int> cache;

    bool checked_first_number = false;
    bool is_positive = true;
    bool zero_was_previous = false;
    bool sign_exist = false;


    for (char c : s)
    {
        if (!checked_first_number)
        {
            if (c == ' ')
            {
                if (zero_was_previous)
                {
                    return 0;
                }

                continue;
            }
            if (c == '0')
            {
                zero_was_previous = true;
                continue;
            }
            if (c == '-')
            {
                if (zero_was_previous)
                {
                    return 0;
                }
                is_positive = false;
                checked_first_number = true;
                sign_exist = true;
            }
            else if (c == '+')
            {
                if (zero_was_previous)
                {
                    return 0;
                }
                is_positive = true;
                checked_first_number = true;
                sign_exist = true;
            }
            else if (c != 0 and isdigit(c))
            {
                int n = static_cast<int>(c - '0');
                cache.push(n);
                checked_first_number = true;
            }
            else
            {
                return 0;
            }
        }
        else
        {
            if (sign_exist and c == '0')
            {
                continue;
            }

            if (isdigit(c))
            {
                int n = static_cast<int>(c - '0');
                cache.push(n);
                sign_exist = false;
            }
            else
            {
                break;
            }
        }
    }

    if (cache.size() > 10)
    {
        if (is_positive)
        {
            return INT_MAX;
        }
        else
        {
            return INT_MIN;
        }
    }

    unsigned long long temporary_number = 0ULL;

    int degree = 0;
    while (!cache.empty())
    {
        temporary_number += (cache.top() * pow(10, degree));
        cache.pop();
        degree++;
    }
    if (is_positive and temporary_number >= INT_MAX)
    {
        return INT_MAX;
    }
    if (!is_positive and
        temporary_number >= (-1 * static_cast<uint64_t>(INT_MIN)))
    {
        return INT_MIN;
    }

    int result = static_cast<int>(temporary_number);

    if (!is_positive)
    {
        result *= (-1);
    }

    return result;
}
