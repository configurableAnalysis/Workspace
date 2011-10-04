#
#  SUSY-PAT configuration file
#
#  PAT configuration for the SUSY group - 42X series
#  More information here:
#  https://twiki.cern.ch/twiki/bin/view/CMS/SusyPatLayer1DefV10
#

# Starting with a skeleton process which gets imported with the following line
#from PhysicsTools.PatAlgos.patTemplate_cfg import *

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
			'file:/LVM/SATA/wto/RECO/Run166512/MuHad/FA3D4FB8-BA91-E011-97AB-003048673374.root',
    )
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
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

#process.GlobalTag.globaltag = 'START42_V13::All' # MC Setting
#addDefaultSUSYPAT(process,True,'HLT',['L1FastJet','L2Relative','L3Absolute'],'',['AK5PF','AK5JPT'])

process.GlobalTag.globaltag = 'GR_R_42_V19::All'   # Data Setting
addDefaultSUSYPAT(process,False,'HLT',['L1FastJet','L2Relative','L3Absolute','L2L3Residual'],'',['AK5PF','AK5JPT'])
process.metJESCorAK5PFTypeI.corrector = cms.string('ak5PFL2L3Residual') # Type1PFMET Residual for data only.

process.pfNoTauPF.enable = cms.bool(False)
SUSY_pattuple_outputCommands = getSUSY_pattuple_outputCommands( process )
############################## END SUSYPAT specifics ####################################

#Turn on trigger info
from PhysicsTools.PatAlgos.tools.trigTools import switchOnTrigger
switchOnTrigger(process, triggerProducer='patTrigger', triggerEventProducer='patTriggerEvent', sequence='patDefaultSequence', hltProcess="HLT")

process.load("Workspace.ConfigurableAnalysis.configurableAnalysis_ForPattuple_cff")
process.load('CommonTools/RecoAlgos/HBHENoiseFilterResultProducer_cfi')
process.load('RecoMET.METAnalyzers.CSCHaloFilter_cfi')
process.load('Sandbox.Skims.trackingFailureFilter_cfi')
process.load('JetMETAnalysis.ecalDeadCellTools.RA2TPfilter_cff')

process.scrapingVeto = cms.EDFilter("FilterOutScraping",
                                     applyfilter = cms.untracked.bool(True),
                                     debugOn = cms.untracked.bool(False),
                                     numtrack = cms.untracked.uint32(10),
                                     thresh = cms.untracked.double(0.2)
)


#-- Output module configuration -----------------------------------------------
process.out.fileName = "SUSYPAT.root" 
process.out.splitLevel = cms.untracked.int32(99)  # Turn on split level (smaller files???)
process.out.overrideInputFileSplitLevels = cms.untracked.bool(True)
process.out.dropMetaData = cms.untracked.string('DROPPED')   # Get rid of metadata related to dropped collections
process.out.outputCommands = cms.untracked.vstring('drop *',"keep *_HBHENoiseFilterResultProducer_*_*","keep *_BFieldColl_*_*","keep *_JetCorrectionColl_*_*", *SUSY_pattuple_outputCommands )
#-- Execution path ------------------------------------------------------------
# Full path
#This is to run on full sim or data
process.ecaltpfilter= cms.Path(process.ecalDeadCellTPfilter)
process.csctighthalofilter = cms.Path(process.CSCTightHaloFilter)
process.scrapingveto = cms.Path(process.scrapingVeto)
process.p = cms.Path(process.HBHENoiseFilterResultProducer + process.BFieldColl + process.susyPatDefaultSequence + process.JetCorrColl)
process.trackingfailturefilter = cms.Path(process.goodVerticesRA4*process.trackingFailureFilter)
process.outpath = cms.EndPath(cms.ignore(process.configurableAnalysis))

#-- Dump config ------------------------------------------------------------
file = open('SusyPAT_cfg.py','w')
file.write(str(process.dumpPython()))
file.close()
