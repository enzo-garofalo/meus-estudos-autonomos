#include "shapesDTO.h"
#include "json.h"

ShapesDTO::ShapesDTO(const Json::Value &Root)
{
    s_dt_positionX = shape.GetM_positionX();
    s_dt_positionY = shape.GetM_positionY();
    s_dt_isTridimensional = shape.IsTridimensional();
    s_dt_radius = 0.0;
    s_dt_base = 0.0;
    s_dt_height = 0.0;
    s_dt_width = 0.0;


    if( const Circle *circle = dynamic_cast<const Circle *>(&shape))
    {
        s_dt_type = "Circle";
        s_dt_radius = circle->GetRadius();
    }
    else if (const Rectangle *rectangle = dynamic_cast<const Rectangle *>(&shape)) {
        s_dt_type = "Rectangle";
        s_dt_width = rectangle->GetWidth();
        s_dt_height = rectangle->GetHeight();  
    }
    else if (const Triangle *triangle = dynamic_cast<const Triangle *>(&shape)) {
        s_dt_type = "Triangle";
        s_dt_base =  triangle->GetBase();
        s_dt_height = triangle->GetHeight();  
    }
    else {
        s_dt_type = "Unknown Shape";
    }
};

ShapesDTO::~ShapesDTO() {};

ShapesDTO::ShapesDTO( const ShapesDTO &cp)
{
    s_dt_type = cp.s_dt_type;
    s_dt_positionX = cp.s_dt_positionX;
    s_dt_positionY = cp.s_dt_positionY;
    s_dt_isTridimensional = cp.s_dt_isTridimensional;
    s_dt_radius = cp.s_dt_radius;
    s_dt_width = cp.s_dt_width;
    s_dt_height = cp.s_dt_height;
    s_dt_base = cp.s_dt_base;
}

ShapesDTO& ShapesDTO::operator=(const ShapesDTO& cp)
{
    s_dt_type = cp.s_dt_type;
    s_dt_positionX = cp.s_dt_positionX;
    s_dt_positionY = cp.s_dt_positionY;
    s_dt_isTridimensional = cp.s_dt_isTridimensional;
    s_dt_radius = cp.s_dt_radius;
    s_dt_width = cp.s_dt_width;
    s_dt_height = cp.s_dt_height;
    s_dt_base = cp.s_dt_base;
    return *this;
};