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

bool is35(int x)
{
    int sum = (x % 3 == 0) + (x % 5 == 0);
    return sum == 1;
}

int main()
{
    int x;
    std::cout << "x = ";
    if (!readInt(x)) { std::cout << "Not a number"; return 0; }
    std::cout << "is35(" << x << ") = " << (is35(x) ? "true" : "false");

    return 0;
}