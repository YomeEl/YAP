#include <iostream>

int charToNum(char x)
{
    if (x < '0' || x > '9') return -1;
    return x - '0';
}

int main() {
    char x;
    std::cout << "Enter digit: ";
    std::cin >> x;
    
    int res = charToNum(x);
    if (res == -1) 
    {
        std::cout << "Character is not a digit!";
        return 0;
    }
    
    std::cout << "Digit is " << res;
    return 0;
}