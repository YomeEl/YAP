#include "pointless.h"

PointLess::PointLess(double x, double y) : _x(x), _y(y) {}

double PointLess::x() const
{
    return _x;
}
double PointLess::y() const
{
    return _y;
}

void PointLess::setX(double x)
{
    _x = x;
}
void PointLess::setY(double y)
{
    _y = y;
}

std::wstring PointLess::print() const
{
    return L"{" + std::to_wstring(_x) + L", " + std::to_wstring(_y) + L"}";
}