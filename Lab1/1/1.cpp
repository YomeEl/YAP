#include <iostream>
#include <math.h>
#include <string>

bool readDouble(double &res)
{
    std::string s;
    std::cin >> s;
    try 
    {
        res = stod(s);
    }
    catch(std::exception)
    {
        return false;
    }
    return true;
}

double fraction(double x)
{
    return x - trunc(x);
}

int main()
{
    double x;
    std::cout << "Enter your number: ";
    if (!readDouble(x)) 
    {
        std::cout << "Not a number";
        return 0;
    };
    
    std::cout << "Fraction: " << fraction(x);

    return 0;
}