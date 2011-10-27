#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/TriggerPath.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerAlgorithm.h"
#include "RecoEgamma/EgammaTools/interface/ConversionFinder.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/Scalers/interface/DcsStatus.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "DataFormats/Common/interface/ConditionsInEdm.h"
#include "FWCore/Framework/interface/Run.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"

using namespace std;

class AdHocNTupler : public NTupler {
 public:
  AdHocNTupler (const edm::ParameterSet& iConfig){
    edm::ParameterSet adHocPSet = iConfig.getParameter<edm::ParameterSet>("AdHocNPSet");

    if (adHocPSet.exists("useTFileService"))
      useTFileService_=adHocPSet.getParameter<bool>("useTFileService");         
    else
      useTFileService_=iConfig.getParameter<bool>("useTFileService");

    if (useTFileService_){
      if (adHocPSet.exists("treeName")){
	treeName_=adHocPSet.getParameter<std::string>("treeName");
	ownTheTree_=true;
      }
      else{
	treeName_=iConfig.getParameter<std::string>("treeName");
	ownTheTree_=false;
      }
    }
    

    trigger_prescalevalue = new std::vector<float>;
    trigger_name = new std::vector<std::string>;
    trigger_decision = new std::vector<float>;
    trigger_lastfiltername = new std::vector<std::string>;
    triggerobject_pt = new std::vector<std::vector<float> >;
    triggerobject_px = new std::vector<std::vector<float> >;
    triggerobject_py = new std::vector<std::vector<float> >;
    triggerobject_pz = new std::vector<std::vector<float> >;
    triggerobject_et = new std::vector<std::vector<float> >;
    triggerobject_energy = new std::vector<std::vector<float> >;
    triggerobject_phi = new std::vector<std::vector<float> >;
    triggerobject_eta = new std::vector<std::vector<float> >;
    triggerobject_collectionname = new std::vector<std::vector<TString> >;
    standalone_triggerobject_pt = new std::vector<float>;
    standalone_triggerobject_px = new std::vector<float>;
    standalone_triggerobject_py = new std::vector<float>;
    standalone_triggerobject_pz = new std::vector<float>;
    standalone_triggerobject_et = new std::vector<float>;
    standalone_triggerobject_energy = new std::vector<float>;
    standalone_triggerobject_phi = new std::vector<float>;
    standalone_triggerobject_eta = new std::vector<float>;
    standalone_triggerobject_collectionname = new std::vector<std::string>;
    L1trigger_bit = new std::vector<float>;
    L1trigger_techTrigger = new std::vector<float>;
    L1trigger_prescalevalue = new std::vector<float>;
    L1trigger_name = new std::vector<std::string>;
    L1trigger_alias = new std::vector<std::string>;
    L1trigger_decision = new std::vector<float>;
    L1trigger_decision_nomask = new std::vector<float>;
    els_conversion_dist = new std::vector<float>;
    els_conversion_dcot = new std::vector<float>;
    hbhefilter_decision_ = new int;
    cschalofilter_decision_ = new int;
    ecalTPfilter_decision_ = new int;
    scrapingVeto_decision_ = new int;
    totalkinematicsfilter_decision_ = new int;
    trackingfailurefilter_decision_ = new int;
    MPT_ = new float;
    jets_AK5PFclean_corrL2L3_ = new std::vector<float>; 
    jets_AK5PFclean_corrL2L3Residual_ = new std::vector<float>;
    jets_AK5PFclean_corrL1FastL2L3_ = new std::vector<float>;
    jets_AK5PFclean_corrL1L2L3_ = new std::vector<float>;
    jets_AK5PFclean_corrL1FastL2L3Residual_ = new std::vector<float>;
    jets_AK5PFclean_corrL1L2L3Residual_ = new std::vector<float>;
    jets_AK5clean_corrL2L3_ = new std::vector<float>;
    jets_AK5clean_corrL2L3Residual_ = new std::vector<float>;
    jets_AK5clean_corrL1FastL2L3_ = new std::vector<float>;
    jets_AK5clean_corrL1L2L3_ = new std::vector<float>;
    jets_AK5clean_corrL1FastL2L3Residual_ = new std::vector<float>;
    jets_AK5clean_corrL1L2L3Residual_ = new std::vector<float>;
    PU_zpositions_ = new std::vector<std::vector<float> >;
    PU_sumpT_lowpT_ = new std::vector<std::vector<float> >;
    PU_sumpT_highpT_ = new std::vector<std::vector<float> >;
    PU_ntrks_lowpT_ = new std::vector<std::vector<int> >;
    PU_ntrks_highpT_ = new std::vector<std::vector<int> >;
    PU_NumInteractions_ = new std::vector<int>;
    PU_bunchCrossing_ = new std::vector<int>;
  }

