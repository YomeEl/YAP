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

bool isEqual(int a, int b, int c)
{
    return a == b && b == c;
}

int main()
{
    int a, b, c;
    std::cout << "a = ";
    if (!readInt(a)) { std::cout << "Not a number"; return 0; }
    std::cout << "b = ";
    if (!readInt(b)) { std::cout << "Not a number"; return 0; }
    std::cout << "c = ";
    if (!readInt(c)) { std::cout << "Not a number"; return 0; }

    bool res = isEqual(a, b, c);
    std::cout << a << ", " << b << " and " << c << " are " << (res ? "" : "not ") << "equal";
    return 0;
}