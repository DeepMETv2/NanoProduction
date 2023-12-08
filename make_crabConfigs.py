#!/usr/bin/env python3
'''
Generate all crabConfig files using template.
'''
#usage: ./make_crabConfigs.py [-h] -u <username> -s <storageSite>
#
#optional arguments:
#  -h, --help            show this help message and exit
#  -u <username>, --user <username>
#                        storage site username
#  -s <storageSite>, --site <storageSite>
#                        storage site for crab jobs
import argparse

psetName = 'deepmet_NanoAODv12_130X_cfg.py'
outputDatasetTag = 'Run3Summer22NanoAODv12'

jobs = [
['DYJetsToLL', 1200000,
'/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22MiniAODv4-forPOG_130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'],
['TTto2L2Nu', 1200000,
'/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'],
['Zto2Nu-4Jets_HT-100to200', 200000,
'/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'],
['Zto2Nu-4Jets_HT-200to400', 200000,
'/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'],
['Zto2Nu-4Jets_HT-400to800', 200000,
'/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'],
['Zto2Nu-4Jets_HT-800to1500', 200000,
'/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'],
['Zto2Nu-4Jets_HT-1500to2500', 200000,
'/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'],
['Zto2Nu-4Jets_HT-2500', 200000,
'/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM']
]

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', metavar='<username>',
        type=str, required=True, help='storage site username')
    parser.add_argument('-s', '--site', metavar='<storageSite>',
        type=str, required=True, help='storage site for crab jobs')
    return parser.parse_args()

def main():
    args = get_args()
    storageSite = args.site
    username = args.user
    outLFNDirBase = f'/store/user/{username}/deepmet'

    print(f'config.storageSite set to {storageSite}')
    print(f'config.outLFNDirBase set to {outLFNDirBase}')

    config_files = []
    for name, nEvents, inputDataset in jobs:
        config_file = f'crabConfig_{name}.py'
        config_files.append(config_file)
        requestName = f'{name}_{outputDatasetTag}'

        config = ''
        with open('template_crabConfig.py', 'r') as template:
            for line in template.readlines():
                line = line.replace('__requestName__', requestName)
                line = line.replace('__psetName__', psetName)
                line = line.replace('__inputDataset__', inputDataset)
                line = line.replace('__outputDatasetTag__', outputDatasetTag)
                line = line.replace('__nEvents__', str(nEvents))
                line = line.replace('__outLFNDirBase__', outLFNDirBase)
                line = line.replace('__storageSite__', storageSite)
                config += line

        with open(config_file, 'w') as crabConfig:
            crabConfig.write(config)
        print(f'Wrote {config_file}')

    with open('submit_all.sh', 'w') as submit_all:
        submit_all.write('#!/bin/bash\n\n')
        for config_file in config_files:
            cmd = f'crab submit -c {config_file}'
            submit_all.write(f'{cmd}\n')
    print('submit_all.sh updated')

if __name__=='__main__':
    main()
