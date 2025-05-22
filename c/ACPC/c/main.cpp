
#include <bits/stdc++.h>

int main() {
    int j;
    std::cin >> j;
    std::string character;
    std::cin >> character;
    std::string result = "";
    for (int i = 97; i < (97 + 26); i++) {
        char char_items = static_cast<char>(i);
        int count = 0;
        if (character.find(char_items) != std::string::npos) {
            for (char k : character) {
                if (k == char_items) {
                    count++;
                }
            }
        } else {
            continue;
        }
        character.erase(std::remove(character.begin(), character.end(), char_items), character.end());
        for (int m = 0; m < count; m++) {
            result += char_items;
        }
        if (character.empty()) {
            break;
        }
    }
    std::cout << result << std::endl;
    return 0;
}

