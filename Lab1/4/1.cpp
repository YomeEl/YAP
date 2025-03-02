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

bool readIntArr(int res[], int n)
{
    for (int i = 0; i < n; i++)
    {
        std::cout << "[" << i << "]: ";
        if (!readInt(res[i])) { std::cout << "Not a number"; return false; } ;
    }
    return true;
}

// Добавил аргумент n -- длина массива arr
int findFirst(int arr[], int n, int x)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == x) return i;
    }
    return -1;
}

int main() 
{
    int len, x;
    std::cout << "Enter array length: ";
    if (!readInt(len) || len < 0) { std::cout << "Wrong length"; return 0; }
    int *arr = new int[len];
    if (!readIntArr(arr, len)) goto die; 
    std::cout << "x = ";
    if (!readInt(x)) { std::cout << "Not a number"; goto die; }

    std::cout << "first index of x is " << findFirst(arr, len, x);
die:
    delete[] arr;
    return 0;   
}