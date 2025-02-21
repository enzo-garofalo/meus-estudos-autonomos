#ifndef SHAPES_H
#define SHAPES_H

#include <iostream>

class Shapes
{
protected: // attrs
    double m_positionX, m_positionY;
    bool m_isTridimensional;

public: 
    Shapes(double m_positionX, double m_positionY,  bool m_isTridimensional); // Constructor

    ~Shapes(); // Destructor
    
    Shapes(const Shapes &cp);

    Shapes& operator= (const Shapes& cp);

public: // abstracts methods 
    virtual double calculateArea() const = 0;
    virtual std::string showBeatifulMessage() const =0;   

public: 
    // getters 
    bool IsTridimensional() const { return m_isTridimensional; }
    double GetM_positionX() const { return m_positionX; }
    double GetM_positionY() const { return m_positionY; }

    // setters
    void SetTridimensional(bool t) { m_isTridimensional = t; }
    void SetM_positionX(double x) { m_positionX = x; }
    void SetM_positionY(double y) { m_positionY = y; }
};

class Circle : public Shapes
{
public:
    Circle(double m_radius);
    ~Circle();

protected:
    double m_radius;

public:
    double GetRadius() const { return m_radius; }
    void SetRadius(double r) { m_radius = r; }

public:

    double calculateArea() const override
    {
        return 3.1415 * m_radius * m_radius;
    };

    std::string showBeatifulMessage() const override
    {
        return "Thats your circle -> o";
    };

    // CIRCLE method
    double calculateCirclePerimeter()
    {
        return 3.1415 * (2*m_radius);
    };
};

class Rectangle : public Shapes
{
public:
    Rectangle(double m_width, double m_height);
    ~Rectangle();

protected:
    double m_width, m_height;

public:
    // Getters
    double GetWidth() const { return m_width; }
    double GetHeight() const { return m_height; }

    // Setters
    void SetWidth(double width) { m_width = width; }
    void SetHeight(double height) { m_height = height; }


public:
    double calculateArea() const override
    {
        return m_width * m_height;
    }

    std::string showBeatifulMessage() const override
    {
        return "That's your rectangle -> []";
    }

    //Rectangle method
    double calculateRectanglePerimeter()
    {
        return (2*m_width) + (2*m_height);
    }
};

class Triangle : public Shapes
{
public:
    Triangle(double m_base, double m_height);
    ~Triangle();

protected:
    double m_base, m_height;

public:
    // Getters
    double GetBase() const { return m_base; }
    double GetHeight() const { return m_height; }

    // Setters
    void SetBase(double base) { m_base = base; }
    void SetHeight(double height) { m_height = height; }

public:
    double calculateArea() const override
    {
        return 0.5 * m_base * m_height;
    };

    std::string showBeatifulMessage() const override
    {
        return "That's your triangle -> △";
    };

    double calculateTrianglePerimeter()
    {
        return 7;
    };
};

#endif