  ~AdHocNTupler(){
    delete trigger_prescalevalue;
    delete trigger_name;
    delete trigger_decision;
    delete trigger_lastfiltername;
    delete triggerobject_pt;
    delete triggerobject_px;
    delete triggerobject_py;
    delete triggerobject_pz;
    delete triggerobject_et;
    delete triggerobject_energy;
    delete triggerobject_phi;
    delete triggerobject_eta;
    delete triggerobject_collectionname;
    delete standalone_triggerobject_pt;
    delete standalone_triggerobject_px;
    delete standalone_triggerobject_py;
    delete standalone_triggerobject_pz;
    delete standalone_triggerobject_et;
    delete standalone_triggerobject_energy;
    delete standalone_triggerobject_phi;
    delete standalone_triggerobject_eta;
    delete standalone_triggerobject_collectionname;
    delete L1trigger_bit;
    delete L1trigger_techTrigger;
    delete L1trigger_prescalevalue;
    delete L1trigger_name;
    delete L1trigger_alias;
    delete L1trigger_decision;
    delete L1trigger_decision_nomask;
    delete els_conversion_dist;
    delete els_conversion_dcot;
    delete hbhefilter_decision_;
    delete cschalofilter_decision_;
    delete ecalTPfilter_decision_;
		delete scrapingVeto_decision_;
		delete totalkinematicsfilter_decision_;
    delete trackingfailurefilter_decision_;
    delete MPT_;
    delete jets_AK5PFclean_corrL2L3_;
    delete jets_AK5PFclean_corrL2L3Residual_;
    delete jets_AK5PFclean_corrL1FastL2L3_;
    delete jets_AK5PFclean_corrL1L2L3_;
    delete jets_AK5PFclean_corrL1FastL2L3Residual_;
    delete jets_AK5PFclean_corrL1L2L3Residual_;
    delete jets_AK5clean_corrL2L3_;
    delete jets_AK5clean_corrL2L3Residual_;
    delete jets_AK5clean_corrL1FastL2L3_;
    delete jets_AK5clean_corrL1L2L3_;
    delete jets_AK5clean_corrL1FastL2L3Residual_;
    delete jets_AK5clean_corrL1L2L3Residual_;
    delete PU_zpositions_;
    delete PU_sumpT_lowpT_;
    delete PU_sumpT_highpT_;
    delete PU_ntrks_lowpT_;
    delete PU_ntrks_highpT_;
    delete PU_NumInteractions_;
    delete PU_bunchCrossing_;
  }

