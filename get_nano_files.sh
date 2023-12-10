#!/bin/bash
echo "DYJetsToLL" > nano_files.txt
dasgoclient --query="file dataset=/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/alejands-Run3Summer22NanoAODv12-d9ddddd4f19357b983eff889332759e6/USER instance=prod/phys03" >> nano_files.txt

echo "TTto2L2Nu" >> nano_files.txt
dasgoclient --query="file dataset=/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/alejands-Run3Summer22NanoAODv12-d9ddddd4f19357b983eff889332759e6/USER instance=prod/phys03" >> nano_files.txt

echo "Zto2Nu-4Jets_HT-100to200" >> nano_files.txt
dasgoclient --query="file dataset=/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/alejands-Run3Summer22NanoAODv12-d9ddddd4f19357b983eff889332759e6/USER instance=prod/phys03" >> nano_files.txt

echo "Zto2Nu-4Jets_HT-200to400" >> nano_files.txt
dasgoclient --query="file dataset=/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/alejands-Run3Summer22NanoAODv12-d9ddddd4f19357b983eff889332759e6/USER instance=prod/phys03" >> nano_files.txt

echo "Zto2Nu-4Jets_HT-400to800" >> nano_files.txt
dasgoclient --query="file dataset=/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/alejands-Run3Summer22NanoAODv12-d9ddddd4f19357b983eff889332759e6/USER instance=prod/phys03" >> nano_files.txt

echo "Zto2Nu-4Jets_HT-800to1500" >> nano_files.txt
dasgoclient --query="file dataset=/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/alejands-Run3Summer22NanoAODv12-d9ddddd4f19357b983eff889332759e6/USER instance=prod/phys03" >> nano_files.txt

echo "/Zto2Nu-4Jets_HT-1500to2500" >> nano_files.txt
dasgoclient --query="file dataset=/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/alejands-Run3Summer22NanoAODv12-d9ddddd4f19357b983eff889332759e6/USER instance=prod/phys03" >> nano_files.txt

echo "Zto2Nu-4Jets_HT-2500" >> nano_files.txt
dasgoclient --query="file dataset=/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/alejands-Run3Summer22NanoAODv12-d9ddddd4f19357b983eff889332759e6/USER instance=prod/phys03" >> nano_files.txt
