# ConfigGenProduction
Configuration files for MC generation (lhe,hepmc,...) 

###Setup the code
```
cmsrel CMSSW_5_3_9
cd CMSSW_5_3_9/src/
scramv1 b 
cmsenv
git clone https://github.com/salerno/ConfigGenProduction ConfigGenProduction
```

###Produce a hepmc from lhe
```
cmsRun READlhe_8TeV_pythiaDecayUE_cff.py
mv GenEvent_ASCII.dat GenEvent_ASCII.hepmc
```

###Produce a hepmc with minimum bias events from empty source
```
cmsRun MinimumBias_8TeV_pythiaDecayUE_cff.py
mv GenEvent_ASCII.dat GenEvent_ASCII.hepmc
```

####Use of the hepmc file

a) You can run [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes) here general instructions (that included last CMS modification) to install it
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
