#include <iostream>
#include <string>

bool readLong(long &res)
{
    std::string s;
    std::cin >> s;
    try 
    {
        res = stol(s);
    }
    catch(std::exception)
    {
        return false;
    }
    return true;
}

int numLen(long x)
{
    int len = 0;
    while (x > 0)
    {
        len++;
        x /= 10;
    }
    return len;
}

int main()
{
    long x;
    std::cout << "x = ";
    if (!readLong(x)) { std::cout << "Not a number"; return 0; }
    std::cout << "numLen(x) = " << numLen(x);

    return 0;
}