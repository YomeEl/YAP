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
int maxAbs(int arr[], int n)
{
    int max = 0;
    for (int i = 0; i < n; i++)
    {
        int cur = abs(arr[i]);
        max = max > cur ? max : cur;
    }
    return max;
}

int main() 
{
    int len, x;
    std::cout << "Enter array length: ";
    if (!readInt(len) || len < 0) { std::cout << "Wrong length"; return 0; }
    int *arr = new int[len];
    if (!readIntArr(arr, len)) goto die;

    std::cout << "maxAbs(arr, len) = " << maxAbs(arr, len);
die:
    delete[] arr;
    return 0;   
}