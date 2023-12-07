from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'Zto2Nu-4Jets_HT-400to800_Run3Summer22NanoAODv12'
config.General.workArea = 'jobs'
config.General.transferLogs = True
config.General.instance = 'prod'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'deepmet_run3summer22_nanov12_cfg.py'
config.JobType.maxMemoryMB = 5000
config.JobType.numCores = 4

config.Data.inputDataset = '/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
config.Data.splitting = 'Automatic'
config.Data.totalUnits = 200000
config.Data.outLFNDirBase = '/store/user/alejands/deepmet'

config.Site.storageSite = 'T3_US_CMU'
