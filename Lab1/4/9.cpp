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
        if (!readInt(res[i])) { std::cout << "Not a number"; return false; }
    }
    return true;
}

void printIntArr(int arr[], int len)
{
    for (int i = 0; i < len; i++) std::cout << arr[i] << " ";
}

// Добавил аргумент arrLen -- длина массива arr
int* findAll(int arr[], int arrLen, int x, int &resultLen)
{
    int *result = new int[arrLen];
    resultLen = 0;
    for (int i = 0; i < arrLen; i++) 
        if (arr[i] == x) 
        {
            result[resultLen++] = i;
        }
    return result;
}

int main() 
{
    int arrLen, x, resultLen;
    int *arr, *result;

    std::cout << "Enter arr length: ";
    if (!readInt(arrLen) || arrLen < 0) { std::cout << "Wrong length"; return 0; }
    arr = new int[arrLen];
    if (!readIntArr(arr, arrLen)) goto die_arr; 

    std::cout << "x = ";
    if (!readInt(x)) { std::cout << "Not a number"; goto die_arr; } 

    result = findAll(arr, arrLen, x, resultLen);
    printIntArr(result, resultLen);
    
    delete[] result;
die_arr:
    delete[] arr;
    return 0;
}