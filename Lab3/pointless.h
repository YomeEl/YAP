#ifndef POINTLESS_H
#define POINTLESS_H

#include <string>

class PointLess
{
public:
    PointLess(double x, double y);

    double x() const;
    double y() const;

    void setX(double x);
    void setY(double y);
    
    std::wstring print() const;
    
private: 
    double _x;
    double _y;
};

#endif // !POINTLESS_H
