#ifndef WRITEMAPSJSONH
#define WRITEMAPSJSONH

#include "json.h"

namespace JSONTools {
  template< class T1, class T2>
  inline void AddMap(double shiftX, Json::Value &root, const std::map<T1, T2>&mymap, const std::string &key, double scaleY = +1.) {
    
    typename std::map<T1, T2>::const_iterator w;

    std::stringstream out;
    out << mymap.size() << " ";
    for (w = mymap.begin(); w != mymap.end(); w++) {
      double x = w->first + shiftX;
      double y = w->second;
      y *= scaleY;
      out << x << " " << y << " ";
    }

    root[key] = out.str();
  }

  template< class T1, class T2>
  inline void GetMap(Json::Value &root, std::map< T1, T2 >  & mymap, const std::string &key) {
    mymap.clear();

    std::stringstream data;
    if (root.isMember(key) == false) {
      myex;
      throw myex;
    }
    data << root[key];

    int size;
    data >> size;
    for (int i = 0; i < size; i++) {
      T1 A;
      T2 B;
      data >> A >> B;
      mymap[A] = B;
    }
  }

};

#endif


