
#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <numeric>

int main()
{
    std::vector<int> result;
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++)
    {
        std::string input_string;
        std::cin >> input_string;
        std::istringstream iss(input_string);
        int number;
        while (iss >> number)
        {
            result.push_back(number);
        }
    }
    std::cout << *std::copy(result.begin(), result.end(), std::ostream_iterator<int>(std