#ifndef SHAPE_FACTORY_H
#define SHAPE_FACTORY_H

#include "shapes.h"
#include "shapesDTO.h"


class ShapesFactory
{
    
private:
    static bool Validate(ShapesDTO &shapeDTO)
    {
        const std::string typeName = shapeDTO.GetType();
        if(typeName == "Circle")
        {  
            if(shapeDTO.GetRadius()>0)
            {
                throw(std::bad_exception());
            }
        }
        else if(typeName == "Rectange")
        {
            shapeDTO.GetWidth() > 0 && shapeDTO.GetHeight() > 0
        }
        else if(typeName == "Triangle")
        {
            
        }
        else{
            std::cout << "Invalid Type.\n";
            throw(std::bad_exception());
        }

        if (shapeDTO.GetType() == "Circle" && shapeDTO.GetRadius() > 0)
            return  new Circle(shapeDTO.GetRadius());
        
        if (shapeDTO.GetType() == "Rectangle" && shapeDTO.GetWidth() > 0 && shapeDTO.GetHeight() > 0)
            return new Rectangle(shapeDTO.GetWidth(), shapeDTO.GetHeight());
        
        if (shapeDTO.GetType() == "Triangle" && shapeDTO.GetBase() > 0 && shapeDTO.GetHeight() > 0)
            return new Triangle(shapeDTO.GetBase(), shapeDTO.GetHeight());
        
            MESSAGE
        throw(std::bad_exception());
            
        return nullptr; 
    };

public:
    static Shapes* Create(ShapesDTO &shapeDTO)
    {
        Shapes * shape = Validate(shapeDTO);
        return shape;

    };
};


#endif