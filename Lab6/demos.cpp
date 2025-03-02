#include "demos.h"

#include <iostream>
#include <fstream>
#include <string>
#include <locale>
#include <codecvt>

#include "list.h"
#include "linkedlist.h"
#include "hashset.h"
#include "dictionary.h"

void demos::listDemo() 
{
    auto intListToString = [](const List<int> &list) 
    {
        std::wstring result = L"[";

        auto cur = list.first();
        while (cur) 
        {
            result += std::to_wstring(cur->value) + L", ";
            cur = cur->next;
        }

        return result.substr(0, result.length() - 2) + L"]";
    };

    int arr[] {1, 2, 3, 4, 3, 7, 3}; 
    List<int> list(arr, 7);
    std::wcout << L"Начальный список: " << intListToString(list) << std::endl;
    list.remove(3);
    std::wcout << L"Список после удаления элемента {3}: " << intListToString(list) << std::endl;
}

void demos::linkedListDemo() 
{
    auto intListToString = [](const LinkedList<int> &list, bool reverse) 
    {
        std::wstring result = L"[";

        auto cur = reverse ? list.last() : list.first();
        while (cur) 
        {
            result += std::to_wstring(cur->value) + L", ";
            cur = reverse ? cur->prev : cur->next;
        }

        return result.substr(0, result.length() - 2) + L"]";
    };

    int arr[] {1, 2, 3, 4, 3, 7, 3}; 
    LinkedList<int> list(arr, 7);
    std::wcout << L"Начальный список: " << intListToString(list, false) << std::endl;
    std::wcout << L"Начальный список в обратном порядке: " << intListToString(list, true) << std::endl;
}

#define print_set(set, delim, fnc) auto buf_##set = set.toArray();\
std::wstring str_##set = L"{ ";\
for (size_t i = 0; i < set.count(); i++) str_##set += fnc(buf_##set[i]) + delim;\
if (set.count() > 0) str_##set = str_##set.substr(0, str_##set.length() - std::wstring(delim).length());\
std::wcout << str_##set << L" }";\
delete[] buf_##set;

#define IDENT

void demos::hashSet1Demo() 
{
    std::wstring companiesArr[] { L"C1", L"C2", L"C3", L"C4", L"C5", L"C6", L"C7" };
    HashSet companies(companiesArr, 7);
    std::wstring school1CompaniesArr[] { L"C1", L"C2", L"C7" };
    HashSet school1Companies(school1CompaniesArr, 3);
    std::wstring school2CompaniesArr[] { L"C2", L"C3", L"C7" };
    HashSet school2Companies(school2CompaniesArr, 3);
    std::wstring school3CompaniesArr[] { L"C3", L"C4", L"C7" };
    HashSet school3Companies(school3CompaniesArr, 3);

    std::wcout << L"Компании: ";
    print_set(companies, L", ", IDENT);
    std::wcout << L"\nКомпании, в которых закупалась школа 1: ";
    print_set(school1Companies, L", ", IDENT);
    std::wcout << L"\nКомпании, в которых закупалась школа 2: ";
    print_set(school2Companies, L", ", IDENT);
    std::wcout << L"\nКомпании, в которых закупалась школа 3: ";
    print_set(school3Companies, L", ", IDENT);
    std::wcout << std::endl;

    auto intersectAll = school1Companies.Intersect(school2Companies).Intersect(school3Companies);
    auto unionAll = school1Companies.Union(school2Companies).Union(school3Companies);
    auto allExceptUnionAll = companies.Except(unionAll);

    std::wcout << L"\nКомпании, в которых закупка производилась каждой школой: ";
    print_set(intersectAll, L", ", IDENT);
    std::wcout << L"\nКомпании, в которых закупка производилась хотя бы одной из школ: ";
    print_set(unionAll, L", ", IDENT);
    std::wcout << L"\nКомпании, в которых закупка не производилась ни одной из школ: ";
    print_set(allExceptUnionAll, L", ", IDENT);
    std::wcout << std::endl;
}

void demos::hashSet2Demo() 
{
    // read file
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;

    const std::string filename = "hashSet2Demo.txt";
    std::ifstream file(filename);
    std::string buf;
    std::wstring content = L"";
    while (file >> buf) content += (converter.from_bytes(buf));
    
    // convert to lowercase and append into set
    HashSet<wchar_t> textLetters;
    for (size_t i = 0; i < content.length(); i++)
    {
        wchar_t ch = content[i];
        if (ch >= L'А' && ch <= L'Я') ch = ch - L'А' + L'а';
        textLetters.append(ch);
    }

    // set of letters to filter
    wchar_t lettersArr[] = { L'б', L'в', L'г', L'д', L'ж', L'з', L'л', L'м', L'н', L'р' };
    HashSet letters(lettersArr, 10);

    auto intersection = letters.Intersect(textLetters);
    std::wcout << L"Буквы, входящие хотя бы в одно слово в файле ";
    std::cout << filename << ":\n\t";
    print_set(intersection, L", ", std::wstring(L"") + IDENT);
    std::cout << std::endl;
}

#undef print_set
#undef IDENT

void demos::dictionaryDemo() 
{
    Dictionary<std::wstring, std::wstring, 100> usernames;
    Dictionary<std::wstring, size_t, 100> counts;

    std::wcout << L"Введите количество учеников N, а затем N строк вида {имя} {фамилия}: ";

    size_t n;
    std::cin >> n;
    for (size_t i = 0; i < n; i++)
    {
        std::wstring name, surname, fullName, username;
        std::wcin >> surname >> name;
        fullName = surname + L" " + name;
        username = surname;
        size_t count = counts[surname]++;
        if (count > 0) username += std::to_wstring(count + 1);
        usernames.append(fullName, username);
    }

    std::wcout << L"Имя\tЛогин\n";
    auto pairs = usernames.pairs();
    for (size_t i = 0; i < usernames.count(); i++)
    {
        std::wcout << pairs[i].key << L"\t" << pairs[i].value << std::endl;
    }
    delete[] pairs;
}
