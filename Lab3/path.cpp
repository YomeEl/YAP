#include "path.h"

Path::Path() : _size(1), _count(0) 
{
    _points = new Point*[1];
}

Path::Path(Point **points, size_t count)
{
    _size = count;
    _points = new Point*[_size];
    _count = count;
    for (size_t i = 0; i < count; i++)
    {
        _points[i] = points[i];
    }
}

Path::~Path()
{
    delete[] _points;
}

void Path::append(Point *point)
{
    insert(point);
}

// returns nullptr on bad index
Point *Path::operator[](const size_t index)
{
    if (index >= _count) return nullptr;
    return _points[index];
}

size_t Path::count() const
{
    return _count;
}

Point *Path::first() const
{
    if (_count == 0) return nullptr;
    return _points[0];
}

Point *Path::last() const
{
    if (_count == 0) return nullptr;
    return _points[_count - 1];
}

std::wstring Path::print() const
{
    std::wstring result = L"[";
    for (size_t i = 0; i < _count; i++)
    {
        result += _points[i]->print() + L", ";
    }

    return result.substr(0, result.length() - 2) + L"]";
}

void Path::insert(Point *point)
{
    if (_count == _size) grow();
    _points[_count++] = point;
}

void Path::grow()
{
    Point ** newArray = new Point*[_size * 2];
    for (size_t i = 0; i < _count; i++)
    {
        newArray[i] = _points[i];
    }
    delete[] _points;
    _points = newArray;
    _size *= 2;
}
