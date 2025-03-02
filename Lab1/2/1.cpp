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

int abs(int x)
{
    return x < 0 ? -x : x;
}

int main()
{
    int x;
    std::cout << "x = ";
    if (!readInt(x)) { std::cout << "Not a number"; return 0; }
    std::cout << "abs(" << x << ") = " << abs(x);

    return 0;
}