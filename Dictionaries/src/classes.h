// -*- C++ -*-
//Add includes for your classes here
#include <vector>
#include <string>
#include "DataFormats/Common/interface/Wrapper.h"

namespace {
  struct dictionary {
    std::vector<std::vector<int> > vi2d;
    edm::Wrapper<std::vector<std::vector<int> > > wvi2d;
      
    std::vector<std::vector<float> > vf2d;
    edm::Wrapper<std::vector<std::vector<float> > > wvf2d;

    std::string s;
    edm::Wrapper<std::string> ws;
      
    std::vector<std::string> vs;
    edm::Wrapper<std::vector<std::string> > wvs;
          
    std::vector<std::vector<std::string> > vs2d;
    edm::Wrapper<std::vector<std::vector<std::string> > > wvs2d;


  };
}
