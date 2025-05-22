#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main()
{
    clock_t cock = clock();
    string line;
    int mul_coment_var_start;
    int mul_coment_var_close;
    bool mul_coment_var_state = false;
    int sin_coment_var;
    while (true)
    {
        if (kbhit())
        {
            getline(cin, line);
            mul_coment_var_start = line.find("/*");
            mul_coment_var_close = line.find("*/");
            sin_coment_var = line.find("//");
            if (line == "")
            {
                continue;
            }
            else if (sin_coment_var > 0)
            {
                cout << line.substr(0, sin_coment_var);
            }
            else if (mul_coment_var_state == false)
            {
                if (mul_coment_var_start != -1)
                {
                    if (mul_coment_var_start > 0)
                    {

                        cout << line.substr(0, mul_coment_var_start);
                        mul_coment_var_state = true;
                    }
                }
            }
            else
            {
                if (mul_coment_var_close != -1)
                {
                    if (line.substr(mul_coment_var_close).length() > 2)
                    {
                        cout << line.substr(mul_coment_var_close + 2);
                    }
                    mul_coment_var_state = true;
                }
            }
        }
    }
    return 0;
}
