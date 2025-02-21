#include <iostream>
#include "Abstract.h"


Abstract::Abstract(){};

Abstract::~Abstract() {};

Abstract::Abstract(const Abstract &cp) 
{
    m_attr1 = cp.m_attr1;
    m_attr2 = cp.m_attr2;
    m_attr3 = cp.m_attr3;
};

Abstract::Abstract& operator= (const Abstract& cp)
{
    m_attr1 = cp.m_attr1;
    m_attr2 = cp.m_attr2;
    m_attr3 = cp.m_attr3;
    
    return *this;
};


class derived : public Abstract
{
public:
    derived() { std::cout << "This class can be instantiated" << std::endl; }
    ~derived() {}

public:
    std::string derivedAttr = "Derived atribute";
    
};


int main(){
    std::cout << "Hello" << std::endl;
    
    derived aDerived;
    std::cout << aDerived.derivedAttr << std::endl;

    aDerived.setAttr3("new attr 3");
    std::cout << "attr3: " << aDerived.getAttr3() << std::endl;

    return 0;
}