#include "point.h"

Point::Point() : _x(0), _y(0) {}

Point::Point(const Point &other)
{
    _x = other._x;
    _y = other._y;
}

Point::Point(double x, double y) : _x(x), _y(y) {}

double Point::x() const
{
    return _x;
}
double Point::y() const
{
    return _y;
}

void Point::setX(double x)
{
    _x = x;
}
void Point::setY(double y)
{
    _y = y;
}

std::wstring Point::print() const
{
    return L"{" + std::to_wstring(_x) + L", " + std::to_wstring(_y) + L"}";
}