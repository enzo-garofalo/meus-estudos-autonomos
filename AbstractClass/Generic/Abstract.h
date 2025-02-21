#ifndef MAIN_HPP
#define MAIN_HPP

#include <iostream>

class Abstract
{
public:
    Abstract(); // constructor
    
    ~Abstract(); // destructor
    
    Abstract(const Abstract &cp); //  construtor de copias
    
    Abstract& operator= (const Abstract& cp);

    virtual void Name() =0;

protected:
    int m_attr1 = 0;
    double m_attr2 = 0.0;
    std::string m_attr3 = "attr3";

public:
    void setAttr3(const std::string &newAttr) { m_attr3 = newAttr; }
    std::string getAttr3() const { return m_attr3; }    

};

#endif
