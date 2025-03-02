#include "line.h"

#include <math.h>

Line::Line(Point* from, Point* to) : _from(from), _to(to), _ownsFrom(false), _ownsTo(false) {}

Line::Line(double x1, double y1, double x2, double y2) : _ownsFrom(true), _ownsTo(true)
{
    _from = new Point(x1, y1);
    _to = new Point(x2, y2);
}

Line::~Line()
{
    if (_ownsFrom) delete _from;
    if (_ownsTo) delete _to;
}

Point* Line::from() const
{
    return _from;
}

Point* Line::to() const
{
    return _to;
}

void Line::setFrom(Point* from)
{
    _from = from;
}

void Line::setTo(Point* to)
{
    _to = to;
}

#define sqr(x) (x) * (x)
double Line::length() const
{
    return sqrt(sqr(_from->x() - _to->x()) + sqr(_from->y() - _to->y()));
}
#undef sqr

size_t Line::truncatedLength() const
{
    return static_cast<size_t>(length());
}

std::wstring Line::print()
{
    return L"Линия от " + _from->print() + L" до " + _to->print();
}
