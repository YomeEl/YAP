#include <iostream>
#include <string>

bool readInt(int &res)
{
    std::string s;
    std::cin >> s;
    try 
    {
        res = stoi(s);
    }
    catch(std::exception)
    {
        return false;
    }
    return true;
}

void rightTriangle(int x)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < x; j++) 
        {
            std::cout << (j >= x - i - 1 ? "*" : " ");
        }
        if (i + 1 < x) std::cout << "\n";
    }
}

int main()
{
    int x;
    std::cout << "x = ";
    if (!readInt(x)) { std::cout << "Not a number"; return 0; }
    if (x < 0) { std::cout << "x should be >= 0"; return 0; }
    rightTriangle(x);

    return 0;
}