#https://twiki.cern.ch/twiki/bin/view/CMS/TrackingPOGFilters
import FWCore.ParameterSet.Config as cms

#from TrackingTools.TrackAssociator.default_cfi import *

toomanystripclus53X = cms.EDFilter('ByClusterSummaryMultiplicityPairEventFilter',
                                                      multiplicityConfig = cms.PSet(
                                                                           firstMultiplicityConfig = cms.PSet(
                                                                                                     clusterSummaryCollection = cms.InputTag("clusterSummaryProducer"),
                                                                                                     subDetEnum = cms.int32(5),
                                                                                                     subDetVariable = cms.string("pHits")
                                                                                                     ),
                                                                           secondMultiplicityConfig = cms.PSet(
                                                                                                      clusterSummaryCollection = cms.InputTag("clusterSummaryProducer"),
                                                                                                      subDetEnum = cms.int32(0),
                                                                                                      subDetVariable = cms.string("cHits")
                                                                                                      ),
                                                                           ),
                                                      cut = cms.string("(mult2>50000) && ( mult2 > 20000+7*mult1)")
                                                      )

manystripclus53X = cms.EDFilter('ByClusterSummaryMultiplicityPairEventFilter',
                                                      multiplicityConfig = cms.PSet(
                                                                           firstMultiplicityConfig = cms.PSet(
                                                                                                     clusterSummaryCollection = cms.InputTag("clusterSummaryProducer"),
                                                                                                     subDetEnum = cms.int32(5),
                                                                                                     subDetVariable = cms.string("pHits")
                                                                                                     ),
                                                                           secondMultiplicityConfig = cms.PSet(
                                                                                                      clusterSummaryCollection = cms.InputTag("clusterSummaryProducer"),
                                                                                                      subDetEnum = cms.int32(0),
                                                                                                      subDetVariable = cms.string("cHits")
                                                                                                      ),
                                                                           ),
                                                      cut = cms.string("( mult2 > 20000+7*mult1)")
                                                      )

logErrorTooManyClusters = cms.EDFilter("LogErrorEventFilter",
                                               src = cms.InputTag("logErrorHarvester"),
                                               maxErrorFractionInLumi = cms.double(1.0), 
                                               maxErrorFractionInRun  = cms.double(1.0),
                                               maxSavedEventsPerLumiAndError = cms.uint32(100000), 
                                               categoriesToWatch = cms.vstring("TooManyClusters"),
                                               modulesToIgnore = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:regionalCosmicTrackerSeeds",
                                                                                                  "PhotonConversionTrajectorySeedProducerFromSingleLeg:photonConvTrajSeedFromSingleLeg")
                                       
                                       )
				       
logErrorTooManyTripletsPairs = cms.EDFilter("LogErrorEventFilter",
                                               src = cms.InputTag("logErrorHarvester"),
                                               maxErrorFractionInLumi = cms.double(1.0), 
                                               maxErrorFractionInRun  = cms.double(1.0), 
                                               maxSavedEventsPerLumiAndError = cms.uint32(100000), 
                                               categoriesToWatch = cms.vstring("TooManyTriplets","TooManyPairs","PixelTripletHLTGenerator"),
                                               modulesToIgnore = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:regionalCosmicTrackerSeeds",
                                                                                                  "PhotonConversionTrajectorySeedProducerFromSingleLeg:photonConvTrajSeedFromSingleLeg")
                                       
                                       )
				       
logErrorTooManySeeds = cms.EDFilter("LogErrorEventFilter",
                                               src = cms.InputTag("logErrorHarvester"),
                                               maxErrorFractionInLumi = cms.double(1.0),
                                               maxErrorFractionInRun  = cms.double(1.0),
                                               maxSavedEventsPerLumiAndError = cms.uint32(100000), 
                                               categoriesToWatch = cms.vstring("TooManySeeds"),
                                                                              )
