#!/bin/bash

# cmsDriver template obtained from nanoAOD-doc
# https://gitlab.cern.ch/cms-nanoAOD/nanoaod-doc/-/wikis/Instructions/Private-production

# era and conditions obtained from PdmV recipes
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVRun3Analysis#Recipes_for_Run3Summer22_and_Run

cmsDriver.py --python_filename deepmet_run3summer22_nanov12_cfg.py \
--step NANO --mc --conditions 130X_mcRun3_2022_realistic_v5 \
--era Run3 --eventcontent NANOAODSIM --datatier NANOAODSIM \
--filein "/store/mc/Run3Summer22MiniAODv4"\
"/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/MINIAODSIM"\
"/forPOG_130X_mcRun3_2022_realistic_v5-v2/"\
"2520000/08252cf5-7cda-4c6d-b358-0db4779efc6f.root" \
--fileout nanov12_deepmet.root \
--customise_commands="process.add_(cms.Service('InitRootHandlers',"\
"EnableIMT=cms.untracked.bool(False)));"\
"process.MessageLogger.cerr.FwkReport.reportEvery=1000;"\
"process.NANOAODSIMoutput.fakeNameForCrab = cms.untracked.bool(True)"  \
--nThreads 4 -n 10 \
--customise PhysicsTools/NanoAOD/custom_btv_cff.PrepBTVCustomNanoAOD_MC \
--no_exec
