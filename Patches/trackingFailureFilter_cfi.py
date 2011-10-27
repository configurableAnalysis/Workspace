
import FWCore.ParameterSet.Config as cms

trackingFailureFilter = cms.EDFilter(
  "TrackingFailureFilter",
  JetSource = cms.InputTag('patJetsAK5PF'),
  TrackSource = cms.InputTag('generalTracks'),
  VertexSource = cms.InputTag('goodVerticesRA4'),
  DzTrVtxMax = cms.double(1),
  DxyTrVtxMax = cms.double(0.2),
  MinSumPtOverHT = cms.double(0.10)
)

goodVerticesRA4 = cms.EDFilter(
  "VertexSelector",
  filter = cms.bool(False),
  src = cms.InputTag("offlinePrimaryVertices"),
  cut = cms.string(" ! isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
)