  uint registerleaves(edm::ProducerBase * producer){
    uint nLeaves=0;
    if (useTFileService_){
      edm::Service<TFileService> fs;      
      if (ownTheTree_){
	ownTheTree_=true;
	tree_=fs->make<TTree>(treeName_.c_str(),"StringBasedNTupler tree");
      }else{
	TObject * object = fs->file().Get(treeName_.c_str());
	if (!object){
	  ownTheTree_=true;
	  tree_=fs->make<TTree>(treeName_.c_str(),"StringBasedNTupler tree");
	}
	tree_=dynamic_cast<TTree*>(object);
	if (!tree_){
	  ownTheTree_=true;
	  tree_=fs->make<TTree>(treeName_.c_str(),"StringBasedNTupler tree");
	}
      }
      
      //register the leaves by hand
      tree_->Branch("trigger_prescalevalue",&trigger_prescalevalue);
      tree_->Branch("trigger_name",&trigger_name);
      tree_->Branch("trigger_decision",&trigger_decision);
      tree_->Branch("trigger_lastfiltername",&trigger_lastfiltername);
      tree_->Branch("triggerobject_pt",&triggerobject_pt);
      tree_->Branch("triggerobject_px",&triggerobject_px);
      tree_->Branch("triggerobject_py",&triggerobject_py);
      tree_->Branch("triggerobject_pz",&triggerobject_pz);
      tree_->Branch("triggerobject_et",&triggerobject_et);
      tree_->Branch("triggerobject_energy",&triggerobject_energy);
      tree_->Branch("triggerobject_phi",&triggerobject_phi);
      tree_->Branch("triggerobject_eta",&triggerobject_eta);
      tree_->Branch("triggerobject_collectionname",&triggerobject_collectionname);
      tree_->Branch("standalone_triggerobject_pt",&standalone_triggerobject_pt);
      tree_->Branch("standalone_triggerobject_px",&standalone_triggerobject_px);
      tree_->Branch("standalone_triggerobject_py",&standalone_triggerobject_py);
      tree_->Branch("standalone_triggerobject_pz",&standalone_triggerobject_pz);
      tree_->Branch("standalone_triggerobject_et",&standalone_triggerobject_et);
      tree_->Branch("standalone_triggerobject_energy",&standalone_triggerobject_energy);
      tree_->Branch("standalone_triggerobject_phi",&standalone_triggerobject_phi);
      tree_->Branch("standalone_triggerobject_eta",&standalone_triggerobject_eta);
      tree_->Branch("standalone_triggerobject_collectionname",&standalone_triggerobject_collectionname);
      tree_->Branch("L1trigger_bit",&L1trigger_bit);
      tree_->Branch("L1trigger_techTrigger",&L1trigger_techTrigger);
      tree_->Branch("L1trigger_prescalevalue",&L1trigger_prescalevalue);
      tree_->Branch("L1trigger_name",&L1trigger_name);
      tree_->Branch("L1trigger_alias",&L1trigger_alias);
      tree_->Branch("L1trigger_decision",&L1trigger_decision);
      tree_->Branch("L1trigger_decision_nomask",&L1trigger_decision_nomask);
      tree_->Branch("els_conversion_dist",&els_conversion_dist);
      tree_->Branch("els_conversion_dcot",&els_conversion_dcot);
      tree_->Branch("hbhefilter_decision",hbhefilter_decision_,"hbhefilter_decision/I");
      tree_->Branch("trackingfailurefilter_decision",trackingfailurefilter_decision_,"trackingfailurefilter_decision/I");
			tree_->Branch("cschalofilter_decision",cschalofilter_decision_,"cschalofilter_decision/I");
			tree_->Branch("ecalTPfilter_decision",ecalTPfilter_decision_,"ecalTPfilter_decision/I");
			tree_->Branch("scrapingVeto_decision",scrapingVeto_decision_,"scrapingVeto_decision/I");
			tree_->Branch("totalkinematicsfilter_decision",totalkinematicsfilter_decision_,"totalkinematicsfilter_decision/I");
      tree_->Branch("MPT",MPT_,"MPT/F");
      tree_->Branch("jets_AK5PFclean_corrL2L3",&jets_AK5PFclean_corrL2L3_);
      tree_->Branch("jets_AK5PFclean_corrL2L3Residual",&jets_AK5PFclean_corrL2L3Residual_);
      tree_->Branch("jets_AK5PFclean_corrL1FastL2L3",&jets_AK5PFclean_corrL1FastL2L3_);
      tree_->Branch("jets_AK5PFclean_corrL1L2L3",&jets_AK5PFclean_corrL1L2L3_);
      tree_->Branch("jets_AK5PFclean_corrL1FastL2L3Residual",&jets_AK5PFclean_corrL1FastL2L3Residual_);
      tree_->Branch("jets_AK5PFclean_corrL1L2L3Residual",&jets_AK5PFclean_corrL1L2L3Residual_);
      tree_->Branch("jets_AK5_corrL2L3",&jets_AK5clean_corrL2L3_);
      tree_->Branch("jets_AK5_corrL2L3Residual",&jets_AK5clean_corrL2L3Residual_);
      tree_->Branch("jets_AK5_corrL1FastL2L3",&jets_AK5clean_corrL1FastL2L3_);
      tree_->Branch("jets_AK5_corrL1L2L3",&jets_AK5clean_corrL1L2L3_);
      tree_->Branch("jets_AK5_corrL1FastL2L3Residual",&jets_AK5clean_corrL1FastL2L3Residual_);
      tree_->Branch("jets_AK5_corrL1L2L3Residual",&jets_AK5clean_corrL1L2L3Residual_);
      tree_->Branch("PU_zpositions",&PU_zpositions_);
      tree_->Branch("PU_sumpT_lowpT",&PU_sumpT_lowpT_);
      tree_->Branch("PU_sumpT_highpT",&PU_sumpT_highpT_);
      tree_->Branch("PU_ntrks_lowpT",&PU_ntrks_lowpT_);
      tree_->Branch("PU_ntrks_highpT",&PU_ntrks_highpT_);
      tree_->Branch("PU_NumInteractions",&PU_NumInteractions_);
      tree_->Branch("PU_bunchCrossing",&PU_bunchCrossing_);
    }

    else{
      //EDM COMPLIANT PART
      //      producer->produce<ACertainCollection>(ACertainInstanceName);
    }


    return nLeaves;
  }

