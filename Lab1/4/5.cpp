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

void printIntArr(int arr[], int len)
{
    for (int i = 0; i < len; i++) std::cout << arr[i] << " ";
}

// Добавил аргументы arrLen, insLen -- длины массивов
int* add(int arr[], int arrLen, int ins[], int insLen, int pos)
{
    if (pos < 0 || pos > arrLen)
    {
        std::cout << "Wrong pos!";
        return nullptr;
    }

    int *res = new int[arrLen + insLen];
    for (int i = 0; i < pos; i++) res[i] = arr[i];
    for (int i = 0; i < insLen; i++) res[pos + i] = ins[i];
    for (int i = 0; i < arrLen - pos; i++) res[pos + insLen + i] = arr[pos + i];
    return res;
}

int main() 
{
    int arrLen, insLen, pos;
    int *arr, *ins, *result;

    std::cout << "Enter arr length: ";
    if (!readInt(arrLen) || arrLen < 0) { std::cout << "Wrong length"; return 0; }
    arr = new int[arrLen];
    if (!readIntArr(arr, arrLen)) goto die_arr; 

    std::cout << "Enter ins length: ";
    if (!readInt(insLen) || insLen < 0) { std::cout << "Wrong length"; return 0; }
    ins = new int[insLen];
    if (!readIntArr(ins, insLen)) goto die_ins;

    std::cout << "pos = ";
    if (!readInt(pos)) { std::cout << "Not a number"; goto die_ins; }


    result = add(arr, arrLen, ins, insLen, pos);
    if (!result) goto die_res;
    printIntArr(result, arrLen + insLen);
    
die_res:
    delete[] result;
die_ins:
    delete[] ins;
die_arr:
    delete[] arr;
    return 0;   
}