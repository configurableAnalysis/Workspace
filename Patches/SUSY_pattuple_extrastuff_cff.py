import FWCore.ParameterSet.Config as cms

def addPF2PATNoTauJets(process,mcInfo=True,jetCorrections=['L2Relative', 'L3Absolute']):
    ##Add the PF2PAT-no-tau-cleaning jet collection : postfix = PFLOW
    ##-- PAT standard config -------------------------------------------------------
    #process.load("PhysicsTools.PatAlgos.patSequences_cff")
    ##-- Jet corrections -----------------------------------------------------------
    #process.patJetCorrFactors.levels = options.jetCorrections 
    from PhysicsTools.PatAlgos.tools.pfTools import usePF2PAT
    #-- PF2PAT config -------------------------------------------------------------
    usePF2PAT(process,runPF2PAT=True, jetAlgo='AK5',runOnMC=(mcInfo==1),postfix="PFLOW", jetCorrections=('AK5PFchs', jetCorrections))
    from PhysicsTools.PatAlgos.tools.pfTools import switchToPFJets
    switchToPFJets( process, cms.InputTag('pfJets'+'PFLOW'), 'AK5', postfix='PFLOW', jetCorrections=('AK5PFchs', jetCorrections) )
    process.patJetsPFLOW.addTagInfos = cms.bool(True)
    process.patJetsPFLOW.tagInfoSources = cms.VInputTag("secondaryVertexTagInfosAODPFLOW") 
    if ("L1FastJet" in jetCorrections):
        process.pfJetsPFLOW.doAreaFastjet = True                           
    #from JetMETCorrections.Type1MET.MetType1Corrections_cff import metJESCorAK5PFJet 
    #process.metJESCorAK5PFLOWTypeI = metJESCorAK5PFJet.clone( 
    #    inputUncorJetsLabel = "patJetsPFLOW", 
    #    metType = "pat",                  
    #    inputUncorMetLabel = "pfMet",
    #    )
    #process.patMETsTypeIPFLOW = process.patMETsPFLOW.clone(
    #    metSource = cms.InputTag("metJESCorAK5PFLOWTypeI")
    #    )
    ## Add to producersLayer1 sequence
    ##process.patDefaultSequencePFLOW.replace(
    #process.patPF2PATSequencePFLOW.replace(
    #    process.patMETsPFLOW,
    #    process.patMETsPFLOW+
    #    process.metJESCorAK5PFLOWTypeI+
    #    process.patMETsTypeIPFLOW
    #    )
    #Set isolation cone to 0.3
    process.isoValElectronWithChargedPFLOW.deposits[0].deltaR = 0.3
    process.isoValElectronWithNeutralPFLOW.deposits[0].deltaR = 0.3
    process.isoValElectronWithPhotonsPFLOW.deposits[0].deltaR = 0.3
    process.isoValMuonWithChargedPFLOW.deposits[0].deltaR = 0.3
    process.isoValMuonWithNeutralPFLOW.deposits[0].deltaR = 0.3
    process.isoValMuonWithPhotonsPFLOW.deposits[0].deltaR = 0.3

    #-- Enable pileup sequence -------------------------------------------------------------
    #Vertices
    process.goodVerticesPFLOW = cms.EDFilter("VertexSelector",
                                             src = cms.InputTag("offlinePrimaryVertices"),
                                             cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
                                             filter = cms.bool(False),
                                             )
    process.pfPileUpPFLOW.Vertices = "goodVerticesPFLOW"
    process.pfPileUpPFLOW.Enable = True
    
    process.pfNoPileUpSequencePFLOW.replace(process.pfPileUpPFLOW,
                                            process.goodVerticesPFLOW + process.pfPileUpPFLOW)



