// -*- C++ -*-
//Add includes for your classes here
#include <vector>
//#include <string>
#include "TString.h"
#include "DataFormats/Common/interface/Wrapper.h"

namespace {
  struct dictionary {
    std::vector<std::vector<int> > vi2d;
    edm::Wrapper<std::vector<std::vector<int> > > wvi2d;
      
    std::vector<std::vector<float> > vf2d;
    edm::Wrapper<std::vector<std::vector<float> > > wvf2d;

    TString s;
    edm::Wrapper<TString> ws;
      
    std::vector<TString> vs;
    edm::Wrapper<std::vector<TString> > wvs;
          
    std::vector<std::vector<TString> > vs2d;
    edm::Wrapper<std::vector<std::vector<TString> > > wvs2d;


  };
}
