// -*- C++ -*-
//
// Package:    JetCorrProducer
// Class:      JetCorrProducer
// 
//   Author:  Paul Geffert
//   Created: May 24 2011
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "DataFormats/PatCandidates/interface/PFParticle.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"

//
// class declaration
//

class JetCorrProducer : public edm::EDProducer {
   public:
      explicit JetCorrProducer(const edm::ParameterSet&);
      ~JetCorrProducer();

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  typedef std::vector<double> JetCorrCollection;
  typedef std::vector<double> JetEnergyUncert;


};



JetCorrProducer::JetCorrProducer(const edm::ParameterSet& iConfig)
{

  produces<JetCorrCollection>( "ak5PFL2L3" ).setBranchAlias( "ak5PFL2L3s");
  produces<JetCorrCollection>( "ak5PFL2L3Residual" ).setBranchAlias( "ak5PFL2L3Residuals");
  produces<JetCorrCollection>( "ak5PFL1FastL2L3" ).setBranchAlias( "ak5PFL1FastL2L3s");
  produces<JetCorrCollection>( "ak5PFL1L2L3" ).setBranchAlias( "ak5PFL1L2L3s");
  produces<JetCorrCollection>( "ak5PFL1FastL2L3Residual" ).setBranchAlias( "ak5PFL1FastL2L3Residuals");
  produces<JetCorrCollection>( "ak5PFL1L2L3Residual" ).setBranchAlias( "ak5PFL1L2L3Residuals");
  /*
  produces<JetCorrCollection>( "ak5CaloL2L3" ).setBranchAlias( "ak5CaloL2L3s");
  produces<JetCorrCollection>( "ak5CaloL2L3Residual" ).setBranchAlias( "ak5CaloL2L3Residuals");
  produces<JetCorrCollection>( "ak5CaloL1FastL2L3" ).setBranchAlias( "ak5CaloL1FastL2L3s");
  produces<JetCorrCollection>( "ak5CaloL1L2L3" ).setBranchAlias( "ak5CaloL1L2L3s");
  produces<JetCorrCollection>( "ak5CaloL1FastL2L3Residual" ).setBranchAlias( "ak5CaloL1FastL2L3Residuals");
  produces<JetCorrCollection>( "ak5CaloL1L2L3Residual" ).setBranchAlias( "ak5CaloL1L2L3Residuals");
  */
  produces<JetEnergyUncert>( "ak5PFUncert" ).setBranchAlias( "ak5PFUncerts");

}


JetCorrProducer::~JetCorrProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
JetCorrProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   //   using namespace reco; 
   using namespace std;

