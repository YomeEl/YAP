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

int max3(int x, int y, int z)
{
    int sub = x > y ? x : y;
    return sub > z ? sub : z;
}

int main()
{
    int x, y, z;
    std::cout << "x = ";
    if (!readInt(x)) { std::cout << "Not a number"; return 0; }
    std::cout << "y = ";
    if (!readInt(y)) { std::cout << "Not a number"; return 0; }
    std::cout << "z = ";
    if (!readInt(z)) { std::cout << "Not a number"; return 0; }
    std::cout << "max3(x, y, z) = " << max3(x, y, z);

    return 0;
}
