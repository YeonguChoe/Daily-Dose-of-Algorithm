int canCompleteCircuit(vector<int>& gas, vector<int>& cost)
{
    int number_node = gas.size();
    for (int i = 0; i < number_node; i++)
    {
        int remaining_gas = gas[i];
        int current_node = i;

        do
        {
            remaining_gas = remaining_gas - cost[current_node];
            if (remaining_gas < 0)
            {
                break;
            }
            if (current_node >= number_node - 1)
            {
                current_node = 0;
            }
            else
            {
                current_node++;
            }

            if (current_node == i)
            {
                return current_node;
            }
            else
            {
                remaining_gas += gas[current_node];
            }
        }
        while (current_node != i);
    }
    return -1;
}
