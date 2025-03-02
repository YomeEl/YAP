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

std::string listNums(int x)
{
    int left = x < 0 ? x : 0;
    int right = x > 0 ? x : 0;
    std::string result;
    
    for (int i = left; i <= right; i++)
    {
        result += std::to_string(i) + ' ';
    }
    return result.substr(0, result.length() - 1);
}

int main()
{
    int x;
    std::cout << "x = ";
    if (!readInt(x)) { std::cout << "Not a number"; return 0; }
    std::cout << "listNums(x) = " << listNums(x);

    return 0;
}