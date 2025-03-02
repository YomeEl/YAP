#include <iostream>
#include <string>
#include <map>

#include "demos.h"

enum class Task
{ 
    List, LinkedList, HashSet1, HashSet2, Dictionary, EXIT, ERR_TASK
};

std::map<Task, std::wstring> texts 
{
    { Task::List, L"1\tList" },
    { Task::LinkedList, L"2\tLinkedList" },
    { Task::HashSet1, L"3\tHashSet 1" },
    { Task::HashSet2, L"4\tHashSet 2" },
    { Task::Dictionary, L"5\tDictionary" },
};

Task selectTask(const std::wstring selection)
{
    if (selection == L"-1") return Task::EXIT;
    for (const auto &pair : texts)
    {
        size_t tabIndex = pair.second.find(L"\t");
        if (pair.second.substr(0, tabIndex) == selection) return pair.first;
    }
    return Task::ERR_TASK;
}

std::wstring showMainPage()
{
    std::wcout << L"Номер\tНазвание\n";
    for (const auto &pair : texts)
    {
        std::wcout << pair.second << std::endl;
    }
    std::wcout << L"Введите номер задачи или -1, чтобы выйти: ";
    std::wstring selection;
    std::wcin >> selection;
    return selection;
}

void runDemo(Task task)
{
    switch (task)
    {
    case Task::List: 
        demos::listDemo();
        break;
    case Task::LinkedList: 
        demos::linkedListDemo();
        break;
    case Task::HashSet1: 
        demos::hashSet1Demo();
        break;
    case Task::HashSet2: 
        demos::hashSet2Demo();
        break;
    case Task::Dictionary: 
        demos::dictionaryDemo();
        break;
    default: 
        return;
    }
    system("pause");
}

int main()
{
    system("chcp 1251");
    setlocale(LC_ALL, "ru-RU");

    while (true)
    {
        std::wstring selection = showMainPage();
        Task task = selectTask(selection);
        if (task == Task::EXIT) break;
        runDemo(task);
    }

    return 0;
}
