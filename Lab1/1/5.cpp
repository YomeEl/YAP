#include <iostream>
#include <string>
#include <math.h>

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

// Двузначным принимаем число, в записи которого две цифры
// Например, -55 -- двузначное
bool is2Digits(int n)
{
    n = abs(n);
    return n > 9 && n < 100;
}

int main()
{
    int n;
    std::cout << "Enter your number: ";
    if (!readInt(n))
    {
        std::cout << "Not a number";
        return 0;
    }
    std::cout << (is2Digits(n) ? "Two digits" : "Not two digits");
    return 0;
}