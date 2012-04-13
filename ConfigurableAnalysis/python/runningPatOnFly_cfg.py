#
#  SUSY-PAT configuration file
#
#  PAT configuration for the SUSY group - 52X series
#  More information here:
#  https://twiki.cern.ch/twiki/bin/view/CMS/SusyPatLayer1DefV12
#

#swith between MC and data
isMC = False
#isMC = True


import FWCore.ParameterSet.Config as cms

process = cms.Process("PAT")

#-- Message Logger ------------------------------------------------------------
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.categories.append('PATSummaryTables')
process.MessageLogger.cerr.PATSummaryTables = cms.untracked.PSet(
    limit = cms.untracked.int32(-1),
    reportEvery = cms.untracked.int32(100)
)

#-- Source information ------------------------------------------------------
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
			'file:/LVM/SATA/pbgeff/temp_52X_ntuple/MuHad_Run2012A-PromptReco-v1_AOD_709B4CB9-BF82-E111-BD9B-003048F1182E.root',
                        #'file:/LVM/SATA/pbgeff/temp_52X_ntuple/TTJets_TuneZ2star_8TeV-madgraph-tauola_PU_S7_START52_V5-v1_AODSIM_FEC0CBA1-5A81-E111-8D3A-0018F3D0968E.root',
    )
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(
#  '166512:551-166512:551',
#)
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

## Standard PAT Configuration File
process.load("PhysicsTools.PatAlgos.patSequences_cff")
process.BFieldColl = cms.EDProducer('BFieldProducer')
process.JetCorrColl = cms.EDProducer('JetCorrProducer')

#Need this for L1 triggers with CMSSW >= 381
process.load("PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff")
process.patTrigger.addL1Algos = cms.bool( True )

## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
     #verbose = cms.untracked.bool(True),
     fileName = cms.untracked.string('patTuple.root'),
     SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
     outputCommands = cms.untracked.vstring('drop *', "keep *_BFieldColl_*_*_","keep *_JetCorrColl_*_*_", *patEventContent 
		 )
)

#-- SUSYPAT and GlobalTag Settings -----------------------------------------------------------
from PhysicsTools.Configuration.SUSY_pattuple_cff import addDefaultSUSYPAT, getSUSY_pattuple_outputCommands

if isMC:
	process.GlobalTag.globaltag = 'START52_V9::All' # MC Setting
	addDefaultSUSYPAT(process,True,'HLT',['L1FastJet','L2Relative','L3Absolute'],'',['AK5PF'])
else:
	process.GlobalTag.globaltag = 'GR_R_52_V7::All'   # Data Setting
	addDefaultSUSYPAT(process,False,'HLT',['L1FastJet','L2Relative','L3Absolute','L2L3Residual'],'',['AK5PF'])
	#process.metJESCorAK5PFTypeI.corrector = cms.string('ak5PFL2L3Residual') # Type1PFMET Residual for data only.

process.pfNoTauPF.enable = cms.bool(False)
SUSY_pattuple_outputCommands = getSUSY_pattuple_outputCommands( process )
############################## END SUSYPAT specifics ####################################


################### Add Type-I PFMET (for default RECO-PF jets) ########################
process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")

# NOTE: use "ak5PFL1FastL2L3" for MC / "ak5PFL1FastL2L3Residual" for Data
if isMC:
	process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3"
else:
	process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3Residual"

process.patPFMETs = process.patMETs.clone(
    metSource = cms.InputTag('pfMet'),
    addMuonCorrections = cms.bool(False),
    #genMETSource = cms.InputTag('genMetTrue'),
    #addGenMET = cms.bool(True)
    )
process.patPFMETsTypeIcorrected = process.patPFMETs.clone(
    metSource = cms.InputTag('pfType1CorrectedMet')
    )
process.patPFMETsTypeIpIIcorrected = process.patPFMETs.clone(
    metSource = cms.InputTag('pfType1p2CorrectedMet')
    )


