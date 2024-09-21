#include <iostream>
#include <string>
#include <algorithm>

int main()
{
    int Len_of_Char, n_operation;
    std::string character;

    std::cin >> Len_of_Char >> n_operation;
    std::cin >> character;

    for (int i = 0; i < n_operation; i++)
    {
        std::string operation;
        std::getline(std::cin, operation);
        std::istringstream iss(operation);
        std::string op;
        iss >> op;

        if (op == "substr")
        {
            int l, r;
            iss >> l >> r;
            std::string new_str = character.substr(l - 1, r - l + 1);
            std::cout << new_str << std::endl;
        }
        else if (op == "sort")
        {
            int l, r;
            iss >> l >> r;
            std::string new_str = character.substr(0, l) + std::string(std::begin(character) + l, std::begin(character) + r);
            std::sort(new_str.begin() + l, new_str.begin() + r);
            character = new_str;
        }
        else if (op == "reverse")
        {
            int l, r;
            iss >> l >> r;
            std::string new_str = character.substr(0, l - 1) + std::string(std::rbegin(character) + (Len_of_Char - r), std::rbegin(character) + (Len_of_Char - l + 1)) + character.substr(r);
            character = new_str;
        }
        else if (op == "push_back")
        {
            std::string s;
            iss >> s;
            character += s;
        }
        else if (op == "print")
        {
            int index;
            iss >> index;
            std::cout << character[index] << std::endl;
        }
        else if (op == "pop_back")
        {
            character.pop_back();
        }
        else if (op == "back")
        {
            std::cout << character.back() << std::endl;
        }
        else if (op == "front")
        {
            std::cout << character.front() << std::endl;
        }
    }

    return 0;
}
