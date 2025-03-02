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

bool isInRange(int a, int b, int num)
{
    int left = a < b ? a : b;
    int right = a > b ? a : b;
    return num >= left && num <= right;
}

int main()
{
    int a, b, num;
    std::cout << "a = ";
    if (!readInt(a)) { std::cout << "Not a number"; return 0; }
    std::cout << "b = ";
    if (!readInt(b)) { std::cout << "Not a number"; return 0; }
    std::cout << "num = ";
    if (!readInt(num)) { std::cout << "Not a number"; return 0; }

    std::cout << "num is " << (isInRange(a, b, num) ? "" : "not ") << "in range";
    return 0;
}