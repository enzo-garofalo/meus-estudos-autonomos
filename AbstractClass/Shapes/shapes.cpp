#include "shapes.h"


Shapes::Shapes(double m_positionX, double m_positionY,  bool m_isTridimensional){};

Shapes::~Shapes() {};

Shapes::Shapes(const Shapes &cp)
{
    m_positionX = cp.m_positionX;
    m_positionY = cp.m_positionY;
    m_isTridimensional = cp.m_isTridimensional;
};

Shapes& Shapes::operator=(const Shapes& cp)
{
    m_positionX = cp.m_positionX;
    m_positionY = cp.m_positionY;
    m_isTridimensional = cp.m_isTridimensional;
    return *this;
};

// Circle
Circle::Circle(double radius) : Shapes(0.0, 0.0, false), m_radius(radius) {};

Circle::~Circle() {};

// Rectangle
Rectangle::Rectangle(double width, double height): Shapes(0.0, 0.0, false), m_width(width), m_height(height) {};

Rectangle::~Rectangle() {};

// Triangle
Triangle::Triangle(double base, double height) : Shapes(0.0, 0.0, false), m_base(base), m_height(height) {};

Triangle::~Triangle() {};

