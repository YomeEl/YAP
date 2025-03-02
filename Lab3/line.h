#ifndef LINE_H
#define LINE_H

#include <string>
#include "point.h"

// Does't take ownership
class Line
{
public:
    Line(Point* from, Point* to);
    Line(double x1, double y1, double x2, double y2);

    ~Line();

    Point* from() const;
    Point* to() const;

    void setFrom(Point* from);
    void setTo(Point* to);

    double length() const;
    size_t truncatedLength() const; 

    std::wstring print();

private:
    Point* _from;
    Point* _to;

    bool _ownsFrom;
    bool _ownsTo;
};

#endif // !LINE_H