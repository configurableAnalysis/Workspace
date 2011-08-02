import FWCore.ParameterSet.Config as cms

from configurableAnalysis_ForPattuple_cfi import *

InputTagDistributorService = cms.Service("InputTagDistributorService")

VariableHelperService = cms.Service("VariableHelperService")

UpdaterService = cms.Service("UpdaterService")

TFileService = cms.Service("TFileService",
    fileName = cms.string('configurableAnalysis.root')
)