##now for PF2PAT-no-tau-cleaning jets (postfix=PFLOW)
#process.pfCandsNotInJetPFLOW = process.pfCandsNotInJet.clone(
#    topCollection = cms.InputTag('pfJetsPFLOW')
#   )
#process.pfType2CandsPFLOW = process.pfType2Cands.clone(
#    src = cms.InputTag('pfCandsNotInJetPFLOW'),
#    )
#process.pfJetMETcorrPFLOW = process.pfJetMETcorr.clone(
#    src = cms.InputTag('pfJetsPFLOW'),
#    )
#process.pfCandMETcorrPFLOW = process.pfCandMETcorr.clone(
#    src = cms.InputTag('pfCandsNotInJetPFLOW')
#    )
#process.pfType1CorrectedMetPFLOW = process.pfType1CorrectedMet.clone(
#    src = cms.InputTag('pfMETPFLOW'),
#    srcType1Corrections = cms.VInputTag(
#        cms.InputTag('pfJetMETcorrPFLOW', 'type1')
#        ),
#    )
#process.pfType1p2CorrectedMetPFLOW = process.pfType1p2CorrectedMet.clone(
#    src = cms.InputTag('pfMETPFLOW'),
#    srcType1Corrections = cms.VInputTag(
#        cms.InputTag('pfJetMETcorrPFLOW', 'type1')
#        ),
#    srcUnclEnergySums = cms.VInputTag(
#        cms.InputTag('pfJetMETcorrPFLOW', 'type2'),
#        cms.InputTag('pfCandMETcorrPFLOW')
#        ),          
#    )
#process.producePFMETCorrectionsPFLOW = cms.Sequence(
#    process.pfCandsNotInJetPFLOW
#    * process.pfType2CandsPFLOW
#    * process.pfJetMETcorrPFLOW
#    * process.pfCandMETcorrPFLOW
#    * process.pfType1CorrectedMetPFLOW
#    * process.pfType1p2CorrectedMetPFLOW
#    )
#process.patPFMETsPFLOW = process.patPFMETs.clone(
#    metSource = cms.InputTag('pfMETPFLOW'),
#    )
#process.patPFMETsTypeIcorrectedPFLOW = process.patPFMETsPFLOW.clone(
#    metSource = cms.InputTag('pfType1CorrectedMetPFLOW')
#    )
#process.patPFMETsTypeIpIIcorrectedPFLOW = process.patPFMETsPFLOW.clone(
#    metSource = cms.InputTag('pfType1p2CorrectedMetPFLOW')
#    )



#Turn on trigger info
from PhysicsTools.PatAlgos.tools.trigTools import switchOnTrigger
switchOnTrigger(process, triggerProducer='patTrigger', triggerEventProducer='patTriggerEvent', sequence='patDefaultSequence', hltProcess="HLT")

process.load("Workspace.ConfigurableAnalysis.configurableAnalysis_ForPattuple_cff")
process.load('CommonTools/RecoAlgos/HBHENoiseFilterResultProducer_cfi')
process.load('RecoMET.METAnalyzers.CSCHaloFilter_cfi')
process.load('RecoMET.METFilters.trackingFailureFilter_cfi')
process.load('RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi')
process.load('RecoMET.METFilters.inconsistentMuonPFCandidateFilter_cfi')
process.load('RecoMET.METFilters.greedyMuonPFCandidateFilter_cfi')
#process.load('Sandbox.Skims.eeNoiseFilter_cfi')

process.scrapingVeto = cms.EDFilter("FilterOutScraping",
                                     applyfilter = cms.untracked.bool(True),
                                     debugOn = cms.untracked.bool(False),
                                     numtrack = cms.untracked.uint32(10),
                                     thresh = cms.untracked.double(0.2)
)

