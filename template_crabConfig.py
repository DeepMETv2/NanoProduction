from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '__requestName__'
config.General.workArea = 'jobs'
config.General.transferLogs = True
config.General.instance = 'prod'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '__psetName__'

config.Data.inputDataset = '__inputDataset__'
config.Data.splitting = 'Automatic'
config.Data.totalUnits = __nEvents__
config.Data.outLFNDirBase = '__outLFNDirBase__'

config.Site.storageSite = '__storageSite__'
