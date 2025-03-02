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

std::wstring day(int x)
{
    switch (x)
    {
    case 1: return L"понедельник";
    case 2: return L"вторник";
    case 3: return L"среда";
    case 4: return L"четверг";
    case 5: return L"пятница";
    case 6: return L"суббота";
    case 7: return L"воскресенье";    
    }
    return L"это не день недели";
}

int main()
{
    setlocale(LC_ALL, "ru-RU");

    int x;
    std::cout << "x = ";
    if (!readInt(x)) { std::cout << "Not a number"; return 0; }
    std::wcout << L"day(x) = " << day(x);

    return 0;
}