# The section below is for the filter on Boundary Energy. Available in AOD in CMSSW>44x
process.load('RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi')
process.EcalDeadCellBoundaryEnergyFilter.taggingMode = cms.bool(False)
process.EcalDeadCellBoundaryEnergyFilter.cutBoundEnergyDeadCellsEB=cms.untracked.double(10)
process.EcalDeadCellBoundaryEnergyFilter.cutBoundEnergyDeadCellsEE=cms.untracked.double(10)
process.EcalDeadCellBoundaryEnergyFilter.cutBoundEnergyGapEB=cms.untracked.double(100)
process.EcalDeadCellBoundaryEnergyFilter.cutBoundEnergyGapEE=cms.untracked.double(100)
process.EcalDeadCellBoundaryEnergyFilter.enableGap=cms.untracked.bool(False)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEB = cms.vint32(12,14)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEE = cms.vint32(12,14)
# End of Boundary Energy filter configuration 


#-- Output module configuration -----------------------------------------------
process.out.fileName = "SUSYPAT.root" 
process.out.splitLevel = cms.untracked.int32(99)  # Turn on split level (smaller files???)
process.out.overrideInputFileSplitLevels = cms.untracked.bool(True)
process.out.dropMetaData = cms.untracked.string('DROPPED')   # Get rid of metadata related to dropped collections
#process.out.outputCommands = cms.untracked.vstring('drop *',"keep *_HBHENoiseFilterResultProducer_*_*","keep *_BFieldColl_*_*","keep *_JetCorrectionColl_*_*", *SUSY_pattuple_outputCommands )
process.out.outputCommands = cms.untracked.vstring('keep *',"keep *_HBHENoiseFilterResultProducer_*_*","keep *_BFieldColl_*_*","keep *_JetCorrectionColl_*_*", *SUSY_pattuple_outputCommands )
process.out.outputCommands.append('keep *_patPFMETsTypeIcorrected_*_PAT')
#process.out.outputCommands.append('keep *_selectedPatJetsPFLOW_*_PAT')
#process.out.outputCommands.append('keep *_selectedPatElectronsPFLOW_*_PAT')
#process.out.outputCommands.append('keep *_selectedPatMuonsPFLOW_*_PAT')
#process.out.outputCommands.append('keep *_patPFMETsTypeIcorrectedPFLOW_*_PAT')
#process.out.outputCommands.append('keep *_patPFMETsTypeIpIIcorrectedPFLOW_*_PAT')

#-- Execution path ------------------------------------------------------------
# Full path
#This is to run on full sim or data
process.ecaltpfilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
#Run both TP and BE filters; doesn't work right now
#process.ecaltpfilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter*process.EcalDeadCellBoundaryEnergyFilter)
process.csctighthalofilter = cms.Path(process.CSCTightHaloFilter)
process.scrapingveto = cms.Path(process.scrapingVeto)
process.greedymuonfilter = cms.Path(process.greedyMuonPFCandidateFilter)
process.inconsistentPFmuonfilter = cms.Path(process.inconsistentMuonPFCandidateFilter)
#process.eenoisefilter = cms.Path(process.eeNoiseFilter)
process.p = cms.Path(process.HBHENoiseFilterResultProducer + process.BFieldColl + process.susyPatDefaultSequence + process.JetCorrColl)
#process.p += process.patPF2PATSequencePFLOW
process.p += process.producePFMETCorrections
process.p += process.patPFMETsTypeIcorrected
#process.p += process.producePFMETCorrectionsPFLOW
#process.p += process.patPFMETsTypeIcorrectedPFLOW

#process.trackingfailturefilter = cms.Path(process.goodVerticesRA4*process.trackingFailureFilter)
process.trackingfailturefilter = cms.Path(process.trackingFailureFilter)
process.outpath = cms.EndPath(cms.ignore(process.configurableAnalysis))
#process.outpath = cms.EndPath(process.out)

#-- Dump config ------------------------------------------------------------
file = open('SusyPAT_cfg.py','w')
file.write(str(process.dumpPython()))
file.close()
