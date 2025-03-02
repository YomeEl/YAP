#ifndef PATH_H
#define PATH_H

#include <string>
#include "point.h"

// Doesn't take ownership
class Path
{
public:
    Path();
    Path(Point **points, size_t count);

    ~Path();
    
    void append(Point *point);
    void append(Point **points, size_t count);
    
    Point* operator[](const size_t index);
    size_t count() const;

    Point* first() const;
    Point* last() const;

    double length() const;

    std::wstring print() const;

private:
    void insert(Point *point);
    void grow();

private:
    size_t _size;
    size_t _count;
    Point **_points;
};

#endif // !PATH_H