//PF jet corrections
   auto_ptr<JetCorrCollection> ak5PFL2L3s( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5PFL2L3Residuals( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5PFL1FastL2L3s( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5PFL1L2L3s( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5PFL1FastL2L3Residuals( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5PFL1L2L3Residuals( new JetCorrCollection );

/*
//Calo jet corrections
   auto_ptr<JetCorrCollection> ak5CaloL2L3s( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5CaloL2L3Residuals( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5CaloL1FastL2L3s( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5CaloL1L2L3s( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5CaloL1FastL2L3Residuals( new JetCorrCollection );
   auto_ptr<JetCorrCollection> ak5CaloL1L2L3Residuals( new JetCorrCollection );
*/

//PF jet energy uncertainty
   auto_ptr<JetEnergyUncert> ak5PFUncerts( new JetEnergyUncert );


   bool useResiduals = true;
   if(!iEvent.isRealData()) useResiduals = false; //No residual corrections in MC
	 
   std::string dummy = "ak5PFL2L3";
   std::string name1 = "ak5PFL2L3Residual"; 
   std::string name2 = "ak5PFL1FastL2L3Residual";
   std::string name3 = "ak5PFL1L2L3Residual";
   //std::string name4 = "ak5CaloL2L3Residual";
   //std::string name5 = "ak5CaloL1FastL2L3Residual";
   //std::string name6 = "ak5CaloL1L2L3Residual";
   if(!useResiduals) {//No residual corrections in MC
     name1 = name2 = name3 = dummy;
     //name4 = name5 = name6 = dummy;
   }


   const JetCorrector& ak5PFL2L3Corrector_ = * JetCorrector::getJetCorrector ("ak5PFL2L3", iSetup);
   const JetCorrector& ak5PFL1FastL2L3Corrector_ = * JetCorrector::getJetCorrector ("ak5PFL1FastL2L3", iSetup);
   const JetCorrector& ak5PFL1L2L3Corrector_ = * JetCorrector::getJetCorrector ("ak5PFL1L2L3", iSetup);
   const JetCorrector& ak5PFL2L3ResidualCorrector_ = * JetCorrector::getJetCorrector (name1, iSetup);
   const JetCorrector& ak5PFL1FastL2L3ResidualCorrector_ = * JetCorrector::getJetCorrector (name2, iSetup);
   const JetCorrector& ak5PFL1L2L3ResidualCorrector_ = * JetCorrector::getJetCorrector (name3, iSetup);

/*
   const JetCorrector& ak5CaloL2L3Corrector_ = * JetCorrector::getJetCorrector ("ak5CaloL2L3", iSetup);
   const JetCorrector& ak5CaloL1FastL2L3Corrector_ = * JetCorrector::getJetCorrector ("ak5CaloL1FastL2L3", iSetup);
   const JetCorrector& ak5CaloL1L2L3Corrector_ = * JetCorrector::getJetCorrector ("ak5CaloL1L2L3", iSetup);
   const JetCorrector& ak5CaloL2L3ResidualCorrector_ = * JetCorrector::getJetCorrector (name4, iSetup);
   const JetCorrector& ak5CaloL1FastL2L3ResidualCorrector_ = * JetCorrector::getJetCorrector (name5, iSetup);
   const JetCorrector& ak5CaloL1L2L3ResidualCorrector_ = * JetCorrector::getJetCorrector (name6, iSetup);
*/

   //Get object used to calculate jet energy uncertainty
   edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
   iSetup.get<JetCorrectionsRecord>().get("AK5PF",JetCorParColl);
   JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
   JetCorrectionUncertainty *jecUnc = new JetCorrectionUncertainty(JetCorPar);


   //Get PF jet corrections---------------------------
    edm::Handle< std::vector<pat::Jet> > jets;
    //iEvent.getByLabel("selectedPatJetsPF",jets);
    iEvent.getByLabel("cleanPatJetsAK5PF",jets);

   std::vector<pat::Jet> uncorJets;

   for(  std::vector<pat::Jet>::const_iterator ijet = jets->begin(); ijet != jets->end(); ++ijet )
   {
      pat::Jet uncorrJet = ijet->correctedJet("Uncorrected");
      uncorJets.push_back(uncorrJet);
   }

   std::vector<pat::Jet>::const_iterator iuncorrjet = uncorJets.begin();

   for(  std::vector<pat::Jet>::const_iterator ijet = jets->begin(); ijet != jets->end(); ++ijet, ++iuncorrjet )
   {

      //int index = iuncorrjet-uncorJets.begin();
      //const edm::RefToBase<reco::Jet> uncorjetRef(edm::Ref<std::vector<pat::Jet> >(&uncorJets,index));

      ak5PFL2L3s->push_back( ak5PFL2L3Corrector_.correction( *iuncorrjet,  iEvent,iSetup ) );
      ak5PFL1FastL2L3s->push_back( ak5PFL1FastL2L3Corrector_.correction( *iuncorrjet,  iEvent,iSetup ) );
      ak5PFL1L2L3s->push_back( ak5PFL1L2L3Corrector_.correction( *iuncorrjet,  iEvent,iSetup ) );
      if(useResiduals) {
	ak5PFL2L3Residuals->push_back( ak5PFL2L3ResidualCorrector_.correction( *iuncorrjet,  iEvent,iSetup ) );
	ak5PFL1FastL2L3Residuals->push_back( ak5PFL1FastL2L3ResidualCorrector_.correction( *iuncorrjet,  iEvent,iSetup ) );
	ak5PFL1L2L3Residuals->push_back( ak5PFL1L2L3ResidualCorrector_.correction( *iuncorrjet,  iEvent,iSetup ) );
      }
      else {
	ak5PFL2L3Residuals->push_back(0);
	ak5PFL1FastL2L3Residuals->push_back(0);
	ak5PFL1L2L3Residuals->push_back(0);
      }

      //Get jet energy uncertainty
      jecUnc->setJetEta(ijet->eta());
      jecUnc->setJetPt(ijet->pt()); // here you must use the CORRECTED jet pt
      double unc = fabs(ijet->eta()) <5.2 ? jecUnc->getUncertainty(true) : 0.0;
      ak5PFUncerts->push_back( unc );
      
   }

   iEvent.put( ak5PFL2L3s, "ak5PFL2L3" );
   iEvent.put( ak5PFL2L3Residuals, "ak5PFL2L3Residual" );
   iEvent.put( ak5PFL1FastL2L3s, "ak5PFL1FastL2L3" );
   iEvent.put( ak5PFL1L2L3s, "ak5PFL1L2L3" );
   iEvent.put( ak5PFL1FastL2L3Residuals, "ak5PFL1FastL2L3Residual" );
   iEvent.put( ak5PFL1L2L3Residuals, "ak5PFL1L2L3Residual" );
   iEvent.put( ak5PFUncerts, "ak5PFUncert" );

   delete jecUnc;

/*
   //Get Calo jet corrections---------------------------
    edm::Handle< std::vector<pat::Jet> > Calojets;
    iEvent.getByLabel("cleanPatJetsAK5Calo",Calojets);

   std::vector<pat::Jet> uncorCaloJets;

   for(  std::vector<pat::Jet>::const_iterator ijet = Calojets->begin(); ijet != Calojets->end(); ++ijet )
   {
      pat::Jet uncorrJet = ijet->correctedJet("Uncorrected");
      uncorCaloJets.push_back(uncorrJet);
   }

   std::vector<pat::Jet>::const_iterator iuncorrCalojet = uncorCaloJets.begin();

   for(  std::vector<pat::Jet>::const_iterator ijet = Calojets->begin(); ijet != Calojets->end(); ++ijet, ++iuncorrCalojet )
   {

      pat::Jet uncorrJet = ijet->correctedJet("Uncorrected");

      int index = iuncorrCalojet-uncorCaloJets.begin();
      const edm::RefToBase<reco::Jet> uncorjetRef(edm::Ref<std::vector<pat::Jet> >(&uncorCaloJets,index));

      ak5CaloL2L3s->push_back( ak5CaloL2L3Corrector_.correction( *iuncorrCalojet,  iEvent,iSetup ) );
      ak5CaloL1FastL2L3s->push_back( ak5CaloL1FastL2L3Corrector_.correction( *iuncorrCalojet,  iEvent,iSetup ) );
      ak5CaloL1L2L3s->push_back( ak5CaloL1L2L3Corrector_.correction( *iuncorrCalojet,  iEvent,iSetup ) );
      if(useResiduals) {
	ak5CaloL2L3Residuals->push_back( ak5CaloL2L3ResidualCorrector_.correction( *iuncorrCalojet,  iEvent,iSetup ) );
	ak5CaloL1FastL2L3Residuals->push_back( ak5CaloL1FastL2L3ResidualCorrector_.correction( *iuncorrCalojet,  iEvent,iSetup ) );
	ak5CaloL1L2L3Residuals->push_back( ak5CaloL1L2L3ResidualCorrector_.correction( *iuncorrCalojet,  iEvent,iSetup ) );
      }
      else {
	ak5CaloL2L3Residuals->push_back(0);
	ak5CaloL1FastL2L3Residuals->push_back(0);
	ak5CaloL1L2L3Residuals->push_back(0);
      }
   }

   iEvent.put( ak5CaloL2L3s, "ak5CaloL2L3" );
   iEvent.put( ak5CaloL2L3Residuals, "ak5CaloL2L3Residual" );
   iEvent.put( ak5CaloL1FastL2L3s, "ak5CaloL1FastL2L3" );
   iEvent.put( ak5CaloL1L2L3s, "ak5CaloL1L2L3" );
   iEvent.put( ak5CaloL1FastL2L3Residuals, "ak5CaloL1FastL2L3Residual" );
   iEvent.put( ak5CaloL1L2L3Residuals, "ak5CaloL1L2L3Residual" );
*/

 
}

// ------------ method called once each job just before starting event loop  ------------
void 
JetCorrProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetCorrProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetCorrProducer);
