#ifndef SHAPESDTO_H
#define SHAPESDTO_H

#include "shapes.h"
#include <iostream>

class ShapesDTO
{
protected:
    // Shapes attrs
    std::string s_dt_type;
    double s_dt_positionX;
    double s_dt_positionY;
    bool s_dt_isTridimensional;
    
    double s_dt_radius; // Circle attrs
    double s_dt_width, s_dt_height; // Rectangle attrs
    double s_dt_base; // Triangle attrs

public:
    ShapesDTO();
    
    ~ShapesDTO();

    ShapesDTO( const Shapes &cp);

    ShapesDTO& operator= (const ShapesDTO& cp);

public:
    // getters
    inline std::string GetType() const { return s_dt_type; }
    inline double GetPositionX() const { return s_dt_positionX; }
    inline double GetPositionY() const { return s_dt_positionY; }
    inline bool   IsTridimensional() const { return s_dt_isTridimensional; }
    
    inline double GetRadius() const { return s_dt_radius; }
    inline double GetWidth() const { return s_dt_width; }
    inline double GetHeight() const { return s_dt_height; }
    inline double GetBase() const { return s_dt_base; } 

};


#endif