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
then you can run [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes) here general instructions (that included last CMS modification) to install it
```
git clone https://github.com/sethzenz/Delphes.git
cd Delphes
./configure
make
```
then to read the hepmc file in Delphes and produce the output
```
./DelphesHepMC  Cards/CMS_Phase_I_NoPileUp.tcl output.root GenEvent_ASCII_DY.hepmc
```
