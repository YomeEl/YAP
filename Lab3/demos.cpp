#include "demos.h"

#include "point.h"
#include "line.h"
#include "path.h"

#include <iostream>

void demos::pointDemo()
{
    Point a(1, 1);
    Point b(2, 2);
    Point c(3, 3);

    std::wcout << L"A: " << a.print() << L"\nB: " << b.print() << L"\nC: " << c.print() << std::endl;
}

void demos::lineDemo()
{
    Point line1From(1, 3);
    Point line1To(23, 8);
    Point line2From(5, 10);
    Point line2To(25, 10);

    Line line1(&line1From, &line1To);
    Line line2(&line2From, &line2To);
    Line line3(&line1From, &line2To);

    std::wcout << L"Начальное состояние линий" << std::endl;

    std::wcout 
        << L"\t1: " << line1.print() 
        << L"\n\t2: " << line2.print() 
        << L"\n\t3: " << line3.print() << std::endl;

    std::wcout << L"Сдвигаем начало первой линии в точку (2, 4)" << std::endl;
    line1.from()->setX(2);
    line1.from()->setY(4);

    std::wcout << L"Сдвигаем конец второй линии в точку (30, 15)" << std::endl;
    line2.to()->setX(30);
    line2.to()->setY(15);

    std::wcout 
        << L"\t1: " << line1.print() 
        << L"\n\t2: " << line2.print() 
        << L"\n\t3: " << line3.print() << std::endl;

    std::wcout << L"Сдвигаем конец первой линии в точку (5, 5)" << std::endl;
    line1.to()->setX(5);
    line1.to()->setY(5);

    std::wcout 
        << L"\t1: " << line1.print() 
        << L"\n\t2: " << line2.print() 
        << L"\n\t3: " << line3.print() << std::endl;
}

void demos::pathDemo()
{
    Point pBegin(1, 5);
    Point pEnd(5, 3);

    Point pFirstCenter(2, 8);
    Point pSecondCenter1(2, -5);
    Point pSecondCenter2(4, -8);

    Path path1;
    path1.append(&pBegin);
    path1.append(&pFirstCenter);
    path1.append(&pEnd);

    Path path2;
    path2.append(&pBegin);
    path2.append(&pSecondCenter1);
    path2.append(&pSecondCenter2);
    path2.append(&pEnd);

    std::wcout << L"Начальное состояние ломаных\n";
    std::wcout << L"\t1: " << path1.print() << L"\n\t2: " << path2.print() << std::endl;

    std::wcout << L"Сдвигаем начало первой ломаной в точку {0, 1}\n";
    path1.first()->setX(0);
    path1.first()->setY(1);
    std::wcout << L"\t1: " << path1.print() << L"\n\t2: " << path2.print() << std::endl;
}

void demos::createPointDemo()
{
    Point a(3, 5);
    std::wcout << a.print() << std::endl;
    Point b(25, 6);
    std::wcout << b.print() << std::endl;
    Point c(7, 8);
    std::wcout << c.print() << std::endl;
}

void demos::createLineDemo()
{
    Line line1(1, 3, 23, 8);
    Line line2(5, 10, 25, 10);
    Line line3(line1.from(), line2.to());

    std::wcout << L"Начальное состояние линий" << std::endl;

    std::wcout 
        << L"\t1: " << line1.print() 
        << L"\n\t2: " << line2.print() 
        << L"\n\t3: " << line3.print() << std::endl;

    std::wcout << L"Сдвигаем начало первой линии в точку (2, 4)" << std::endl;
    line1.from()->setX(2);
    line1.from()->setY(4);

    std::wcout << L"Сдвигаем конец второй линии в точку (30, 15)" << std::endl;
    line2.to()->setX(30);
    line2.to()->setY(15);

    std::wcout 
        << L"\t1: " << line1.print() 
        << L"\n\t2: " << line2.print() 
        << L"\n\t3: " << line3.print() << std::endl;

    std::wcout << L"Сдвигаем конец первой линии в точку (5, 5)" << std::endl;
    line1.to()->setX(5);
    line1.to()->setY(5);

    std::wcout 
        << L"\t1: " << line1.print() 
        << L"\n\t2: " << line2.print() 
        << L"\n\t3: " << line3.print() << std::endl;
}

void demos::lineLengthDemo()
{
    Line line(1,1,10,15);
    std::wcout << line.print() << std::endl;
    std::wcout << L"Длина линии: " << line.length() << std::endl;
    std::wcout << L"Целая часть длины линии: " << line.truncatedLength() << std::endl;
}
