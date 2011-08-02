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

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")

## Options and Output Report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
      #'/store/relval/CMSSW_3_6_0/RelValTTbar/GEN-SIM-RECO/START36_V4-v1/0013/306F945C-9A49-DF11-85F8-0018F3D0965A.root'
    )
)

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = cms.string('START36_V4::All')
from Configuration.PyReleaseValidation.autoCond import autoCond
#process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )
#print autoCond[ 'startup' ]
process.load("Configuration.StandardSequences.MagneticField_cff")

## Standard PAT Configuration File
process.load("PhysicsTools.PatAlgos.patSequences_cff")

process.BFieldColl = cms.EDProducer('BFieldProducer')

process.JetCorrColl = cms.EDProducer('JetCorrProducer')

#Need this for L1 triggers with CMSSW >= 381
process.load("PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff")
process.patTrigger.addL1Algos = cms.bool( True )
#process.patTrigger.addL1Algos = cms.bool( False )


## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
     verbose = cms.untracked.bool(True),
                               fileName = cms.untracked.string('patTuple.root'),
                               #fileName = cms.untracked.string('PATLayer1_Output.fromAOD_full.root'),
                               # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *', "keep *_BFieldColl_*_*_","keep *_JetCorrColl_*_*_",*patEventContent )
                               #outputCommands = cms.untracked.vstring('drop *', *patEventContent )
                               )
#process.outpath = cms.EndPath(process.out)



#-- Meta data to be logged in DBS ---------------------------------------------
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    name = cms.untracked.string('$Source: /cvs/CMSSW/UserCode/JRVlimant/cmssw/WorkSpace/ConfigurableAnalysis/python/runningPatOnFly_cfg.py,v $'),
    annotation = cms.untracked.string('SUSY pattuple definition')
)

#-- Message Logger ------------------------------------------------------------
process.MessageLogger.categories.append('PATSummaryTables')
process.MessageLogger.cerr.PATSummaryTables = cms.untracked.PSet(
    limit = cms.untracked.int32(-1),
    reportEvery = cms.untracked.int32(1)
    )
process.MessageLogger.cerr.FwkReport.reportEvery = 100


#-- Input Source --------------------------------------------------------------
process.source.fileNames = [
      'file:/LVM/SATA/pbgeff/temp_423_ntuple/DoubleMu_AOD_May10ReReco-v1_BEE13469-5E7C-E011-A3A6-00261894391B.root'
      #'file:/LVM/SATA/wto/RECO/Electron_Run2010B-Apr21ReReco-v1_AOD.root'
      #'file:/LVM/SATA/wto/RECO/RelValTTbar_Tauola_GEN-SIM-RECO_START42_V12_PU_E7TeV_FlatDist10_2011EarlyData_inTimeOnly-v1.root'
    ]

process.maxEvents.input = 1 
# Due to problem in production of LM samples: same event number appears multiple times
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

#-- Calibration tag -----------------------------------------------------------
process.GlobalTag.globaltag = 'GR_R_42_V12::All' 
#process.GlobalTag.globaltag = 'START42_V12::All'

############################# START SUSYPAT specifics ####################################
from PhysicsTools.Configuration.SUSY_pattuple_cff import addDefaultSUSYPAT, getSUSY_pattuple_outputCommands
#Apply SUSYPAT, parameters are: mcInfo, HLT menu, Jet energy corrections, mcVersion ('35x' for 35x samples, empty string for 36X samples),JetCollections
addDefaultSUSYPAT(process,False,'HLT',['L1FastJet','L2Relative','L3Absolute'],'',['AK5PF','AK5JPT'])
#addDefaultSUSYPAT(process,True,'HLT',['L1FastJet','L2Relative','L3Absolute'],'',['AK5PF','AK5JPT'])
SUSY_pattuple_outputCommands = getSUSY_pattuple_outputCommands( process )
############################## END SUSYPAT specifics ####################################


#Turn on trigger info
from PhysicsTools.PatAlgos.tools.trigTools import switchOnTrigger
switchOnTrigger(process, triggerProducer='patTrigger', triggerEventProducer='patTriggerEvent', sequence='patDefaultSequence', hltProcess="HLT")


process.load("Workspace.ConfigurableAnalysis.configurableAnalysis_ForPattuple_cff")

process.load('CommonTools/RecoAlgos/HBHENoiseFilterResultProducer_cfi')

#Only run this for data 
#Should be commented out if Residual corrections are not available
#process.metJESCorAK5PFTypeI.corrector = cms.string('ak5PFL2L3Residual')

#-- Output module configuration -----------------------------------------------
process.out.fileName = "SUSYPAT.root" 

# Custom settings
process.out.splitLevel = cms.untracked.int32(99)  # Turn on split level (smaller files???)
process.out.overrideInputFileSplitLevels = cms.untracked.bool(True)
process.out.dropMetaData = cms.untracked.string('DROPPED')   # Get rid of metadata related to dropped collections


#process.out.outputCommands = cms.untracked.vstring('drop *', *SUSY_pattuple_outputCommands )
process.out.outputCommands = cms.untracked.vstring('drop *',"keep *_HBHENoiseFilterResultProducer_*_*","keep *_BFieldColl_*_*","keep *_JetCorrectionColl_*_*", *SUSY_pattuple_outputCommands )


#-- Execution path ------------------------------------------------------------
# Full path
#This is to run on full sim or data
process.p = cms.Path(process.HBHENoiseFilterResultProducer + process.BFieldColl + process.susyPatDefaultSequence + process.JetCorrColl + process.configurableAnalysis)
#This is to run on FastSim
#process.p = cms.Path( process.BFieldColl + process.susyPatDefaultSequence + process.JetCorrColl +process.configurableAnalysis)


#-- Execution path ------------------------------------------------------------
# Full path
#process.p = cms.Path( process.susyPatDefaultSequence )
#-- Dump config ------------------------------------------------------------
file = open('SusyPAT_cfg.py','w')
file.write(str(process.dumpPython()))
file.close()
