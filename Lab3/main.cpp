#include <iostream>
#include <string>
#include <map>

#include "demos.h"

enum class Task
{ 
    Point, Line, Path, CreatePoint, CreateLine, LineLength, EXIT, ERR_TASK
};

std::map<Task, std::wstring> texts 
{
    { Task::Point, L"1\tТочка координат" },
    { Task::Line, L"2\tПрямая" },
    { Task::Path, L"3\tЛоманая" },
    { Task::CreatePoint, L"4.1\tСоздаём точку" },
    { Task::CreateLine, L"4.2\tСоздаём линию" },
    { Task::LineLength, L"5\tДлина линии" }
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
    case Task::Point: 
        demos::pointDemo();
        break;
    case Task::Line: 
        demos::lineDemo();
        break;
    case Task::Path: 
        demos::pathDemo();
        break;
    case Task::CreatePoint: 
        demos::createPointDemo();
        break;
    case Task::CreateLine: 
        demos::createLineDemo();
        break;
    case Task::LineLength: 
        demos::lineLengthDemo();
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
