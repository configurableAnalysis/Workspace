// -*- C++ -*-
//
// Package:    BFieldProducer
// Class:      BFieldProducer
// 
/**\class BFieldProducer BFieldProducer.cc ProductionBField/BFieldProducer/src/BFieldProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Finn O'Neill Rebassoo,510 1-006,+41227679809,
//         Created:  Thu Oct 14 20:21:08 CEST 2010
// $Id: BFieldProducer.cc,v 1.1 2010/11/04 22:48:06 rebassoo Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Scalers/interface/DcsStatus.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "MagneticField/Engine/interface/MagneticField.h"


//
// class declaration
//

class BFieldProducer : public edm::EDProducer {
   public:
      explicit BFieldProducer(const edm::ParameterSet&);
      ~BFieldProducer();

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  double BField_;
  typedef std::vector<double> BFieldCollection;
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
BFieldProducer::BFieldProducer(const edm::ParameterSet& iConfig)
{
   //register your products
/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
*/
   //now do what ever other initialization is needed
  
  produces<BFieldCollection>( "BField" ).setBranchAlias( "BFields");


}


BFieldProducer::~BFieldProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
BFieldProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   //   using namespace reco; 
   using namespace std;

   edm::Handle<DcsStatusCollection> dcsHandle;
   //   iEvent.getByLabel(dcsTag_, dcsHandle);
   iEvent.getByLabel("scalersRawToDigi", dcsHandle);
   double evt_bField;

   ESHandle<MagneticField> magneticField;
   iSetup.get<IdealMagneticFieldRecord>().get(magneticField);
        
   evt_bField = magneticField->inTesla(GlobalPoint(0.,0.,0.)).z();

   auto_ptr<BFieldCollection> BFields( new BFieldCollection );

   const int size = 1;
   BFields->reserve( size );
   BFields->push_back( evt_bField );

   iEvent.put( BFields, "BField" );


/* This is an event example
   //Read 'ExampleData' from the Event
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   std::auto_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
   iEvent.put(pOut);
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
BFieldProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
BFieldProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(BFieldProducer);
