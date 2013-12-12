# ConfigGenProduction
Configuration files for MC generation (lhe,hepmc,...) 


###Produce a hepmc form lhe
```
cmsrel CMSSW_5_3_9
cd CMSSW_5_3_9/src/
scramv1 b 
cmsenv
git clone https://github.com/salerno/ConfigGenProduction ConfigGenProduction
cp ConfigGenProduction/READlhe_8TeV_pythiaDecayUE_cff.py .
cmsRun READlhe_8TeV_pythiaDecayUE_cff.py
mv GenEvent_ASCII.dat GenEvent_ASCII_DY.hepmc
```
then you can run Delphes