  void fill(edm::Event& iEvent){
    //open the collection that you want
    //retrieve the objects
    //fill the variable for tree filling 


    edm::Handle< pat::TriggerEvent > triggerevent;
    iEvent.getByLabel("patTriggerEvent",triggerevent);  
    //    std::cout<<"The trigger HLT table is"<<triggerevent->nameHltTable()<<std::endl;


		edm::Handle<edm::TriggerResults> hltresults;
		edm::InputTag myPatTrig("TriggerResults","","PAT");
		iEvent.getByLabel(myPatTrig,hltresults);
	//	iEvent.getByLabel("TriggerResults","","PAT",hltresults);
		int ntrigs=hltresults->size();

		// get hold of trigger names - based on TriggerResults object!
		const edm::TriggerNames & triggerNames_ = iEvent.triggerNames(*hltresults);
		int cschalofilterResult =1, trackingfailturefilterResult=1, ecaltpfilterResult=1, scrapingVetoResult=1, totalkinematicsfilterResult=1;
		for (int itrig=0; itrig< ntrigs; itrig++) {
 			TString trigName = triggerNames_.triggerName(itrig);
  		int hltflag = (*hltresults)[itrig].accept();
	 		if (trigName=="csctighthalofilter") cschalofilterResult = hltflag;
	 		if (trigName=="trackingfailturefilter") trackingfailturefilterResult = hltflag;
	 		if (trigName=="ecaltpfilter") ecaltpfilterResult = hltflag;
	 		if (trigName=="scrapingveto") scrapingVetoResult = hltflag;
	 		if (trigName=="totalkinematicsfilter") totalkinematicsfilterResult = hltflag;
	 	}
		
    *cschalofilter_decision_ = cschalofilterResult;
    *trackingfailurefilter_decision_ = trackingfailturefilterResult;
    *ecalTPfilter_decision_ = ecaltpfilterResult;
    *scrapingVeto_decision_ = scrapingVetoResult;
    *totalkinematicsfilter_decision_ = totalkinematicsfilterResult;
		
    edm::Handle< std::vector<pat::TriggerPath> > triggerpaths;
    iEvent.getByLabel("patTrigger",triggerpaths);  
    for( std::vector<pat::TriggerPath>::const_iterator tp=triggerpaths->begin(); tp!=triggerpaths->end(); ++tp ){
      double prescalevalue = tp->prescale(); 
      std::string name = tp->name();
      float decision = tp->wasAccept();
      (*trigger_prescalevalue).push_back(prescalevalue);
      (*trigger_name).push_back(name);
      (*trigger_decision).push_back(decision);

      std::vector<TString> collection_names;
      std::vector<float> pt_vector;
      std::vector<float> px_vector;
      std::vector<float> py_vector;
      std::vector<float> pz_vector;
      std::vector<float> et_vector;
      std::vector<float> energy_vector;
      std::vector<float> phi_vector;
      std::vector<float> eta_vector;

      /*
      cout<<""<<endl;
      cout<<"Trigger names is: "<<name<<endl;
      cout<<"Trigger decision is: "<<decision<<endl;
      */

      edm::RefVector< pat::TriggerFilterCollection> toFilt = triggerevent->pathFilters(name);
      edm::RefVector<pat::TriggerFilterCollection>::const_iterator toFilt_it=toFilt.end();
       if(toFilt.size()>0){
	const pat::TriggerFilter *triggerfilter = (*(--toFilt_it)).get();
	(*trigger_lastfiltername).push_back(triggerfilter->label());
	//cout<<"The trigger filter is: "<<triggerfilter->label()<<endl;
	edm::RefVector< pat::TriggerObjectCollection > tocoll = triggerevent->filterObjects(triggerfilter->label());
      
	for( edm::RefVector<pat::TriggerObjectCollection>::const_iterator to=tocoll.begin(); to!=tocoll.end(); ++to ){
	  const pat::TriggerObject *triggerObject = (*to).get();
	  double pt = triggerObject->pt(); 
	  double px = triggerObject->px(); 
	  double py = triggerObject->py(); 
	  double pz = triggerObject->pz(); 
          double et = triggerObject->et();
	  double energy = triggerObject->energy(); 
          double phi = triggerObject->phi();
          double eta = triggerObject->eta();
	  TString collname(triggerObject->collection());
	  //cout<<"The trigger collname is: "<<collname<<endl;
	  //cout<<"The trigger objectpt is: "<<pt<<endl;
	  collection_names.push_back(collname);
	  pt_vector.push_back(pt);
	  px_vector.push_back(px);
	  py_vector.push_back(py);
	  pz_vector.push_back(pz);
          et_vector.push_back(et);
	  energy_vector.push_back(energy);
          phi_vector.push_back(phi);
          eta_vector.push_back(eta);
	}
	
	(*triggerobject_collectionname).push_back(collection_names);
	(*triggerobject_pt).push_back(pt_vector);
	(*triggerobject_px).push_back(px_vector);
	(*triggerobject_py).push_back(py_vector);
	(*triggerobject_pz).push_back(pz_vector);
        (*triggerobject_et).push_back(et_vector);
	(*triggerobject_energy).push_back(energy_vector);
        (*triggerobject_phi).push_back(phi_vector);
        (*triggerobject_eta).push_back(eta_vector);
       }//end of if statement requiring that reVector be greater than 0
       else{
	 (*trigger_lastfiltername).push_back("none");
	 (*triggerobject_collectionname).push_back(collection_names);
	 (*triggerobject_pt).push_back(pt_vector);
	 (*triggerobject_px).push_back(px_vector);
	 (*triggerobject_py).push_back(py_vector);
	 (*triggerobject_pz).push_back(pz_vector);
         (*triggerobject_et).push_back(et_vector);
	 (*triggerobject_energy).push_back(energy_vector);
         (*triggerobject_phi).push_back(phi_vector);
         (*triggerobject_eta).push_back(eta_vector);
       }
      collection_names.clear();
      pt_vector.clear();
      px_vector.clear();
      py_vector.clear();
      pz_vector.clear();
      et_vector.clear();
      energy_vector.clear();
      phi_vector.clear();
      eta_vector.clear();
    }
    

    //Get all trigger objects
    edm::Handle< std::vector<pat::TriggerObject> > triggerobjects;
    iEvent.getByLabel("patTrigger",triggerobjects);
    for( std::vector<pat::TriggerObject>::const_iterator to=triggerobjects->begin(); to!=triggerobjects->end(); ++to ){
      double pt = to->pt();
      double px = to->px();
      double py = to->py();
      double pz = to->pz();
      double et = to->et();
      double energy = to->energy();
      double phi = to->phi();
      double eta = to->eta();
      std::string collname = to->collection();
      //cout<<"The trigger collname is: "<<collname<<endl;
      //cout<<"The trigger objectpt is: "<<pt<<endl;
      (*standalone_triggerobject_collectionname).push_back(collname);
      (*standalone_triggerobject_pt).push_back(pt);
      (*standalone_triggerobject_px).push_back(px);
      (*standalone_triggerobject_py).push_back(py);
      (*standalone_triggerobject_pz).push_back(pz);
      (*standalone_triggerobject_et).push_back(et);
      (*standalone_triggerobject_energy).push_back(energy);
      (*standalone_triggerobject_phi).push_back(phi);
      (*standalone_triggerobject_eta).push_back(eta);
    }


    edm::Handle< std::vector<pat::TriggerAlgorithm> > triggeralgos;
    iEvent.getByLabel("patTrigger",triggeralgos);
    for( std::vector<pat::TriggerAlgorithm>::const_iterator ta=triggeralgos->begin(); ta!=triggeralgos->end(); ++ta ){
      float prescalevalue = ta->prescale();
      std::string name = ta->name();
      std::string alias = ta->alias();
      float bit = ta->bit();
      float techTrig = ta->techTrigger();
      float decision = ta->decision();
      float decision_nomask = ta->decisionBeforeMask();
      (*L1trigger_prescalevalue).push_back(prescalevalue);
      (*L1trigger_name).push_back(name);
      (*L1trigger_alias).push_back(alias);
      (*L1trigger_bit).push_back(bit);
      (*L1trigger_techTrigger).push_back(techTrig);
      (*L1trigger_decision).push_back(decision);
      (*L1trigger_decision_nomask).push_back(decision_nomask);
    }
    edm::Handle<bool> filter_h;
    if(iEvent.getByLabel("HBHENoiseFilterResultProducer","HBHENoiseFilterResult",filter_h)) { 
      
      iEvent.getByLabel("HBHENoiseFilterResultProducer","HBHENoiseFilterResult", filter_h);
      //      cout<<"The filter decision is :"<<*filter_h<<endl;
      if(*filter_h){*hbhefilter_decision_ = 1;}
      if(!(*filter_h)){*hbhefilter_decision_ = 0;}
    }
    else{
      *hbhefilter_decision_ = -1;
      //      cout<<"The hbheflag is not present, is this FastSim?"<<endl;
    }
   
    *MPT_ = -1; 

    edm::Handle< std::vector<pat::Electron> > electrons;
    iEvent.getByLabel("cleanPatElectrons",electrons);

    edm::Handle<reco::TrackCollection> tracks_h;
    iEvent.getByLabel("generalTracks", tracks_h);

    edm::Handle<DcsStatusCollection> dcsHandle;
    iEvent.getByLabel("scalersRawToDigi", dcsHandle);
    //iEvent.getByLabel(dcsTag_, dcsHandle);

    const edm::Run& iRun = iEvent.getRun();
    // get ConditionsInRunBlock
    edm::Handle<edm::ConditionsInRunBlock> condInRunBlock;
    iRun.getByLabel("conditionsInEdm", condInRunBlock);


    //       edm::Handle<BFieldCollection> bfield_;
    edm::Handle< std::vector<double> > bfield_;
    iEvent.getByLabel("BFieldColl","BField", bfield_);
    //iEvent.getByLabel(dcsTag_, dcsHandle);

    
    double evt_bField;
    // need the magnetic field
    //
    // if isData then derive bfield using the
    // magnet current from DcsStatus
    // otherwise take it from the IdealMagneticFieldRecord
    if (iEvent.isRealData()) {
         // scale factor = 3.801/18166.0 which are
         // average values taken over a stable two
         // week period
         float currentToBFieldScaleFactor = 2.09237036221512717e-04;
         float current;
         if(dcsHandle->size()>0) current = (*dcsHandle)[0].magnetCurrent();
	 else current = condInRunBlock->BAvgCurrent;
         evt_bField = current*currentToBFieldScaleFactor;
         //cout<<"\n"<<evt_bField;
        }
    else {
        
        //edm::ESHandle<MagneticField> magneticField;
        //iSetup.get<IdealMagneticFieldRecord>().get(magneticField);        
        //evt_bField = magneticField->inTesla(GlobalPoint(0.,0.,0.)).z();
       
       //****Temporary solution*******
       //Must fix before running on MC
      //       evt_bField = 3.8;
      evt_bField = (*bfield_)[0];

    }


    for(std::vector<pat::Electron>::const_iterator elec=electrons->begin(); elec!=electrons->end(); ++elec) {

        //Get Gsf electron
        reco::GsfElectron* el = (reco::GsfElectron*) elec->originalObject(); 
	if(el == NULL) {	
	throw cms::Exception("GsfElectron")<<"No GsfElectron matched to pat::Electron.\n";
        }

        //cout << "Found and electron" << endl;
	//if(!el->closestCtfTrackRef().isNonnull())
	//cout<< "Could not find an electron ctf track" << endl;	         

        ConversionFinder convFinder;
        ConversionInfo convInfo = convFinder.getConversionInfo(*el, tracks_h, evt_bField);
   
        (*els_conversion_dist).push_back(convInfo.dist());
        (*els_conversion_dcot).push_back(convInfo.dcot());
        //double convradius = convInfo.radiusOfConversion();
        //math::XYZPoint convPoint = convInfo.pointOfConversion();
    }



    edm::Handle< std::vector<double> > ak5PFL2L3_;
    iEvent.getByLabel("JetCorrColl","ak5PFL2L3", ak5PFL2L3_);
    edm::Handle< std::vector<double> > ak5PFL2L3Residual_;
    iEvent.getByLabel("JetCorrColl","ak5PFL2L3Residual", ak5PFL2L3Residual_);
    edm::Handle< std::vector<double> > ak5PFL1FastL2L3_;
    iEvent.getByLabel("JetCorrColl","ak5PFL1FastL2L3", ak5PFL1FastL2L3_);
    edm::Handle< std::vector<double> > ak5PFL1L2L3_;
    iEvent.getByLabel("JetCorrColl","ak5PFL1L2L3", ak5PFL1L2L3_);
    edm::Handle< std::vector<double> > ak5PFL1FastL2L3Residual_;
    iEvent.getByLabel("JetCorrColl","ak5PFL1FastL2L3Residual", ak5PFL1FastL2L3Residual_);
    edm::Handle< std::vector<double> > ak5PFL1L2L3Residual_;
    iEvent.getByLabel("JetCorrColl","ak5PFL1L2L3Residual", ak5PFL1L2L3Residual_);
    edm::Handle< std::vector<double> > ak5CaloL2L3_;
    iEvent.getByLabel("JetCorrColl","ak5CaloL2L3", ak5CaloL2L3_);
    edm::Handle< std::vector<double> > ak5CaloL2L3Residual_;
    iEvent.getByLabel("JetCorrColl","ak5CaloL2L3Residual", ak5CaloL2L3Residual_);
    edm::Handle< std::vector<double> > ak5CaloL1FastL2L3_;
    iEvent.getByLabel("JetCorrColl","ak5CaloL1FastL2L3", ak5CaloL1FastL2L3_);
    edm::Handle< std::vector<double> > ak5CaloL1L2L3_;
    iEvent.getByLabel("JetCorrColl","ak5CaloL1L2L3", ak5CaloL1L2L3_);
    edm::Handle< std::vector<double> > ak5CaloL1FastL2L3Residual_;
    iEvent.getByLabel("JetCorrColl","ak5CaloL1FastL2L3Residual", ak5CaloL1FastL2L3Residual_);
    edm::Handle< std::vector<double> > ak5CaloL1L2L3Residual_;
    iEvent.getByLabel("JetCorrColl","ak5CaloL1L2L3Residual", ak5CaloL1L2L3Residual_);

    for(uint it=0; it<(*ak5PFL2L3_).size(); it++){
      (*jets_AK5PFclean_corrL2L3_).push_back((*ak5PFL2L3_)[it]);
      (*jets_AK5PFclean_corrL2L3Residual_).push_back((*ak5PFL2L3Residual_)[it]);
      (*jets_AK5PFclean_corrL1FastL2L3_).push_back((*ak5PFL1FastL2L3_)[it]);
      (*jets_AK5PFclean_corrL1L2L3_).push_back((*ak5PFL1L2L3_)[it]);
      (*jets_AK5PFclean_corrL1FastL2L3Residual_).push_back((*ak5PFL1FastL2L3Residual_)[it]);
      (*jets_AK5PFclean_corrL1L2L3Residual_).push_back((*ak5PFL1L2L3Residual_)[it]);
    }

    for(uint it=0; it<(*ak5CaloL2L3_).size(); it++){
      (*jets_AK5clean_corrL2L3_).push_back((*ak5CaloL2L3_)[it]);
      (*jets_AK5clean_corrL2L3Residual_).push_back((*ak5CaloL2L3Residual_)[it]);
      (*jets_AK5clean_corrL1FastL2L3_).push_back((*ak5CaloL1FastL2L3_)[it]);
      (*jets_AK5clean_corrL1L2L3_).push_back((*ak5CaloL1L2L3_)[it]);
      (*jets_AK5clean_corrL1FastL2L3Residual_).push_back((*ak5CaloL1FastL2L3Residual_)[it]);
      (*jets_AK5clean_corrL1L2L3Residual_).push_back((*ak5CaloL1L2L3Residual_)[it]);
    }

  if(!iEvent.isRealData()) { //Access PU info in MC
    edm::Handle<std::vector< PileupSummaryInfo > >  PupInfo;
    iEvent.getByLabel("addPileupInfo", PupInfo);
    std::vector<PileupSummaryInfo>::const_iterator PVI;

    for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI) {
  //    std::cout << " Pileup Information: bunchXing, nvtx: " << PVI->getBunchCrossing() << " " << PVI->getPU_NumInteractions() <<"   "<< iEvent.id().event() << std::endl;
      (*PU_NumInteractions_).push_back(PVI->getPU_NumInteractions());
      (*PU_bunchCrossing_).push_back(PVI->getBunchCrossing());
      (*PU_zpositions_).push_back(PVI->getPU_zpositions());
      (*PU_sumpT_lowpT_).push_back(PVI->getPU_sumpT_lowpT());
      (*PU_sumpT_highpT_).push_back(PVI->getPU_sumpT_highpT());
      (*PU_ntrks_lowpT_).push_back(PVI->getPU_ntrks_lowpT());
      (*PU_ntrks_highpT_).push_back(PVI->getPU_ntrks_highpT());
    }
  }

