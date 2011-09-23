import FWCore.ParameterSet.Config as cms

basicKinematicLeaves = cms.PSet(
	status = cms.string('status'),
	phi = cms.string('phi'),
	pt = cms.string('pt'),
	pz = cms.string('pz'),
	px = cms.string('px'),
	py = cms.string('py'),
	eta = cms.string('eta'),
	theta = cms.string('theta'),
	et = cms.string('et'),
	energy = cms.string('energy')
)
TriggerPSets = cms.PSet(
	#trigger bits 8e29
	HLTriggerFirstPath = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_L1Jet6U = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_Jet15U = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_Jet30U = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_Jet50U = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_FwdJet20U = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_DiJetAve15U_8E29 = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_DiJetAve30U_8E29 = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_QuadJet15U = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_L1MET20 = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_MET45 = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_MET100 = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_HT100U = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_L1MuOpen = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_L1Mu = cms.PSet(
		src = cms.InputTag("TriggerResults","","HLT"),
		method = cms.string('HLTBitVariable')
	),
	HLT_L1Mu20 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_L2Mu9 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_L2Mu11 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_IsoMu3 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Mu3 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Mu5 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Mu9 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_L1DoubleMuOpen = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_DoubleMu0 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_DoubleMu3 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_L1SingleEG5 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_L1SingleEG8 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Ele10_LW_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Ele10_LW_EleId_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Ele15_LW_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Ele15_SC10_LW_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Ele15_SiStrip_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Ele20_LW_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_L1DoubleEG5 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_DoubleEle5_SW_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_DoublePhoton5_eeRes_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_DoublePhoton5_Jpsi_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_DoublePhoton5_Upsilon_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Photon10_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Photon15_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Photon15_TrackIso_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Photon15_LooseEcalIso_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Photon20_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_Photon30_L1R_8E29 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_DoublePhoton10_L1R = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_SingleLooseIsoTau20 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_DoubleLooseIsoTau15 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_BTagMu_Jet10U = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_BTagIP_Jet50U = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_StoppedHSCP_8E29 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_L1Mu14_L1SingleEG10 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_L1Mu14_L1SingleJet6U = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_L1Mu14_L1ETM30 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_ZeroBias = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_MinBiasHcal = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_MinBiasEcal = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_MinBiasPixel = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_MinBiasPixel_Trk5 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_CSCBeamHalo = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_CSCBeamHaloOverlapRing1 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_CSCBeamHaloOverlapRing2 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_CSCBeamHaloRing2or3 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_BackwardBSC = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_ForwardBSC = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_TrackerCosmics = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLT_IsoTrack_8E29 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	AlCa_HcalPhiSym = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	AlCa_EcalPhiSym = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	AlCa_EcalPi0_8E29 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	AlCa_EcalEta_8E29 = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	AlCa_RPCMuonNoHits = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	AlCa_RPCMuonNormalisation = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLTriggerFinalPath = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),
	HLTAnalyzerEndpath = cms.PSet(
	        src = cms.InputTag("TriggerResults","","HLT"),
	        method = cms.string('HLTBitVariable')
	        ),                                                                                                                                                                                                                                                                                                                                  
        HLT_Jet70U = cms.PSet(
                src = cms.InputTag("TriggerResults","","HLT"),
                method = cms.string('HLTBitVariable')
                ),
        HLT_Jet100U = cms.PSet(
                src = cms.InputTag("TriggerResults","","HLT"),
                method = cms.string('HLTBitVariable')
                ),
        HLT_DiJetAve50U = cms.PSet(
                src = cms.InputTag("TriggerResults","","HLT"),
                method = cms.string('HLTBitVariable')
                ),


)
isoAxis = cms.PSet(
    nBins = cms.uint32(100),
    Max = cms.double(20.0),
    Min = cms.double(0.0)
)
eTaxis = cms.PSet(
    nBins = cms.uint32(600),
    Max = cms.double(1200.0),
    Min = cms.double(0.0)
)
#Main module to create the two trees and histograms (these histograms are not from the trees)
configurableAnalysis = cms.EDFilter("ConfigurableAnalysis",
    Selections = cms.PSet(
        filters = cms.PSet(
#            leadingMuon = cms.PSet(
#                src = cms.string('muons'),
#                cut = cms.vstring('pt > 20.0 & abs(eta) < 3.0'),
#                cut = cms.vstring(''),
#                selector = cms.string('patMuonSEventSelector')
#                selector = cms.string('')
#            )#,
#            leadingElectron = cms.PSet(
#                src = cms.string('electrons'),
#                cut = cms.vstring('pt > 20.0 & abs(eta) < 3.0'),
#                selector = cms.string('patElectronSEventSelector')
#            )
        ),
        selections = cms.PSet(
            minSelection = cms.PSet(
                filterOrder = cms.vstring(''),
                makeFinalPlots = cms.bool(True),
                makeSummaryTable = cms.bool(True),
                makeContentPlots = cms.bool(True),
                makeAllButOnePlots = cms.bool(True),
                ntuplize = cms.bool(True),
                nMonitor = cms.uint32(1000),
                makeCumulativePlots = cms.bool(True)
            )
        )
    ),
    Plotter = cms.PSet(
        TH1s = cms.PSet(

        ),
        ComponentName = cms.string('VariablePlotter'),
        TProfiles = cms.PSet(

        ),
        TH2s = cms.PSet(

        )
    ),
    Variables = cms.PSet(
        TriggerPSets,

        L1Bit = cms.PSet(
            src = cms.InputTag("gtDigis"),
            method = cms.string('ComputedVariable'),
            computer = cms.string('L1BitComputer')
            )
    ),
    workAsASelector = cms.bool(True),
    flows = cms.vstring('minSelection'),
    InputTags = cms.PSet(
#        genParticles = cms.InputTag("genParticles"),
        mets = cms.InputTag("layer1METs"),
        genMuons = cms.InputTag("genMuons"),
        genElectrons = cms.InputTag("genElectrons"),
        electrons = cms.InputTag("cleanPatElectrons"),#changed from allLayer1Electrons
				muons = cms.InputTag("cleanPatMuons"),
        jets = cms.InputTag("cleanPatJetsSC5Calo"),
        genJets = cms.InputTag("iterativeCone5GenJetsNoNuBSM")
    ),
    Ntupler = cms.PSet(
        branchesPSet = cms.PSet(
            treeName = cms.string('eventB'),
						
            pv = cms.PSet(
                src = cms.InputTag("offlinePrimaryVertices"),
                 leaves = cms.PSet(
                       vars = cms.vstring(
                          'x:x',
                          'y:y',
                          'z:z',
                          'xErr:xError',
                          'yErr:yError',
                          'zErr:zError',
                          'chi2:chi2',
                          'ndof:ndof',
                          'isFake:isFake',               
                          'isValid:isValid',
                          'tracksSize:tracksSize'
											 
               		),
               ),
               Class = cms.string('reco::Vertex'),
           ),

           beamSpot = cms.PSet(  
           	src = cms.InputTag("offlineBeamSpot"),
            leaves = cms.PSet(
                vars = cms.vstring(
                     'x:position.x',
                     'y:position.y',
                     'z:position.z',
                     'x0Error:x0Error',
                     'y0Error:y0Error',
                     'z0Error:z0Error',
                     'sigmaZ:sigmaZ',
                     'sigmaZ0Error:sigmaZ0Error',
                     'dxdz:dxdz',
                     'dxdzError:dxdzError',
                     'dydz:dydz',
                     'dydzError:dydzError',
                     'beamWidthX:BeamWidthX',#addedFB
                     'beamWidthY:BeamWidthY',#addedFB
                     #'beamWidth:BeamWidth',
                     'beamWidthXError:BeamWidthXError',#addedFB
                     'beamWidthYError:BeamWidthYError'#addedFB
                     #'beamWidthError:BeamWidthError'
                       )
                ),
            Class = cms.string('reco::BeamSpot')
            ),
                                                                              
            mus = cms.PSet(
                src = cms.string('muons'),
                leaves = cms.PSet(
                    basicKinematicLeaves,
                    vars = cms.vstring(
                        'gen_id:genLepton.pdgId',
                        'gen_phi:genLepton.phi',
                        'gen_pt:genLepton.pt',
                        'gen_pz:genLepton.pz',
                        'gen_px:genLepton.px',
                        'gen_py:genLepton.py',
                        'gen_eta:genLepton.eta',
                        'gen_theta:genLepton.theta',
                        'gen_et:genLepton.et',                       
                        'gen_mother_id:genLepton.mother.pdgId',
                        'gen_mother_phi:genLepton.mother.phi',
                        'gen_mother_pt:genLepton.mother.pt',
                        'gen_mother_pz:genLepton.mother.pz',
                        'gen_mother_px:genLepton.mother.px',
                        'gen_mother_py:genLepton.mother.py',
                        'gen_mother_eta:genLepton.mother.eta',
                        'gen_mother_theta:genLepton.mother.theta',
                        'gen_mother_et:genLepton.mother.et',                       
                        'tkHits:track.hitPattern.numberOfValidHits', 
                        'cIso:caloIso', 
                        'tIso:trackIso',
                        'ecalIso:ecalIso',
                        'hcalIso:hcalIso',
                        'ecalvetoDep:ecalIsoDeposit.candEnergy',
                        'hcalvetoDep:hcalIsoDeposit.candEnergy',
#                        'id:leptonID', 
                        'calEnergyEm:calEnergy.em',
                        'calEnergyHad:calEnergy.had',
                        'calEnergyHo:calEnergy.ho',
                        'calEnergyEmS9:calEnergy.emS9',
                        'calEnergyHadS9:calEnergy.hadS9',
                        'calEnergyHoS9:calEnergy.hoS9',
                        'iso03_sumPt:isolationR03.sumPt',
                        'iso03_emEt:isolationR03.emEt',
                        'iso03_hadEt:isolationR03.hadEt',
                        'iso03_hoEt:isolationR03.hoEt',
                        'iso03_nTracks:isolationR03.nTracks',
                        'iso05_sumPt:isolationR05.sumPt',
                        'iso05_emEt:isolationR05.emEt',
                        'iso05_hadEt:isolationR05.hadEt',
                        'iso05_hoEt:isolationR05.hoEt',
                        'iso05_nTracks:isolationR05.nTracks',
                        'charge:charge', 
                        'cm_chi2:combinedMuon.chi2', 
                        'cm_ndof:combinedMuon.ndof', 
                        'cm_chg:combinedMuon.charge', 
                        'cm_pt:combinedMuon.pt', 
                        'cm_px:combinedMuon.px', 
                        'cm_py:combinedMuon.py', 
                        'cm_pz:combinedMuon.pz', 
                        'cm_eta:combinedMuon.eta', 
                        'cm_phi:combinedMuon.phi', 
                        'cm_theta:combinedMuon.theta', 
                        'cm_d0dum:combinedMuon.d0', 
                        'cm_dz:combinedMuon.dz', 
                        'cm_vx:combinedMuon.vx', 
                        'cm_vy:combinedMuon.vy', 
                        'cm_vz:combinedMuon.vz', 
                        'cm_numvalhits:combinedMuon.numberOfValidHits', 
                        'cm_numlosthits:combinedMuon.numberOfLostHits', 
                        'cm_numvalMuonhits:combinedMuon.hitPattern.numberOfValidMuonHits',
                        'cm_d0dumErr:combinedMuon.d0Error', 
                        'cm_dzErr:combinedMuon.dzError', 
                        'cm_ptErr:combinedMuon.ptError', 
                        'cm_etaErr:combinedMuon.etaError', 
                        'cm_phiErr:combinedMuon.phiError', 
                        'tk_id:track.key',
                        'tk_chi2:track.chi2',
                        'tk_ndof:track.ndof', 
                        'tk_chg:track.charge', 
                        'tk_pt:track.pt', 
                        'tk_px:track.px', 
                        'tk_py:track.py', 
                        'tk_pz:track.pz', 
                        'tk_eta:track.eta', 
                        'tk_phi:track.phi', 
                        'tk_theta:track.theta', 
                        'tk_d0dum:track.d0', 
                        'tk_dz:track.dz', 
                        'tk_vx:track.vx', 
                        'tk_vy:track.vy', 
                        'tk_vz:track.vz', 
                        'tk_numvalhits:track.numberOfValidHits', 
                        'tk_numlosthits:track.numberOfLostHits', 
                        'tk_d0dumErr:track.d0Error', 
                        'tk_dzErr:track.dzError', 
                        'tk_ptErr:track.ptError', 
                        'tk_etaErr:track.etaError', 
                        'tk_phiErr:track.phiError', 
                        'tk_numvalPixelhits:track.hitPattern.numberOfValidPixelHits',
                        'tk_numpixelWthMeasr:track.hitPattern.pixelLayersWithMeasurement',
                        'stamu_chi2:standAloneMuon.chi2', 
                        'stamu_ndof:standAloneMuon.ndof', 
                        'stamu_chg:standAloneMuon.charge', 
                        'stamu_pt:standAloneMuon.pt', 
                        'stamu_px:standAloneMuon.px', 
                        'stamu_py:standAloneMuon.py', 
                        'stamu_pz:standAloneMuon.pz', 
                        'stamu_eta:standAloneMuon.eta', 
                        'stamu_phi:standAloneMuon.phi', 
                        'stamu_theta:standAloneMuon.theta', 
                        'stamu_d0dum:standAloneMuon.d0',
                        'stamu_dz:standAloneMuon.dz', 
                        'stamu_vx:standAloneMuon.vx', 
                        'stamu_vy:standAloneMuon.vy', 
                        'stamu_vz:standAloneMuon.vz', 
                        'stamu_numvalhits:standAloneMuon.numberOfValidHits', 
                        'stamu_numlosthits:standAloneMuon.numberOfLostHits', 
                        'stamu_d0dumErr:standAloneMuon.d0Error', 
                        'stamu_dzErr:standAloneMuon.dzError', 
                        'stamu_ptErr:standAloneMuon.ptError', 
                        'stamu_etaErr:standAloneMuon.etaError', 
                        'stamu_phiErr:standAloneMuon.phiError', 
                        'num_matches:numberOfMatches',
                        'isTrackerMuon:isTrackerMuon',
                        'isStandAloneMuon:isStandAloneMuon',
                        'isCaloMuon:isCaloMuon',
                        'isGlobalMuon:isGlobalMuon',
                        'isElectron:isElectron',
                        'isConvertedPhoton:isConvertedPhoton',
                        'isPhoton:isPhoton',
                        'id_All:isGood("All")',
                        'id_AllGlobalMuons:isGood("AllGlobalMuons")',
                        'id_AllStandAloneMuons:isGood("AllStandAloneMuons")',
                        'id_AllTrackerMuons:isGood("AllTrackerMuons")',
                        'id_TrackerMuonArbitrated:isGood("TrackerMuonArbitrated")',
                        'id_AllArbitrated:isGood("AllArbitrated")',
                        'id_GlobalMuonPromptTight:isGood("GlobalMuonPromptTight")',
                        'id_TMLastStationLoose:isGood("TMLastStationLoose")',                        
                        'id_TMLastStationTight:isGood("TMLastStationTight")',
                        'id_TM2DCompatibilityLoose:isGood("TM2DCompatibilityLoose")',
                        'id_TM2DCompatibilityTight:isGood("TM2DCompatibilityTight")',                        
                        'id_TMOneStationLoose:isGood("TMOneStationLoose")',
                        'id_TMOneStationTight:isGood("TMOneStationTight")',
                        'id_TMLastStationOptimizedLowPtLoose:isGood("TMLastStationOptimizedLowPtLoose")',
                        'id_TMLastStationOptimizedLowPtTight:isGood("TMLastStationOptimizedLowPtTight")',
												'tk_LayersWithMeasurement:track.hitPattern.trackerLayersWithMeasurement',
                       'tk_PixelLayersWithMeasurement:track.hitPattern.pixelLayersWithMeasurement',
                       'tk_ValidStripLayersWithMonoAndStereoHit:track.hitPattern.numberOfValidStripLayersWithMonoAndStereo',
                       'tk_LayersWithoutMeasurement:track.hitPattern.trackerLayersWithoutMeasurement',
                       'tk_ExpectedHitsInner:track.trackerExpectedHitsInner.numberOfHits',
                       'tk_ExpectedHitsOuter:track.trackerExpectedHitsOuter.numberOfHits',
                       'cm_LayersWithMeasurement:combinedMuon.hitPattern.trackerLayersWithMeasurement',
                       'cm_PixelLayersWithMeasurement:combinedMuon.hitPattern.pixelLayersWithMeasurement',
                       'cm_ValidStripLayersWithMonoAndStereoHit:combinedMuon.hitPattern.numberOfValidStripLayersWithMonoAndStereo',
                       'cm_LayersWithoutMeasurement:combinedMuon.hitPattern.trackerLayersWithoutMeasurement',
                       'cm_ExpectedHitsInner:combinedMuon.trackerExpectedHitsInner.numberOfHits',
                       'cm_ExpectedHitsOuter:combinedMuon.trackerExpectedHitsOuter.numberOfHits',
                       'picky_LayersWithMeasurement:pickyMuon.hitPattern.trackerLayersWithMeasurement',
                       'picky_PixelLayersWithMeasurement:pickyMuon.hitPattern.pixelLayersWithMeasurement',
                       'picky_ValidStripLayersWithMonoAndStereoHit:pickyMuon.hitPattern.numberOfValidStripLayersWithMonoAndStereo',
                       'picky_LayersWithoutMeasurement:pickyMuon.hitPattern.trackerLayersWithoutMeasurement',
                       'picky_ExpectedHitsInner:pickyMuon.trackerExpectedHitsInner.numberOfHits',
                       'picky_ExpectedHitsOuter:pickyMuon.trackerExpectedHitsOuter.numberOfHits',
                       'tpfms_LayersWithMeasurement:tpfmsMuon.hitPattern.trackerLayersWithMeasurement',
                       'tpfms_PixelLayersWithMeasurement:tpfmsMuon.hitPattern.pixelLayersWithMeasurement',
                       'tpfms_ValidStripLayersWithMonoAndStereoHit:tpfmsMuon.hitPattern.numberOfValidStripLayersWithMonoAndStereo',
                       'tpfms_LayersWithoutMeasurement:tpfmsMuon.hitPattern.trackerLayersWithoutMeasurement',
                       'tpfms_ExpectedHitsInner:tpfmsMuon.trackerExpectedHitsInner.numberOfHits',
                       'tpfms_ExpectedHitsOuter:tpfmsMuon.trackerExpectedHitsOuter.numberOfHits',
                       'picky_id:pickyMuon.key',
                       'picky_chi2:pickyMuon.chi2',
                       'picky_ndof:pickyMuon.ndof',
                       'picky_chg:pickyMuon.charge',
                       'picky_pt:pickyMuon.pt',
                       'picky_px:pickyMuon.px',
                       'picky_py:pickyMuon.py',
                       'picky_pz:pickyMuon.pz',
                       'picky_eta:pickyMuon.eta',
                       'picky_phi:pickyMuon.phi',
                       'picky_theta:pickyMuon.theta',
                       'picky_d0dum:pickyMuon.d0',
                       'picky_dz:pickyMuon.dz',
                       'picky_vx:pickyMuon.vx',
                       'picky_vy:pickyMuon.vy',
                       'picky_vz:pickyMuon.vz',
                       'picky_numvalhits:pickyMuon.numberOfValidHits',
                       'picky_numlosthits:pickyMuon.numberOfLostHits',
                       'picky_d0dumErr:pickyMuon.d0Error',
                       'picky_dzErr:pickyMuon.dzError',
                       'picky_ptErr:pickyMuon.ptError',
                       'picky_etaErr:pickyMuon.etaError',
                       'picky_phiErr:pickyMuon.phiError',
                       'picky_numvalPixelhits:pickyMuon.hitPattern.numberOfValidPixelHits',
                       'tpfms_id:tpfmsMuon.key',
                       'tpfms_chi2:tpfmsMuon.chi2',
                       'tpfms_ndof:tpfmsMuon.ndof',
                       'tpfms_chg:tpfmsMuon.charge',
                       'tpfms_pt:tpfmsMuon.pt',
                       'tpfms_px:tpfmsMuon.px',
                       'tpfms_py:tpfmsMuon.py',
                       'tpfms_pz:tpfmsMuon.pz',
                       'tpfms_eta:tpfmsMuon.eta',
                       'tpfms_phi:tpfmsMuon.phi',
                       'tpfms_theta:tpfmsMuon.theta',
                       'tpfms_d0dum:tpfmsMuon.d0',
                       'tpfms_dz:tpfmsMuon.dz',
                       'tpfms_vx:tpfmsMuon.vx',
                       'tpfms_vy:tpfmsMuon.vy',
                       'tpfms_vz:tpfmsMuon.vz',
                       'tpfms_numvalhits:tpfmsMuon.numberOfValidHits',
                       'tpfms_numlosthits:tpfmsMuon.numberOfLostHits',
                       'tpfms_d0dumErr:tpfmsMuon.d0Error',
                       'tpfms_dzErr:tpfmsMuon.dzError',
                       'tpfms_ptErr:tpfmsMuon.ptError',
                       'tpfms_etaErr:tpfmsMuon.etaError',
                       'tpfms_phiErr:tpfmsMuon.phiError',
                       'tpfms_numvalPixelhits:tpfmsMuon.hitPattern.numberOfValidPixelHits',   
												                                                                                                                                      )
                ),
                Class = cms.string('pat::Muon')
            ),




                 mets_AK5 = cms.PSet(
#                src = cms.InputTag("allLayer1METsIC5"),#vhanged to line below
                  src = cms.InputTag("patMETsAK5Calo"),
                   leaves = cms.PSet(
                    vars = cms.vstring('et:et', 
                        'phi:phi', 
                        'ex:px', 
                        'ey:py', 
                        'gen_et:genMET.et', 
                        'gen_phi:genMET.phi',
                        'sign:metSignificance',
                        'sumEt:sumEt', 
                        'unCPhi:uncorrectedPhi', 
                        'unCPt:uncorrectedPt')
                ),
                Class = cms.string('pat::MET')
            ),


                 pfmets = cms.PSet(
#                src = cms.InputTag("allLayer1METsIC5"),#vhanged to line below
                  src = cms.InputTag("patMETsPF"),
                   leaves = cms.PSet(
                    vars = cms.vstring('et:et', 
                        'phi:phi', 
                        'ex:px', 
                        'ey:py', 
                        'gen_et:genMET.et', 
                        'gen_phi:genMET.phi',
                        'sign:metSignificance',
                        'sumEt:sumEt', 
                        'unCPhi:uncorrectedPhi', 
                        'unCPt:uncorrectedPt')
                ),
                Class = cms.string('pat::MET')
            ),


                  pfTypeImets = cms.PSet( 	 
	                   src = cms.InputTag("patMETsTypeIPF"), 	 
	                    leaves = cms.PSet( 	 
	                     vars = cms.vstring('et:et', 	 
	                         'phi:phi', 	 
	                         'ex:px', 	 
	                         'ey:py', 	 
	                         'gen_et:genMET.et', 	 
	                         'gen_phi:genMET.phi', 	 
	                         'sign:metSignificance', 	 
	                         'sumEt:sumEt', 	 
	                         'unCPhi:uncorrectedPhi', 	 
	                         'unCPt:uncorrectedPt') 	 
	                 ), 	 
	                 Class = cms.string('pat::MET') 	 
	             ), 	 
	 


            tcmets = cms.PSet(
                  src = cms.InputTag("patMETsTC"),
                  leaves = cms.PSet(
                      vars = cms.vstring('et:et',
                                         'phi:phi',
                                         'ex:px',
                                         'ey:py',
                                         'sumEt:sumEt',
                                         )
                      ),
                  Class = cms.string('pat::MET')
            ),
                                                                        

            photons = cms.PSet(
                src = cms.InputTag("cleanPatPhotons"),#clean<=>all
                leaves = cms.PSet(
                    basicKinematicLeaves,
                    vars= cms.vstring('hadOverEM:hadronicOverEm',
                                      'scEnergy:superCluster.energy',
                                      'scRawEnergy:superCluster.rawEnergy',
                                      'scEta:superCluster.position.eta',
                                      'scPhi:superCluster.position.phi',
                                      'scEtaWidth:superCluster.etaWidth',
                                      'scPhiWidth:superCluster.phiWidth',
                                      'tIso:trackIso',
                                      'ecalIso:ecalIso',
                                      'hcalIso:hcalIso',
                                      
                                      #'isoEcalRecHit:isolationEcalRecHit',
                                      #'isoHcalRecHit:isolationHcalRecHit',
                                      #'isoSolidTrkCone:isolationSolidTrkCone',
                                      #'isoHollowTrkCone:isolationHollowTrkCone',
                                      #'nTrkSolidCone:nTrkSolidCone',
                                      #'nTrkHollowCone:nTrkHollowCone',
                                      
                                      'isoEcalRecHitDR04:ecalRecHitSumEtConeDR04',
                                      'isoHcalRecHitDR04:hcalTowerSumEtConeDR04',
                                      'isoSolidTrkConeDR04:trkSumPtSolidConeDR04',
                                      'isoHollowTrkConeDR04:trkSumPtHollowConeDR04',
                                      'nTrkSolidConeDR04:nTrkSolidConeDR04',
                                      'nTrkHollowConeDR04:nTrkSolidConeDR04',
                                      'isoEcalRecHitDR03:ecalRecHitSumEtConeDR03',
                                      'isoHcalRecHitDR03:hcalTowerSumEtConeDR03',
                                      'isoSolidTrkConeDR03:trkSumPtSolidConeDR03',
                                      'isoHollowTrkConeDR03:trkSumPtHollowConeDR03',
                                      'nTrkSolidConeDR03:nTrkSolidConeDR03',
                                      'nTrkHollowConeDR03:nTrkSolidConeDR03',
                                      

                                      #'isAlsoElectron:isAlsoElectron',
                                      'isAlsoElectron:isElectron',
                                      
                                      'hasPixelSeed:hasPixelSeed',
                                      #'isConverted:isConverted',
                                      'isConverted:isConvertedPhoton',
                                      'isEBGap:isEBGap',
                                      'isEEGap:isEEGap',
                                      'isEBEEGap:isEBEEGap',
                                      'isEBPho:isEB',#changed from isEBPho
                                      'isEEPho:isEE',#changed from isEEPho
                                      #'isLooseEM:isLooseEM',
                                      #'isLoosePhoton:isLoosePhoton',
                                      #'isTightPhoton:isTightPhoton',
                                      'isLoosePhoton:photonID("PhotonCutBasedIDLoose")',
                                      'isTightPhoton:photonID("PhotonCutBasedIDLoose")',
                                      #Currently (28-07) all photons are defined as LooseEM, but this will be added again as
                                      # they are going to relax pre-selection cuts on the photon 
                                      #'isLooseEM:photonID()',
                                      'maxEnergyXtal:maxEnergyXtal',
                                      'e1x5:e1x5',
                                      'e2x5:e2x5',
                                      'e3x3:e3x3',
                                      'e5x5:e5x5',
                                      'sigmaEtaEta:sigmaEtaEta',
                                      'sigmaIetaIeta:sigmaIetaIeta',
                                      'r9:r9',
                                      'gen_et:genPhoton.et',
                                      'gen_eta:genPhoton.eta',
                                      'gen_phi:genPhoton.phi',
                                      'gen_id:genPhoton.pdgId'
                                      )
                                      ),
                    
                Class = cms.string('pat::Photon')
            ),

            mc_doc = cms.PSet(
                src = cms.InputTag("genParticles"),
                leaves = cms.PSet(
                    vars = cms.vstring('id:pdgId',
                        'pt:pt',
                        'px:px',
                        'py:py',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'energy:energy',
                        'status:status',
                        'charge:charge',
                        'mother_id:mother.pdgId',
                        'grandmother_id:mother.mother.pdgId',
                        'ggrandmother_id:mother.mother.mother.pdgId',
                        'mother_pt:mother.pt',
                        'vertex_x:vertex.x',
                        'vertex_y:vertex.y',
                        'vertex_z:vertex.z',
                        'mass:mass',
                        'numOfDaughters:numberOfDaughters',
                        'numOfMothers:numberOfMothers'
                                       )
                ),
                selection = cms.string('status=3'),
                Class = cms.string('reco::GenParticle')
            ),
            mc_mus = cms.PSet(
                src = cms.InputTag("genParticles"),
                leaves = cms.PSet(
                    vars = cms.vstring('id:pdgId',
                        'pt:pt',
                        'px:px',
                        'py:py',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'status:status',
                        'energy:energy',
                        'charge:charge',
                        'mother_id:mother.pdgId',
                        'mother_pt:mother.pt',
                        'grandmother_id:mother.mother.pdgId',
                        'ggrandmother_id:mother.mother.mother.pdgId',
                        'vertex_x:vertex.x',
                        'vertex_y:vertex.y',
                        'vertex_z:vertex.z',
                        'mass:mass',
                        'numOfDaughters:numberOfDaughters')
                ),
                selection = cms.string('status!=3 & (pdgId=13 | pdgId=-13)'),
                Class = cms.string('reco::GenParticle')
            ),
            mc_electrons = cms.PSet(
                src = cms.InputTag("genParticles"),
                leaves = cms.PSet(
                    vars = cms.vstring('id:pdgId',
                        'pt:pt',
                        'px:px',
                        'py:py',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'status:status',
                        'energy:energy',
                        'charge:charge',
                        'mother_id:mother.pdgId',
                        'mother_pt:mother.pt',
                        'grandmother_id:mother.mother.pdgId',
                        'ggrandmother_id:mother.mother.mother.pdgId',
                        'vertex_x:vertex.x',
                        'vertex_y:vertex.y',
                        'vertex_z:vertex.z',
                        'mass:mass',
                        'numOfDaughters:numberOfDaughters')
                ),
                selection = cms.string('status!=3 & (pdgId=11 | pdgId=-11)'),
                Class = cms.string('reco::GenParticle')
            ),

            mc_taus = cms.PSet(
                src = cms.InputTag("genParticles"),
                leaves = cms.PSet(
                    vars = cms.vstring('id:pdgId',
                        'pt:pt',
                        'px:px',
                        'py:py',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'status:status',
                        'energy:energy',
                        'charge:charge',
                        'mother_id:mother.pdgId',
                        'mother_pt:mother.pt',
                        'grandmother_id:mother.mother.pdgId',
                        'ggrandmother_id:mother.mother.mother.pdgId',
                        'vertex_x:vertex.x',
                        'vertex_y:vertex.y',
                        'vertex_z:vertex.z',
                        'mass:mass',
                        'numOfDaughters:numberOfDaughters')
                ),
                selection = cms.string('status!=3 & (pdgId=15 | pdgId=-15)'),
                Class = cms.string('reco::GenParticle')
            ),

            mc_photons = cms.PSet(
                src = cms.InputTag("genParticles"),
                leaves = cms.PSet(
                    vars = cms.vstring('id:pdgId',
                        'pt:pt',
                        'px:px',
                        'py:py',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'status:status',
                        'energy:energy',
                        'charge:charge',
                        'mother_id:mother.pdgId',
                        'mother_pt:mother.pt',
                        'grandmother_id:mother.mother.pdgId',
                        'ggrandmother_id:mother.mother.mother.pdgId',
                        'vertex_x:vertex.x',
                        'vertex_y:vertex.y',
                        'vertex_z:vertex.z',
                        'mass:mass',
                        'numOfDaughters:numberOfDaughters')
                ),
                selection = cms.string('status!=3 & (pdgId=22) & pt>10'),
                Class = cms.string('reco::GenParticle')
            ),

            mc_nutaus = cms.PSet(
                src = cms.InputTag("genParticles"),
                leaves = cms.PSet(
                    vars = cms.vstring('id:pdgId',
                        'pt:pt',
                        'px:px',
                        'py:py',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'status:status',
                        'energy:energy',
                        'charge:charge',
                        'mother_id:mother.pdgId',
                        'mother_pt:mother.pt',
                        'grandmother_id:mother.mother.pdgId',
                        'ggrandmother_id:mother.mother.mother.pdgId',
                        'vertex_x:vertex.x',
                        'vertex_y:vertex.y',
                        'vertex_z:vertex.z',
                        'mass:mass',
                        'numOfDaughters:numberOfDaughters')
                ),
                selection = cms.string('status!=3 & (pdgId=16 | pdgId=-16)'),
                Class = cms.string('reco::GenParticle')
            ),
            mc_nues = cms.PSet(
                src = cms.InputTag("genParticles"),
                leaves = cms.PSet(
                    vars = cms.vstring('id:pdgId',
                        'pt:pt',
                        'px:px',
                        'py:py',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'status:status',
                        'energy:energy',
                        'charge:charge',
                        'mother_id:mother.pdgId',
                        'mother_pt:mother.pt',
                        'grandmother_id:mother.mother.pdgId',
                        'ggrandmother_id:mother.mother.mother.pdgId',
                        'vertex_x:vertex.x',
                        'vertex_y:vertex.y',
                        'vertex_z:vertex.z',
                        'mass:mass',
                        'numOfDaughters:numberOfDaughters')
                ),
                selection = cms.string('status!=3 & (pdgId=12 | pdgId=-12)'),
                Class = cms.string('reco::GenParticle')
            ),
            mc_numus = cms.PSet(
                src = cms.InputTag("genParticles"),
                leaves = cms.PSet(
                    vars = cms.vstring('id:pdgId',
                        'pt:pt',
                        'px:px',
                        'py:py',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'status:status',
                        'energy:energy',
                        'charge:charge',
                        'mother_id:mother.pdgId',
                        'mother_pt:mother.pt',
                        'grandmother_id:mother.mother.pdgId',
                        'ggrandmother_id:mother.mother.mother.pdgId',
                        'vertex_x:vertex.x',
                        'vertex_y:vertex.y',
                        'vertex_z:vertex.z',
                        'mass:mass',
                        'numOfDaughters:numberOfDaughters')
                ),
                selection = cms.string('status!=3 & (pdgId=14 | pdgId=-14)'),
                Class = cms.string('reco::GenParticle')
            ),

            pfcand_mus = cms.PSet(
                src = cms.InputTag("particleFlow"),
                leaves = cms.PSet(
                    vars = cms.vstring(
			'particleId:particleId',
                        'pt:pt',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'energy:energy',
                        'charge:charge'
                     )
                ),
                selection = cms.string('particleId=3'),
                Class = cms.string('reco::PFCandidate')
            ),

            pfcand_els = cms.PSet(
                src = cms.InputTag("particleFlow"),
                leaves = cms.PSet(
                    vars = cms.vstring(
                        'particleId:particleId',
                        'pt:pt',
                        'pz:pz',
                        'eta:eta',
                        'phi:phi',
                        'theta:theta',
                        'energy:energy',
                        'charge:charge'
                     )
                ),
                selection = cms.string('particleId=2'),
                Class = cms.string('reco::PFCandidate')
            ),

            pf_mus = cms.PSet(
                src = cms.InputTag("selectedPatMuonsPF"),
                leaves = cms.PSet(
                    basicKinematicLeaves,
                    vars = cms.vstring(
                        'gen_id:genLepton.pdgId',
                        'gen_phi:genLepton.phi',
                        'gen_pt:genLepton.pt',
                        'gen_pz:genLepton.pz',
                        'gen_px:genLepton.px',
                        'gen_py:genLepton.py',
                        'gen_eta:genLepton.eta',
                        'gen_theta:genLepton.theta',
                        'gen_et:genLepton.et',
                        'gen_mother_id:genLepton.mother.pdgId',
                        'gen_mother_phi:genLepton.mother.phi',
                        'gen_mother_pt:genLepton.mother.pt',
                        'gen_mother_pz:genLepton.mother.pz',
                        'gen_mother_px:genLepton.mother.px',
                        'gen_mother_py:genLepton.mother.py',
                        'gen_mother_eta:genLepton.mother.eta',
                        'gen_mother_theta:genLepton.mother.theta',
                        'gen_mother_et:genLepton.mother.et',
                        'tkHits:track.hitPattern.numberOfValidHits',
                        'cIso:caloIso',
                        'tIso:trackIso',
                        'ecalIso:ecalIso',
                        'hcalIso:hcalIso',
                        'ecalvetoDep:ecalIsoDeposit.candEnergy',
                        'hcalvetoDep:hcalIsoDeposit.candEnergy',
#                        'id:leptonID',
                        'calEnergyEm:calEnergy.em',
                        'calEnergyHad:calEnergy.had',
                        'calEnergyHo:calEnergy.ho',
                        'calEnergyEmS9:calEnergy.emS9',
                        'calEnergyHadS9:calEnergy.hadS9',
                        'calEnergyHoS9:calEnergy.hoS9',
                        'iso03_sumPt:isolationR03.sumPt',
                        'iso03_emEt:isolationR03.emEt',
                        'iso03_hadEt:isolationR03.hadEt',
                        'iso03_hoEt:isolationR03.hoEt',
                        'iso03_nTracks:isolationR03.nTracks',
                        'iso05_sumPt:isolationR05.sumPt',
                        'iso05_emEt:isolationR05.emEt',
                        'iso05_hadEt:isolationR05.hadEt',
                        'iso05_hoEt:isolationR05.hoEt',
                        'iso05_nTracks:isolationR05.nTracks',
                        'neutralHadronIso:neutralHadronIso',
                        'chargedHadronIso:chargedHadronIso',
                        'photonIso:photonIso',
                        'charge:charge',
                        'cm_chi2:combinedMuon.chi2',
                        'cm_ndof:combinedMuon.ndof',
                        'cm_chg:combinedMuon.charge',
                        'cm_pt:combinedMuon.pt',
                        'cm_px:combinedMuon.px',
                        'cm_py:combinedMuon.py',
                        'cm_pz:combinedMuon.pz',
                        'cm_eta:combinedMuon.eta',
                        'cm_phi:combinedMuon.phi',
                        'cm_theta:combinedMuon.theta',
                        'cm_d0dum:combinedMuon.d0',
                        'cm_dz:combinedMuon.dz',
                        'cm_vx:combinedMuon.vx',
                        'cm_vy:combinedMuon.vy',
                        'cm_vz:combinedMuon.vz',
                        'cm_numvalhits:combinedMuon.numberOfValidHits',
                        'cm_numlosthits:combinedMuon.numberOfLostHits',
                        'cm_numvalMuonhits:combinedMuon.hitPattern.numberOfValidMuonHits',
                        'cm_d0dumErr:combinedMuon.d0Error',
                        'cm_dzErr:combinedMuon.dzError',
                        'cm_ptErr:combinedMuon.ptError',
                        'cm_etaErr:combinedMuon.etaError',
                        'cm_phiErr:combinedMuon.phiError',
                        'tk_id:track.key',
                        'tk_chi2:track.chi2',
                        'tk_ndof:track.ndof',
                        'tk_chg:track.charge',
                        'tk_pt:track.pt',
                        'tk_px:track.px',
                        'tk_py:track.py',
                        'tk_pz:track.pz',
                        'tk_eta:track.eta',
                        'tk_phi:track.phi',
                        'tk_theta:track.theta',
                        'tk_d0dum:track.d0',
                        'tk_dz:track.dz',
                        'tk_vx:track.vx',
                        'tk_vy:track.vy',
                        'tk_vz:track.vz',
                        'tk_numvalhits:track.numberOfValidHits',
                        'tk_numlosthits:track.numberOfLostHits',
                        'tk_d0dumErr:track.d0Error',
                        'tk_dzErr:track.dzError',
                        'tk_ptErr:track.ptError',
                        'tk_etaErr:track.etaError',
                        'tk_phiErr:track.phiError',
                        'tk_numvalPixelhits:track.hitPattern.numberOfValidPixelHits',
                        'tk_numpixelWthMeasr:track.hitPattern.pixelLayersWithMeasurement',
                        'stamu_chi2:standAloneMuon.chi2',
                        'stamu_ndof:standAloneMuon.ndof',
                        'stamu_chg:standAloneMuon.charge',
                        'stamu_pt:standAloneMuon.pt',
                        'stamu_px:standAloneMuon.px',
                        'stamu_py:standAloneMuon.py',
                        'stamu_pz:standAloneMuon.pz',
                        'stamu_eta:standAloneMuon.eta',
                        'stamu_phi:standAloneMuon.phi',
                        'stamu_theta:standAloneMuon.theta',
                        'stamu_d0dum:standAloneMuon.d0',
                        'stamu_dz:standAloneMuon.dz',
                        'stamu_vx:standAloneMuon.vx',
                        'stamu_vy:standAloneMuon.vy',
                        'stamu_vz:standAloneMuon.vz',
                        'stamu_numvalhits:standAloneMuon.numberOfValidHits',
                        'stamu_numlosthits:standAloneMuon.numberOfLostHits',
                        'stamu_d0dumErr:standAloneMuon.d0Error',
                        'stamu_dzErr:standAloneMuon.dzError',
                        'stamu_ptErr:standAloneMuon.ptError',
                        'stamu_etaErr:standAloneMuon.etaError',
                        'stamu_phiErr:standAloneMuon.phiError',
                        'num_matches:numberOfMatches',
                        'isTrackerMuon:isTrackerMuon',
                        'isStandAloneMuon:isStandAloneMuon',
                        'isCaloMuon:isCaloMuon',
                        'isGlobalMuon:isGlobalMuon',
                        'isElectron:isElectron',
                        'isConvertedPhoton:isConvertedPhoton',
                        'isPhoton:isPhoton',
                        'id_All:isGood("All")',
                        'id_AllGlobalMuons:isGood("AllGlobalMuons")',
                        'id_AllStandAloneMuons:isGood("AllStandAloneMuons")',
                        'id_AllTrackerMuons:isGood("AllTrackerMuons")',
                        'id_TrackerMuonArbitrated:isGood("TrackerMuonArbitrated")',
                        'id_AllArbitrated:isGood("AllArbitrated")',
                        'id_GlobalMuonPromptTight:isGood("GlobalMuonPromptTight")',
                        'id_TMLastStationLoose:isGood("TMLastStationLoose")',
                        'id_TMLastStationTight:isGood("TMLastStationTight")',
                        'id_TM2DCompatibilityLoose:isGood("TM2DCompatibilityLoose")',
                        'id_TM2DCompatibilityTight:isGood("TM2DCompatibilityTight")',
                        'id_TMOneStationLoose:isGood("TMOneStationLoose")',
                        'id_TMOneStationTight:isGood("TMOneStationTight")',
                        'id_TMLastStationOptimizedLowPtLoose:isGood("TMLastStationOptimizedLowPtLoose")',
                        'id_TMLastStationOptimizedLowPtTight:isGood("TMLastStationOptimizedLowPtTight")',
											 'tk_LayersWithMeasurement:track.hitPattern.trackerLayersWithMeasurement',
                       'tk_PixelLayersWithMeasurement:track.hitPattern.pixelLayersWithMeasurement',
                       'tk_ValidStripLayersWithMonoAndStereoHit:track.hitPattern.numberOfValidStripLayersWithMonoAndStereo',
                       'tk_LayersWithoutMeasurement:track.hitPattern.trackerLayersWithoutMeasurement',
                       'tk_ExpectedHitsInner:track.trackerExpectedHitsInner.numberOfHits',
                       'tk_ExpectedHitsOuter:track.trackerExpectedHitsOuter.numberOfHits',
                       'cm_LayersWithMeasurement:combinedMuon.hitPattern.trackerLayersWithMeasurement',
                       'cm_PixelLayersWithMeasurement:combinedMuon.hitPattern.pixelLayersWithMeasurement',
                       'cm_ValidStripLayersWithMonoAndStereoHit:combinedMuon.hitPattern.numberOfValidStripLayersWithMonoAndStereo',
                       'cm_LayersWithoutMeasurement:combinedMuon.hitPattern.trackerLayersWithoutMeasurement',
                       'cm_ExpectedHitsInner:combinedMuon.trackerExpectedHitsInner.numberOfHits',
                       'cm_ExpectedHitsOuter:combinedMuon.trackerExpectedHitsOuter.numberOfHits',
                       'picky_LayersWithMeasurement:pickyMuon.hitPattern.trackerLayersWithMeasurement',
                       'picky_PixelLayersWithMeasurement:pickyMuon.hitPattern.pixelLayersWithMeasurement',
                       'picky_ValidStripLayersWithMonoAndStereoHit:pickyMuon.hitPattern.numberOfValidStripLayersWithMonoAndStereo',
                       'picky_LayersWithoutMeasurement:pickyMuon.hitPattern.trackerLayersWithoutMeasurement',
                       'picky_ExpectedHitsInner:pickyMuon.trackerExpectedHitsInner.numberOfHits',
                       'picky_ExpectedHitsOuter:pickyMuon.trackerExpectedHitsOuter.numberOfHits',
                       'tpfms_LayersWithMeasurement:tpfmsMuon.hitPattern.trackerLayersWithMeasurement',
                       'tpfms_PixelLayersWithMeasurement:tpfmsMuon.hitPattern.pixelLayersWithMeasurement',
                       'tpfms_ValidStripLayersWithMonoAndStereoHit:tpfmsMuon.hitPattern.numberOfValidStripLayersWithMonoAndStereo',
                       'tpfms_LayersWithoutMeasurement:tpfmsMuon.hitPattern.trackerLayersWithoutMeasurement',
                       'tpfms_ExpectedHitsInner:tpfmsMuon.trackerExpectedHitsInner.numberOfHits',
                       'tpfms_ExpectedHitsOuter:tpfmsMuon.trackerExpectedHitsOuter.numberOfHits',
                       'picky_id:pickyMuon.key',
                       'picky_chi2:pickyMuon.chi2',
                       'picky_ndof:pickyMuon.ndof',
                       'picky_chg:pickyMuon.charge',
                       'picky_pt:pickyMuon.pt',
                       'picky_px:pickyMuon.px',
                       'picky_py:pickyMuon.py',
                       'picky_pz:pickyMuon.pz',
                       'picky_eta:pickyMuon.eta',
                       'picky_phi:pickyMuon.phi',
                       'picky_theta:pickyMuon.theta',
                       'picky_d0dum:pickyMuon.d0',
                       'picky_dz:pickyMuon.dz',
                       'picky_vx:pickyMuon.vx',
                       'picky_vy:pickyMuon.vy',
                       'picky_vz:pickyMuon.vz',
                       'picky_numvalhits:pickyMuon.numberOfValidHits',
                       'picky_numlosthits:pickyMuon.numberOfLostHits',
                       'picky_d0dumErr:pickyMuon.d0Error',
                       'picky_dzErr:pickyMuon.dzError',
                       'picky_ptErr:pickyMuon.ptError',
                       'picky_etaErr:pickyMuon.etaError',
                       'picky_phiErr:pickyMuon.phiError',
                       'picky_numvalPixelhits:pickyMuon.hitPattern.numberOfValidPixelHits',
                       'tpfms_id:tpfmsMuon.key',
                       'tpfms_chi2:tpfmsMuon.chi2',
                       'tpfms_ndof:tpfmsMuon.ndof',
                       'tpfms_chg:tpfmsMuon.charge',
                       'tpfms_pt:tpfmsMuon.pt',
                       'tpfms_px:tpfmsMuon.px',
                       'tpfms_py:tpfmsMuon.py',
                       'tpfms_pz:tpfmsMuon.pz',
                       'tpfms_eta:tpfmsMuon.eta',
                       'tpfms_phi:tpfmsMuon.phi',
                       'tpfms_theta:tpfmsMuon.theta',
                       'tpfms_d0dum:tpfmsMuon.d0',
                       'tpfms_dz:tpfmsMuon.dz',
                       'tpfms_vx:tpfmsMuon.vx',
                       'tpfms_vy:tpfmsMuon.vy',
                       'tpfms_vz:tpfmsMuon.vz',
                       'tpfms_numvalhits:tpfmsMuon.numberOfValidHits',
                       'tpfms_numlosthits:tpfmsMuon.numberOfLostHits',
                       'tpfms_d0dumErr:tpfmsMuon.d0Error',
                       'tpfms_dzErr:tpfmsMuon.dzError',
                       'tpfms_ptErr:tpfmsMuon.ptError',
                       'tpfms_etaErr:tpfmsMuon.etaError',
                       'tpfms_phiErr:tpfmsMuon.phiError',
                       'tpfms_numvalPixelhits:tpfmsMuon.hitPattern.numberOfValidPixelHits',   
									)
                ),
                Class = cms.string('pat::Muon')
            ),

            pf_els = cms.PSet(
                src = cms.InputTag("selectedPatElectronsPF"),
                leaves = cms.PSet(
                    basicKinematicLeaves,
                    vars = cms.vstring(
                        'gen_id:genLepton.pdgId',
                        'gen_phi:genLepton.phi',
                        'gen_pt:genLepton.pt',
                        'gen_pz:genLepton.pz',
                        'gen_px:genLepton.px',
                        'gen_py:genLepton.py',
                        'gen_eta:genLepton.eta',
                        'gen_theta:genLepton.theta',
                        'gen_et:genLepton.et',
                        'gen_mother_id:genLepton.mother.pdgId',
                        'gen_mother_phi:genLepton.mother.phi',
                        'gen_mother_pt:genLepton.mother.pt',
                        'gen_mother_pz:genLepton.mother.pz',
                        'gen_mother_px:genLepton.mother.px',
                        'gen_mother_py:genLepton.mother.py',
                        'gen_mother_eta:genLepton.mother.eta',
                        'gen_mother_theta:genLepton.mother.theta',
                        'gen_mother_et:genLepton.mother.et',
                        'tightId:electronID("eidTight")',
                        'looseId:electronID("eidLoose")',
                        'robustTightId:electronID("eidRobustTight")',
                        'robustLooseId:electronID("eidRobustLoose")',
                        'robustHighEnergyId:electronID("eidRobustHighEnergy")',
                        'simpleEleId95relIso:electronID("simpleEleId95relIso")',
                        'simpleEleId90relIso:electronID("simpleEleId90relIso")',
                        'simpleEleId85relIso:electronID("simpleEleId85relIso")',
                        'simpleEleId80relIso:electronID("simpleEleId80relIso")',
                        'simpleEleId70relIso:electronID("simpleEleId70relIso")',
                        'simpleEleId60relIso:electronID("simpleEleId60relIso")',
                        'simpleEleId95cIso:electronID("simpleEleId95cIso")',
                        'simpleEleId90cIso:electronID("simpleEleId90cIso")',
                        'simpleEleId85cIso:electronID("simpleEleId85cIso")',
                        'simpleEleId80cIso:electronID("simpleEleId80cIso")',
                        'simpleEleId70cIso:electronID("simpleEleId70cIso")',
                        'simpleEleId60cIso:electronID("simpleEleId60cIso")',
                        'cIso:caloIso',
                        'tIso:trackIso',
                        'ecalIso:ecalIso',
                        'hcalIso:hcalIso',
                        'chargedHadronIso:chargedHadronIso',
                        'photonIso:photonIso',
                        'neutralHadronIso:neutralHadronIso',
                        'chi2:gsfTrack.chi2',
#                        'class:classification',
                        'charge:charge',
                        'caloEnergy:caloEnergy',
                        'hadOverEm:hadronicOverEm',
                        'eOverPIn:eSuperClusterOverP',
                        'eSeedOverPOut:eSeedClusterOverPout',
                        'sigmaEtaEta:scSigmaEtaEta',
                        'sigmaIEtaIEta:scSigmaIEtaIEta',
                        'scEnergy:superCluster.energy',
                        'scRawEnergy:superCluster.rawEnergy',
                        'scSeedEnergy:superCluster.seed.energy',
                        'scEta:superCluster.position.eta',
                        'scPhi:superCluster.position.phi',
                        'scEtaWidth:superCluster.etaWidth',
                        'scPhiWidth:superCluster.phiWidth',
                        'scE1x5:scE1x5',
                        'scE2x5Max:scE2x5Max',
                        'scE5x5:scE5x5',
                        'isEB:isEB',
                        'isEE:isEE',
                        'dEtaIn:deltaEtaSuperClusterTrackAtVtx',
                        'dPhiIn:deltaPhiSuperClusterTrackAtVtx',
                        'dEtaOut:deltaEtaSeedClusterTrackAtCalo',
                        'dPhiOut:deltaPhiSeedClusterTrackAtCalo',
                        'numvalhits:gsfTrack.numberOfValidHits',
                        'numlosthits:gsfTrack.numberOfLostHits',
                        #'numCluster:numberOfClusters',
                        'basicClustersSize:basicClustersSize',
                        'tk_pz:gsfTrack.pz',
                        'tk_pt:gsfTrack.pt',
                        'tk_phi:gsfTrack.phi',
                        'tk_eta:gsfTrack.eta',
                        'd0dum:gsfTrack.d0',
                        'dz:gsfTrack.dz',
                        'vx:gsfTrack.vx',
                        'vy:gsfTrack.vy',
                        'vz:gsfTrack.vz',
                        'ndof:gsfTrack.ndof',
                        'ptError:gsfTrack.ptError',
                        'd0dumError:gsfTrack.d0Error',
                        'dzError:gsfTrack.dzError',
                        'etaError:gsfTrack.etaError',
                        'phiError:gsfTrack.phiError',
                        'tk_charge:gsfTrack.charge',
                        'core_ecalDrivenSeed:core.ecalDrivenSeed',
                        'n_inner_layer:gsfTrack.trackerExpectedHitsInner.numberOfHits',
                        'n_outer_layer:gsfTrack.trackerExpectedHitsOuter.numberOfHits',
                        'ctf_tk_id:closestCtfTrackRef.key',
                        'ctf_tk_charge:closestCtfTrackRef.charge',
                        'ctf_tk_eta:closestCtfTrackRef.eta',
                        'ctf_tk_phi:closestCtfTrackRef.phi',
                        'fbrem:fbrem',
                        'shFracInnerHits:shFracInnerHits',
                        'dr03EcalRecHitSumEt:dr03EcalRecHitSumEt',
                        'dr03HcalTowerSumEt:dr03HcalTowerSumEt',
                        'dr03HcalDepth1TowerSumEt:dr03HcalDepth1TowerSumEt',
                        'dr03HcalDepth2TowerSumEt:dr03HcalDepth2TowerSumEt',
                        'dr03TkSumPt:dr03TkSumPt',
                        'dr04EcalRecHitSumEt:dr03EcalRecHitSumEt',
                        'dr04HcalTowerSumEt:dr03HcalTowerSumEt',
                        'dr04HcalDepth1TowerSumEt:dr04HcalDepth1TowerSumEt',
                        'dr04HcalDepth2TowerSumEt:dr04HcalDepth2TowerSumEt',
                        'dr04TkSumPt:dr04TkSumPt',
                        'cpx:trackMomentumAtCalo.x',
                        'cpy:trackMomentumAtCalo.y',
                        'cpz:trackMomentumAtCalo.z',
                        'vpx:trackMomentumAtVtx.x',
                        'vpy:trackMomentumAtVtx.y',
                        'vpz:trackMomentumAtVtx.z',
                        'cx:TrackPositionAtCalo.x',
                        'cy:TrackPositionAtCalo.y',
                        'cz:TrackPositionAtCalo.z'#,
                        #'IDRobust:electronIDRobust'
									)
                ),
                Class = cms.string('pat::Electron')
            ),


            tracks = cms.PSet(
                src = cms.InputTag("generalTracks"),
                leaves = cms.PSet(
                    vars = cms.vstring('chi2:chi2', 
                        'trkExptHitsInner:trackerExpectedHitsInner.numberOfHits',
                        'trkExptHitsOuter:trackerExpectedHitsOuter.numberOfHits',
                        'trks_nlayerslost:hitPattern.trackerLayersWithoutMeasurement',
                        'trks_nlayers:hitPattern.trackerLayersWithMeasurement',
                        'trksvalidpixelhits:hitPattern.numberOfValidPixelHits',
                        'trkslostpixelhits:hitPattern.numberOfLostPixelHits',
                        'ndof:ndof', 
                        'chg:charge', 
                        'pt:pt', 
                        'px:px', 
                        'py:py', 
                        'pz:pz', 
                        'eta:eta', 
                        'phi:phi', 
                        'theta:theta', 
                        'd0dum:d0', 
                        'dz:dz', 
                        'vx:vx', 
                        'vy:vy', 
                        'vz:vz',
												'validFraction:validFraction', 
                        'numvalhits:numberOfValidHits', 
                        'numlosthits:numberOfLostHits', 
                        'd0dumErr:d0Error', 
                        'dzErr:dzError',
                        'ptErr:ptError', 
                        'etaErr:etaError', 
                        'phiErr:phiError', 
                        'Nrechits:recHitsSize', 
                        'innerHitX:innerPosition.x', 
                        'innerHitY:innerPosition.y', 
                        'innerHitZ:innerPosition.z', 
                        'outerHitX:outerPosition.x', 
                        'outerHitY:outerPosition.y', 
                        'outerHitZ:outerPosition.z',												
												'outerPx:outerPx',
												'outerPy:outerPy',
												'outerPz:outerPz',
												'algo:algo',
                        'highPurity:quality("highPurity")'
                                       )
                ),
                selection = cms.string('pt>0.7'),
                Class = cms.string('reco::Track')
            ),

            taus = cms.PSet(
               #               src = cms.InputTag("cleanPatTaus"),
               #              src = cms.InputTag("selectedPatTaus"),
                              src = cms.InputTag("selectedPatTausPF"),
            		      leaves = cms.PSet(
            		          basicKinematicLeaves,
            		          vars = cms.vstring(
            		          #					    'isInEcalCrack:isInEcalCrack',
            		          'charge:charge',
            		          'emf:emFraction',
            		          'hcalTotOverPLead:hcalTotOverPLead',
            		          'hcalMaxOverPLead:hcalMaxOverPLead',
            		          'hcal3x3OverPLead:hcal3x3OverPLead',
            		          'ecalStripSumEOverPLead:ecalStripSumEOverPLead',
            		          'elecPreIdOutput:electronPreIDOutput',
            		          'elecPreIdDecision:electronPreIDDecision',
            		          'leadPFChargedHadrCand_pt:leadPFChargedHadrCand.pt',
            		          'leadPFChargedHadrCand_charge:leadPFChargedHadrCand.charge',
            		          'leadPFChargedHadrCand_eta:leadPFChargedHadrCand.eta',
            		          'leadPFChargedHadrCand_ECAL_eta:leadPFChargedHadrCand.positionAtECALEntrance.eta',
            		          'leadPFChargedHadrCand_phi:leadPFChargedHadrCand.phi',
            		          'isoPFGammaCandsEtSum:isolationPFGammaCandsEtSum',
            		          'isoPFChargedHadrCandsPtSum:isolationPFChargedHadrCandsPtSum',
            		          'leadingTrackFinding:tauID("leadingTrackFinding")',
            		          'leadingTrackPtCut:tauID("leadingTrackPtCut")',
            		          'trackIsolation:tauID("trackIsolation")',
            		          'ecalIsolation:tauID("ecalIsolation")',
            		          'byIsolation:tauID("byIsolation")', 
            		          'againstElectron:tauID("againstElectron")',
            		          'againstMuon:tauID("againstMuon")',
            		          'taNC_quarter:tauID("byTaNCfrQuarterPercent")',
            		          'taNC_one:tauID("byTaNCfrOnePercent")',
            		          'taNC_half:tauID("byTaNCfrHalfPercent")',
            		          'taNC_tenth:tauID("byTaNCfrTenthPercent")',
            		          'taNC:tauID("byTaNC")',
            		          'byIsoUsingLeadingPi:tauID("byIsolationUsingLeadingPion")',
            		          'tkIsoUsingLeadingPi:tauID("trackIsolationUsingLeadingPion")',
            		          'ecalIsoUsingLeadingPi:tauID("ecalIsolationUsingLeadingPion")',
            		          'signalPFChargedHadrCandsSize:signalPFChargedHadrCands.size',
            		          'muDecision:muonDecision',
            		          'Nprongs:signalTracks.size'
            		          )
            		          ),
            		      Class = cms.string('pat::Tau')
            		      ),

            els = cms.PSet(
                src = cms.string('electrons'),
                leaves = cms.PSet(
                    basicKinematicLeaves,
                    vars = cms.vstring(#'id:leptonID', 
                        'gen_id:genLepton.pdgId',
                        'gen_phi:genLepton.phi',
                        'gen_pt:genLepton.pt',
                        'gen_pz:genLepton.pz',
                        'gen_px:genLepton.px',
                        'gen_py:genLepton.py',
                        'gen_eta:genLepton.eta',
                        'gen_theta:genLepton.theta',
                        'gen_et:genLepton.et',                       
                        'gen_mother_id:genLepton.mother.pdgId',
                        'gen_mother_phi:genLepton.mother.phi',
                        'gen_mother_pt:genLepton.mother.pt',
                        'gen_mother_pz:genLepton.mother.pz',
                        'gen_mother_px:genLepton.mother.px',
                        'gen_mother_py:genLepton.mother.py',
                        'gen_mother_eta:genLepton.mother.eta',
                        'gen_mother_theta:genLepton.mother.theta',
                        'gen_mother_et:genLepton.mother.et',                       
                        'tightId:electronID("eidTight")',
                        'looseId:electronID("eidLoose")',
                        'robustTightId:electronID("eidRobustTight")',
                        'robustLooseId:electronID("eidRobustLoose")',
                        'robustHighEnergyId:electronID("eidRobustHighEnergy")',
												'simpleEleId95relIso:electronID("simpleEleId95relIso")',
                        'simpleEleId90relIso:electronID("simpleEleId90relIso")',
                        'simpleEleId85relIso:electronID("simpleEleId85relIso")',
                        'simpleEleId80relIso:electronID("simpleEleId80relIso")',
                        'simpleEleId70relIso:electronID("simpleEleId70relIso")',
                        'simpleEleId60relIso:electronID("simpleEleId60relIso")',
                        'simpleEleId95cIso:electronID("simpleEleId95cIso")',
                        'simpleEleId90cIso:electronID("simpleEleId90cIso")',
                        'simpleEleId85cIso:electronID("simpleEleId85cIso")',
                        'simpleEleId80cIso:electronID("simpleEleId80cIso")',
                        'simpleEleId70cIso:electronID("simpleEleId70cIso")',
                        'simpleEleId60cIso:electronID("simpleEleId60cIso")',
                        'cIso:caloIso', 
                        'tIso:trackIso', 
                        'ecalIso:ecalIso',
                        'hcalIso:hcalIso',
                        'chi2:gsfTrack.chi2', 
#                        'class:classification', 
                        'charge:charge', 
                        'caloEnergy:caloEnergy', 
                        'hadOverEm:hadronicOverEm', 
                        'eOverPIn:eSuperClusterOverP', 
                        'eSeedOverPOut:eSeedClusterOverPout', 
                        'sigmaEtaEta:scSigmaEtaEta',
                        'sigmaIEtaIEta:scSigmaIEtaIEta',
                        'scEnergy:superCluster.energy',
                        'scRawEnergy:superCluster.rawEnergy',
                        'scSeedEnergy:superCluster.seed.energy',
                        'scEta:superCluster.position.eta',
                        'scPhi:superCluster.position.phi',
                        'scEtaWidth:superCluster.etaWidth',
                        'scPhiWidth:superCluster.phiWidth',
                        'scE1x5:scE1x5',
                        'scE2x5Max:scE2x5Max',
                        'scE5x5:scE5x5',
                        'isEB:isEB',
                        'isEE:isEE',
                        'dEtaIn:deltaEtaSuperClusterTrackAtVtx', 
                        'dPhiIn:deltaPhiSuperClusterTrackAtVtx', 
                        'dEtaOut:deltaEtaSeedClusterTrackAtCalo', 
                        'dPhiOut:deltaPhiSeedClusterTrackAtCalo', 
                        'numvalhits:gsfTrack.numberOfValidHits', 
                        'numlosthits:gsfTrack.numberOfLostHits', 
                        #'numCluster:numberOfClusters', 
                        'basicClustersSize:basicClustersSize',
                        'tk_pz:gsfTrack.pz',
                        'tk_pt:gsfTrack.pt', 
                        'tk_phi:gsfTrack.phi', 
                        'tk_eta:gsfTrack.eta', 
                        'd0dum:gsfTrack.d0', 
                        'dz:gsfTrack.dz', 
                        'vx:gsfTrack.vx', 
                        'vy:gsfTrack.vy', 
                        'vz:gsfTrack.vz', 
                        'ndof:gsfTrack.ndof', 
                        'ptError:gsfTrack.ptError', 
                        'd0dumError:gsfTrack.d0Error', 
                        'dzError:gsfTrack.dzError', 
                        'etaError:gsfTrack.etaError', 
                        'phiError:gsfTrack.phiError', 
                        'tk_charge:gsfTrack.charge',
												'core_ecalDrivenSeed:core.ecalDrivenSeed',
                        'n_inner_layer:gsfTrack.trackerExpectedHitsInner.numberOfHits',
                        'n_outer_layer:gsfTrack.trackerExpectedHitsOuter.numberOfHits',
                        'ctf_tk_id:closestCtfTrackRef.key',
                        'ctf_tk_charge:closestCtfTrackRef.charge',
                        'ctf_tk_eta:closestCtfTrackRef.eta',
                        'ctf_tk_phi:closestCtfTrackRef.phi',
                        'fbrem:fbrem',
                        'shFracInnerHits:shFracInnerHits',                        
                        'dr03EcalRecHitSumEt:dr03EcalRecHitSumEt',
                        'dr03HcalTowerSumEt:dr03HcalTowerSumEt',
                        'dr03HcalDepth1TowerSumEt:dr03HcalDepth1TowerSumEt',
                        'dr03HcalDepth2TowerSumEt:dr03HcalDepth2TowerSumEt',
                        'dr03TkSumPt:dr03TkSumPt',
                        'dr04EcalRecHitSumEt:dr03EcalRecHitSumEt',
                        'dr04HcalTowerSumEt:dr03HcalTowerSumEt',
                        'dr04HcalDepth1TowerSumEt:dr04HcalDepth1TowerSumEt',
                        'dr04HcalDepth2TowerSumEt:dr04HcalDepth2TowerSumEt',
                        'dr04TkSumPt:dr04TkSumPt',
                        'cpx:trackMomentumAtCalo.x', 
                        'cpy:trackMomentumAtCalo.y', 
                        'cpz:trackMomentumAtCalo.z', 
                        'vpx:trackMomentumAtVtx.x', 
                        'vpy:trackMomentumAtVtx.y', 
                        'vpz:trackMomentumAtVtx.z', 
                        'cx:TrackPositionAtCalo.x', 
                        'cy:TrackPositionAtCalo.y', 
                        'cz:TrackPositionAtCalo.z'#, 
                        #'IDRobust:electronIDRobust'
                        )
                ),
                Class = cms.string('pat::Electron')
            ),


				jets_AK5PF = cms.PSet(
					src = cms.InputTag("selectedPatJetsPF"),
					leaves = cms.PSet(
						basicKinematicLeaves,
						vars = cms.vstring('parton_Id:genParton.pdgId',
							'parton_motherId:genParton.mother.pdgId',
							'parton_pt:genParton.pt',
							'parton_phi:genParton.phi',
							'parton_eta:genParton.eta',
							'parton_Energy:genParton.energy',
							'parton_mass:genParton.mass',
							#'parton_motherID:genParton.mother.pdgId',
							#'parton_grandmotherID:genParton.mother.mother.pdgId',
							'gen_et:genJet.et',
							'gen_pt:genJet.pt',
							'gen_eta:genJet.eta',
							'gen_phi:genJet.phi',
							'gen_mass:genJet.mass',
							'gen_Energy:genJet.energy',
							'gen_Id:genJet.pdgId',
							'gen_motherID:genJet.mother.pdgId',
							'gen_threeCharge:genJet.threeCharge',
							'partonFlavour:partonFlavour',  #TL add
							'btag_TC_highPur:bDiscriminator("trackCountingHighPurBJetTags")', # TL add: b-tagging info (9lines)
							'btag_TC_highEff:bDiscriminator("trackCountingHighEffBJetTags")',
							'btag_jetProb:bDiscriminator("jetProbabilityBJetTags")',
							'btag_jetBProb:bDiscriminator("jetBProbabilityBJetTags")',
							'btag_softEle:bDiscriminator("softElectronByPtBJetTags")',
							'btag_softMuon:bDiscriminator("softMuonBJetTags")',
							'btag_secVertexHighPur:bDiscriminator("simpleSecondaryVertexHighPurBJetTags")',
							'btag_secVertexHighEff:bDiscriminator("simpleSecondaryVertexHighEffBJetTags")',
							'btag_secVertexCombined:bDiscriminator("combinedSecondaryVertexBJetTags")',
							'jetCharge:jetCharge',
							'chgEmE:chargedEmEnergy',
							'chgHadE:chargedHadronEnergy',
							'chgMuE:chargedMuEnergy',
							'chg_Mult:chargedMultiplicity',
							'neutralEmE:neutralEmEnergy',
							'neutralHadE:neutralHadronEnergy',
							'neutral_Mult:neutralMultiplicity',
							'mu_Mult:muonMultiplicity',
							'emf:emEnergyFraction',
							'ehf:energyFractionHadronic',
							'n60:n60',
							'n90:n90',
							'etaetaMoment:etaetaMoment',
							'etaphiMoment:etaphiMoment',
							'phiphiMoment:phiphiMoment',
							'n90Hits:jetID.n90Hits',
							'fHPD:jetID.fHPD',
							'fRBX:jetID.fRBX',
							'hitsInN90:jetID.hitsInN90',
							'nECALTowers:jetID.nECALTowers',
							'nHCALTowers:jetID.nHCALTowers',
							'fSubDetector1:jetID.fSubDetector1',
							'fSubDetector2:jetID.fSubDetector2',
							'fSubDetector3:jetID.fSubDetector3',
							'fSubDetector4:jetID.fSubDetector4',
							'area:towersArea',
							'corrFactorRaw:jecFactor(0)',
							'mass:mass'
						)
					),
					Class = cms.string('pat::Jet')
				),

        jets_AK5PFclean = cms.PSet(
        	src = cms.InputTag("cleanPatJetsAK5PF"),
        	leaves = cms.PSet(
        		basicKinematicLeaves,
        		vars = cms.vstring('parton_Id:genParton.pdgId',
        			'parton_motherId:genParton.mother.pdgId',
        			'parton_pt:genParton.pt',
        			'parton_phi:genParton.phi',
        			'parton_eta:genParton.eta',
        			'parton_Energy:genParton.energy',
        			'parton_mass:genParton.mass',
        			#'parton_motherID:genParton.mother.pdgId',
        			#'parton_grandmotherID:genParton.mother.mother.pdgId',
        			'gen_et:genJet.et',
        			'gen_pt:genJet.pt',
        			'gen_eta:genJet.eta',
        			'gen_phi:genJet.phi',
        			'gen_mass:genJet.mass',
        			'gen_Energy:genJet.energy',
        			'gen_Id:genJet.pdgId',
#       			 'gen_motherID:genJet.mother.pdgId',
#       			 'gen_threeCharge:genJet.threeCharge',
        			'partonFlavour:partonFlavour',  #TL add
        			'btag_TC_highPur:bDiscriminator("trackCountingHighPurBJetTags")', # TL add: b-tagging info (9lines)
        			'btag_TC_highEff:bDiscriminator("trackCountingHighEffBJetTags")',
        			'btag_jetProb:bDiscriminator("jetProbabilityBJetTags")',
        			'btag_jetBProb:bDiscriminator("jetBProbabilityBJetTags")',
        			'btag_softEle:bDiscriminator("softElectronByPtBJetTags")',
        			'btag_softMuon:bDiscriminator("softMuonBJetTags")',
        			'btag_secVertexHighPur:bDiscriminator("simpleSecondaryVertexHighPurBJetTags")',
        			'btag_secVertexHighEff:bDiscriminator("simpleSecondaryVertexHighEffBJetTags")',
        			'btag_secVertexCombined:bDiscriminator("combinedSecondaryVertexBJetTags")',
        			'jetCharge:jetCharge',
        			'chgEmE:chargedEmEnergy',
        			'chgHadE:chargedHadronEnergy',
        			'chgMuE:chargedMuEnergy',
        			'chg_Mult:chargedMultiplicity',
        			'neutralEmE:neutralEmEnergy',
        			'neutralHadE:neutralHadronEnergy',
        			'neutral_Mult:neutralMultiplicity',
        			'mu_Mult:muonMultiplicity',
        			'emf:emEnergyFraction',
        			'ehf:energyFractionHadronic',
        			'n60:n60',
        			'n90:n90',
        			'etaetaMoment:etaetaMoment',
        			'etaphiMoment:etaphiMoment',
        			'phiphiMoment:phiphiMoment',
        			'n90Hits:jetID.n90Hits',
        			'fHPD:jetID.fHPD',
        			'fRBX:jetID.fRBX',
        			'hitsInN90:jetID.hitsInN90',
        			'nECALTowers:jetID.nECALTowers',
        			'nHCALTowers:jetID.nHCALTowers',
        			'fSubDetector1:jetID.fSubDetector1',
        			'fSubDetector2:jetID.fSubDetector2',
        			'fSubDetector3:jetID.fSubDetector3',
        			'fSubDetector4:jetID.fSubDetector4',
        			'area:towersArea',
        			#'corrFactorRaw:corrFactor("raw")',
        			'corrFactorRaw:jecFactor(0)',
        			'mass:mass'
        		)
        	),
        	Class = cms.string('pat::Jet')
        ),
			),
			ComponentName = cms.string('CompleteNTupler'),
			useTFileService = cms.bool(True), ## false for EDM; true for non EDM
			
                        AdHocNPSet = cms.PSet(
                          treeName = cms.string('eventA')
                        ) # ,

#                        variablesPSet = cms.PSet(
#			  #use all the variables from the PSet above
#			  allVariables = cms.bool(True),
#			  treeName = cms.string('eventV')
#		        )
	)
)




