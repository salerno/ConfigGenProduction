#How to run
#cmsRun READlhe_8TeV_pythiaDecayUE_cff.py
#mv GenEvent_ASCII.dat GenEvent_ASCII_DY.hepmc
#then you can use this one for Delphes
#./DelphesHepMC  Cards/CMS_Phase_I_NoPileUp.tcl test.root GenEvent_ASCII_DY.hepmc
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


process.maxEvents = cms.untracked.PSet(
                                       input = cms.untracked.int32(100),
                                       )


# Input source
process.source = cms.Source("LHESource",
                            fileNames = cms.untracked.vstring('file:/data_CMS/cms/salerno/LHEFiles/GluGluToHHTo2B2Tau_M-125_8TeV_madgraph.lhe')
                            #go0_8TeV_events.lhe
                            )

process.options = cms.untracked.PSet(
                                     SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
                                                   version = cms.untracked.string('$$'),
                                                   annotation = cms.untracked.string(''),
                                                   name = cms.untracked.string('$$')
                                                   )

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
                                           splitLevel = cms.untracked.int32(0),
                                           eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                           outputCommands = process.FEVTDEBUGEventContent.outputCommands,
                                           fileName = cms.untracked.string('test.root'),
                                           dataset = cms.untracked.PSet(
                                                                        filterName = cms.untracked.string(''),
                                                                        dataTier = cms.untracked.string('GEN')
                                                                        ),
                                           SelectEvents = cms.untracked.PSet(
                                                                             SelectEvents = cms.vstring('generation_step')
                                                                             )
                                           )

# Additional output definition

# Other statements
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')
process.generator = cms.EDFilter("Pythia6HadronizerFilter",
                                 ExternalDecays = cms.PSet(
                                                           Tauola = cms.untracked.PSet(
                                                                                       TauolaPolar,
                                                                                       TauolaDefaultInputCards#,
                                                                                       #UseTauolaPolarization = cms.bool(True),
                                                                                       #InputCards = cms.PSet(
                                                                                       #                      mdtau = cms.int32(0),
                                                                                       #                      pjak2 = cms.int32(0),
                                                                                       #                      pjak1 = cms.int32(0)
                                                                                       #                      )
                                                                                       ),
                                                           parameterSets = cms.vstring('Tauola')
                                                           ),
                                 pythiaPylistVerbosity = cms.untracked.int32(1),
                                 filterEfficiency = cms.untracked.double(1.0),
                                 pythiaHepMCVerbosity = cms.untracked.bool(False),
                                 comEnergy = cms.double(8000.0),
                                 maxEventsToPrint = cms.untracked.int32(0),
                                 UseExternalGenerators = cms.untracked.bool(True),
                                 PythiaParameters = cms.PSet(
                                                             pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution',
                                                                                            'MSTJ(22)=2     ! Decay those unstable particles',
                                                                                            'PARJ(71)=10 .  ! for which ctau  10 mm',
                                                                                            'MSTP(33)=0     ! no K factors in hard cross sections',
                                                                                            'MSTP(2)=1      ! which order running alphaS',
                                                                                            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
                                                                                            'MSTP(52)=2     ! work with LHAPDF',
                                                                                            'PARP(82)=1.921 ! pt cutoff for multiparton interactions',
                                                                                            'PARP(89)=1800. ! sqrts for which PARP82 is set',
                                                                                            'PARP(90)=0.227 ! Multiple interactions: rescaling power',
                                                                                            'MSTP(95)=6     ! CR (color reconnection parameters)',
                                                                                            'PARP(77)=1.016 ! CR',
                                                                                            'PARP(78)=0.538 ! CR',
                                                                                            'PARP(80)=0.1   ! Prob. colored parton from BBR',
                                                                                            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
                                                                                            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',
                                                                                            'PARP(62)=1.025 ! ISR cutoff',
                                                                                            'MSTP(91)=1     ! Gaussian primordial kT',
                                                                                            'PARP(93)=10.0  ! primordial kT-max',
                                                                                            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
                                                                                            'MSTP(82)=4     ! Defines the multi-parton model'),
                                                             processParameters = cms.vstring('MSEL=0           ! User defined processes',
                                                                                             'PMAS(5,1)=4.75   ! b quark mass',
                                                                                             'PMAS(6,1)=172.5  ! t quark mass',
                                                                                             'MDME(210,1)=0    ! Higgs decay into dd',
                                                                                             'MDME(211,1)=0    ! Higgs decay into uu',
                                                                                             'MDME(212,1)=0    ! Higgs decay into ss',
                                                                                             'MDME(213,1)=0    ! Higgs decay into cc',
                                                                                             'MDME(214,1)=5    ! Higgs decay into bb',
                                                                                             'MDME(215,1)=0    ! Higgs decay into tt',
                                                                                             'MDME(216,1)=0    ! Higgs decay into bbbar prime',
                                                                                             'MDME(217,1)=0    ! Higgs decay into ttbar prime',
                                                                                             'MDME(218,1)=0    ! Higgs decay into e e',
                                                                                             'MDME(219,1)=0    ! Higgs decay into mu mu',
                                                                                             'MDME(220,1)=4    ! Higgs decay into tau tau',
                                                                                             'MDME(221,1)=0    ! Higgs decay into tau tau prime',
                                                                                             'MDME(222,1)=0    ! Higgs decay into g g',
                                                                                             'MDME(223,1)=0    ! Higgs decay into gam gam',
                                                                                             'MDME(224,1)=0    ! Higgs decay into gam Z',
                                                                                             'MDME(226,1)=0    ! Higgs decay into W W',
                                                                                             'MDME(174,1)=0           !Z decay into d dbar',
                                                                                             'MDME(175,1)=0           !Z decay into u ubar',
                                                                                             'MDME(176,1)=0           !Z decay into s sbar',
                                                                                             'MDME(177,1)=0           !Z decay into c cbar',
                                                                                             'MDME(178,1)=0           !Z decay into b bbar',
                                                                                             'MDME(179,1)=0           !Z decay into t tbar',
                                                                                             'MDME(183,1)=0           !Z decay into nu_e nu_ebar'),
                                                             parameterSets = cms.vstring('pythiaUESettings',
                                                                                         'processParameters'
                                                                                         )
                                                             )
                                 )

process.writer = cms.EDAnalyzer("HepMCEventWriter")

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.outpath = cms.EndPath(process.writer)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step)
process.schedule.extend([process.outpath])

# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