    //fill the tree    
    if (ownTheTree_){ tree_->Fill(); }
    (*trigger_prescalevalue).clear();
    (*trigger_name).clear();
    (*trigger_decision).clear();
    (*trigger_lastfiltername).clear();
    (*triggerobject_pt).clear();
    (*triggerobject_px).clear();
    (*triggerobject_py).clear();
    (*triggerobject_pz).clear();
    (*triggerobject_et).clear();
    (*triggerobject_energy).clear();
    (*triggerobject_phi).clear();
    (*triggerobject_eta).clear();
    (*triggerobject_collectionname).clear();
    (*standalone_triggerobject_pt).clear();
    (*standalone_triggerobject_px).clear();
    (*standalone_triggerobject_py).clear();
    (*standalone_triggerobject_pz).clear();
    (*standalone_triggerobject_et).clear();
    (*standalone_triggerobject_energy).clear();
    (*standalone_triggerobject_phi).clear();
    (*standalone_triggerobject_eta).clear();
    (*standalone_triggerobject_collectionname).clear();
    (*L1trigger_bit).clear();
    (*L1trigger_techTrigger).clear();
    (*L1trigger_prescalevalue).clear();
    (*L1trigger_name).clear();
    (*L1trigger_alias).clear();
    (*L1trigger_decision).clear();
    (*L1trigger_decision_nomask).clear();
    (*els_conversion_dist).clear();
    (*els_conversion_dcot).clear();
    (*jets_AK5PFclean_corrL2L3_).clear();
    (*jets_AK5PFclean_corrL2L3Residual_).clear();
    (*jets_AK5PFclean_corrL1FastL2L3_).clear();
    (*jets_AK5PFclean_corrL1L2L3_).clear();
    (*jets_AK5PFclean_corrL1FastL2L3Residual_).clear();
    (*jets_AK5PFclean_corrL1L2L3Residual_).clear();
    (*jets_AK5clean_corrL2L3_).clear();
    (*jets_AK5clean_corrL2L3Residual_).clear();
    (*jets_AK5clean_corrL1FastL2L3_).clear();
    (*jets_AK5clean_corrL1L2L3_).clear();
    (*jets_AK5clean_corrL1FastL2L3Residual_).clear();
    (*jets_AK5clean_corrL1L2L3Residual_).clear();
    (*PU_zpositions_).clear();
    (*PU_sumpT_lowpT_).clear();
    (*PU_sumpT_highpT_).clear();
    (*PU_ntrks_lowpT_).clear();
    (*PU_ntrks_highpT_).clear();
    (*PU_NumInteractions_).clear();
    (*PU_bunchCrossing_).clear(); 
  }

  void callBack(){
    //clean up whatever memory was allocated
  }

 private:
  bool ownTheTree_;
  std::string treeName_;
  bool useTFileService_;

  std::vector<float> * trigger_prescalevalue;
  std::vector<std::string> * trigger_name;
  std::vector<float> * trigger_decision;
  std::vector<std::string> * trigger_lastfiltername;
  std::vector<std::vector<float> > * triggerobject_pt;
  std::vector<std::vector<float> > * triggerobject_px;
  std::vector<std::vector<float> > * triggerobject_py;
  std::vector<std::vector<float> > * triggerobject_pz;
  std::vector<std::vector<float> > * triggerobject_et;
  std::vector<std::vector<float> > * triggerobject_energy;
  std::vector<std::vector<float> > * triggerobject_phi;
  std::vector<std::vector<float> > * triggerobject_eta;
  std::vector<std::vector<TString> > * triggerobject_collectionname;
  std::vector<float> * standalone_triggerobject_pt;
  std::vector<float> * standalone_triggerobject_px;
  std::vector<float> * standalone_triggerobject_py;
  std::vector<float> * standalone_triggerobject_pz;
  std::vector<float> * standalone_triggerobject_et;
  std::vector<float> * standalone_triggerobject_energy;
  std::vector<float> * standalone_triggerobject_phi;
  std::vector<float> * standalone_triggerobject_eta;
  std::vector<std::string> * standalone_triggerobject_collectionname;
  std::vector<float> * L1trigger_bit;
  std::vector<float> * L1trigger_techTrigger;
  std::vector<float> * L1trigger_prescalevalue;
  std::vector<std::string> * L1trigger_name;
  std::vector<std::string> * L1trigger_alias;
  std::vector<float> * L1trigger_decision;
  std::vector<float> * L1trigger_decision_nomask;
  std::vector<float> * els_conversion_dist;
  std::vector<float> * els_conversion_dcot;
  int * hbhefilter_decision_;
  int * cschalofilter_decision_;
  int * ecalTPfilter_decision_;
  int * scrapingVeto_decision_;
  int * totalkinematicsfilter_decision_;
  int * trackingfailurefilter_decision_;
  float * MPT_;
  std::vector<float> * jets_AK5PFclean_corrL2L3_;
  std::vector<float> * jets_AK5PFclean_corrL2L3Residual_;
  std::vector<float> * jets_AK5PFclean_corrL1FastL2L3_;
  std::vector<float> * jets_AK5PFclean_corrL1L2L3_;
  std::vector<float> * jets_AK5PFclean_corrL1FastL2L3Residual_;
  std::vector<float> * jets_AK5PFclean_corrL1L2L3Residual_;
  std::vector<float> * jets_AK5clean_corrL2L3_;
  std::vector<float> * jets_AK5clean_corrL2L3Residual_;
  std::vector<float> * jets_AK5clean_corrL1FastL2L3_;
  std::vector<float> * jets_AK5clean_corrL1L2L3_;
  std::vector<float> * jets_AK5clean_corrL1FastL2L3Residual_;
  std::vector<float> * jets_AK5clean_corrL1L2L3Residual_;
  std::vector<std::vector<float> > * PU_zpositions_;
  std::vector<std::vector<float> > * PU_sumpT_lowpT_;
  std::vector<std::vector<float> > * PU_sumpT_highpT_;
  std::vector<std::vector<int> > * PU_ntrks_lowpT_;
  std::vector<std::vector<int> > * PU_ntrks_highpT_;
  std::vector<int> * PU_NumInteractions_;
  std::vector<int> * PU_bunchCrossing_;
};
