#include "RA2bSkim.h"
#include "TMath.h"
#include "TFile.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TROOT.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH3F.h"
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include "TString.h"
#include "TVector3.h"
#include "TLorentzVector.h"
using namespace std;

void tree1r(TChain *chainA,TChain *chainB,TString output_filename)
{

  InitializeA(chainA);
  InitializeB(chainB);
  
  // Make the new file
  TFile *newFile = new TFile(output_filename.Data(),"RECREATE");
  TDirectoryFile *dir = new TDirectoryFile("configurableAnalysis","configurableAnalysis");
  dir->cd();
  TTree *newtreeA = chainA->CloneTree(0);
  TTree *newtreeB = chainB->CloneTree(0);

  Int_t nentries = (Int_t)chainB->GetEntries();
  Int_t noutput = 0;

  for (int iEnt = 0; iEnt<nentries; iEnt++) {

    chainA->GetEntry(iEnt);
    chainB->GetEntry(iEnt);

    bool goodevent = false; // For filtering

    int numPFmu = pf_mus_pt->size();
    int numPFel = pf_els_pt->size();
    float PFMET = pfTypeImets_et->at(0);
    float P_leadJet(-9.);

    int numGoodPFJets = 0;
    bool GoodPFJet[10000];
    for (unsigned int k=0; k<jets_AK5PF_pt->size(); k++) {
      GoodPFJet[k]=true;

      if(jets_AK5PF_pt->at(k)<=50.) GoodPFJet[k]=false;
      if(fabs(jets_AK5PF_eta->at(k))>=2.4) GoodPFJet[k]=false;

      double NEF = jets_AK5PF_neutralEmE->at(k)/(jets_AK5PF_energy->at(k)*jets_AK5PF_corrFactorRaw->at(k));
      double CEF = jets_AK5PF_chgEmE->at(k)/(jets_AK5PF_energy->at(k)*jets_AK5PF_corrFactorRaw->at(k));
      double NHF = jets_AK5PF_neutralHadE->at(k)/(jets_AK5PF_energy->at(k)*jets_AK5PF_corrFactorRaw->at(k));
      double CHF = jets_AK5PF_chgHadE->at(k)/(jets_AK5PF_energy->at(k)*jets_AK5PF_corrFactorRaw->at(k));
      int chgMult = jets_AK5PF_chg_Mult->at(k);
      int numConst = jets_AK5PF_mu_Mult->at(k)+jets_AK5PF_neutral_Mult->at(k)+jets_AK5PF_chg_Mult->at(k);

      if(NEF >= 0.99) { GoodPFJet[k] = false;  }
      if(CEF >= 0.99) { GoodPFJet[k] = false;  }
      if(NHF >= 0.99) { GoodPFJet[k] = false;  }
      if(CHF <= 0.) { GoodPFJet[k] = false;  }
      if(chgMult <= 0) { GoodPFJet[k] = false; }
      if(numConst <= 1) { GoodPFJet[k] = false; }

      if (GoodPFJet[k]) {
	numGoodPFJets++;
	if ( jets_AK5PF_pt->at(k) > P_leadJet ) P_leadJet = jets_AK5PF_pt->at(k) ;
      }
    }


    float HT = 0;  // Scalar sum of jet pt's
    // HT is computed only as the scalar sum of the pt's of the jets passing the selection
    for (unsigned int it = 0; it<jets_AK5PF_pt->size(); it++) {
      if (GoodPFJet[it]){
        HT += jets_AK5PF_pt->at(it);
      }
    }

    // Determine if this is a good event, passing the filter.
    if ( numPFmu>=2 || numPFel>=2 || (HT>200 && PFMET>100 && numGoodPFJets>=2 ) ) 
      goodevent = true;
    
    if (goodevent) {
      noutput++;
      newtreeA->Fill();
      newtreeB->Fill();
    }

  }

  newtreeA->AutoSave();
  newtreeB->AutoSave();

  newFile->Write();
  newFile->Close();

  cout << "Wrote " << noutput << " out of " << nentries << endl;

}
