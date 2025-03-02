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

int sum2(int x, int y)
{
    int sum = x + y;
    return isInRange(10, 19, sum) ? 20 : sum;
}

int main()
{
    int x, y;
    std::cout << "x = ";
    if (!readInt(x)) { std::cout << "Not a number"; return 0; }
    std::cout << "y = ";
    if (!readInt(y)) { std::cout << "Not a number"; return 0; }
    std::cout << "sum2(x, y) = " << sum2(x, y);

    return 0;
}