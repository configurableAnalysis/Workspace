## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *
## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)
#process.Tracer = cms.Service("Tracer")

process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")
process.load("Workspace.ConfigurableAnalysis.configurableAnalysis_ForPattuple_cff")
process.load("PhysicsTools.PatAlgos.patSequences_cff")

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#   process.GlobalTag.globaltag =  ...    ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                         ##
#from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
#process.source.fileNames = filesRelValProdTTbarAODSIM
process.source.fileNames = ['/store/mc/Spring14dr/QCD_Pt-10to20_EMEnriched_Tune4C_13TeV_pythia8/AODSIM/castor_PU_S14_POSTLS170_V6-v1/00000/0022A01C-E4E8-E311-97DA-003048FFD75C.root' ]
#                                         ##
process.maxEvents.input = 1000
#                                         ##
#   process.out.outputCommands = [ ... ]  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                         ##
process.out.fileName = 'patTuple_standard.root'
#                                         ##
process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)
process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
process.outpath = cms.EndPath(cms.ignore(process.configurableAnalysis))
