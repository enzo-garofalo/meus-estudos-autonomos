#include "shapes.h"
#include "shapesFactory.h"
#include "shapesDTO.h"
#include <iostream>

int main()
{
    std::cout << "Hello World.\n";

    // Triangle *obj = new Triangle(2.2, 1.2);
    // std::cout << obj->showBeatifulMessage()        << std::endl;
    // std::cout << obj->calculateArea()              << std::endl;
    // std::cout << obj->calculateTrianglePerimeter() << std::endl;
    // std::cout << "=============================="  << std::endl;
    // delete obj;
    
    // Rectangle *obj2 = new Rectangle(2, 8);
    // std::cout << obj2->showBeatifulMessage()         << std::endl;
    // std::cout << obj2->calculateArea()               << std::endl;
    // std::cout << obj2->calculateRectanglePerimeter() << std::endl;
    // std::cout << "=============================="    << std::endl;
    // delete obj2;

    // Circle *obj3 = new Circle(8);
    // std::cout << obj3->showBeatifulMessage()      << std::endl;
    // std::cout << obj3->calculateArea()            << std::endl;
    // std::cout << obj3->calculateCirclePerimeter() << std::endl;
    // std::cout << "==============================" << std::endl;
    // delete obj3;


    // Create a Circle object
    Circle circle(5.0);  // radius 5.0
    ShapesDTO circleDTO(circle);  // Convert Circle to ShapesDTO

    // Create a shape using the factory
    Shapes* circleShape = ShapesFactory::Create(circleDTO);
    if (circleShape != nullptr) {
        std::cout << "Circle created successfully!" << std::endl;
        std::cout << "Area of the circle: " << circleShape->calculateArea() << std::endl;
        delete circleShape;
    } else {
        std::cout << "Failed to create Circle." << std::endl;
    }

    // Create a Rectangle object
    Rectangle rectangle(4.0, 6.0);  // width 4.0, height 6.0
    ShapesDTO rectangleDTO(rectangle);  // Convert Rectangle to ShapesDTO

    // Create a shape using the factory
    Shapes* rectangleShape = ShapesFactory::Create(rectangleDTO);
    if (rectangleShape != nullptr) {
        std::cout << "Rectangle created successfully!" << std::endl;
        std::cout << "Area of the rectangle: " << rectangleShape->calculateArea() << std::endl;
        delete rectangleShape;
    } else {
        std::cout << "Failed to create Rectangle." << std::endl;
    }

    // Create a Triangle object
    Triangle triangle(4.0, 3.0);  // base 4.0, height 3.0
    ShapesDTO triangleDTO(triangle);  // Convert Triangle to ShapesDTO

    // Create a shape using the factory
    Shapes* triangleShape = ShapesFactory::Create(triangleDTO);
    if (triangleShape != nullptr) {
        std::cout << "Triangle created successfully!" << std::endl;
        std::cout << "Area of the triangle: " << triangleShape->calculateArea() << std::endl;
        delete triangleShape;
    } else {
        std::cout << "Failed to create Triangle." << std::endl;
    }

    return 0;
}