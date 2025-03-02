#ifndef POINT_H
#define POINT_H

#include <string>

class Point
{
public:
    Point();
    Point(const Point &other);
    Point(double x, double y);

    double x() const;
    double y() const;

    void setX(double x);
    void setY(double y);
    
    std::wstring print() const;
    
private: 
    double _x;
    double _y;
};

#endif // !POINT_H
