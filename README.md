# NanoProduction

Generate custom NanoAOD samples with PF candidates using CMSSW. This repository is an adaptation of [PFNano](https://github.com/DeepMETv2/PFNano), which is now migrated into native [CMSSW](https://github.com/cms-sw/cmssw).

This branch is used to make **NanoAODv12** in **CMSSW_13_0_13** for Run3. NanoAODv12 is the current recommended version for Run3. Refer to the [XPOG nanoAOD-doc](https://gitlab.cern.ch/cms-nanoAOD/nanoaod-doc/-/wikis/home) for the most up-to-date recommendations.

The functionality of PFNano was added to CMSSW_13_0_13 by the BTV group in the CMSSW branch [`Ming-Yan/130X-fixPuppi_NanoV12`](https://github.com/Ming-Yan/cmssw/tree/130X-fixPuppi_NanoV12), and was further adapted for DeepMET in the CMSSW branch [`alejands/130X-DeepMET_NanoV12`](https://github.com/alejands/cmssw/tree/130X-DeepMET_NanoV12).

## Setup

Create the CMSSW environment, merge the relevant modifications, and clone this workspace.

```
cmsrel CMSSW_13_0_13
cd CMSSW_13_0_13/src
cmsenv
git cms-merge-topic alejands:130X-DeepMET_NanoV12
scram b -j 10

git clone git@github.com:alejands/NanoProduction.git
cd NanoProduction
```

## Creating your own Python configuration file

The `cmsDriver.py` command used to generate the configuration file is located in `run_cmsDriver.sh`. You can also see here for a summary of [private NanoAOD production](https://gitlab.cern.ch/cms-nanoAOD/nanoaod-doc/-/wikis/Instructions/Private%20production).

If you wish to edit this for different conditions, the most important arguments to edit are `--era` and `--conditions`. You can obtain these arguments from the [analysis recipes from PdmV](https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV#Analysis_Recipes). Here are the [recipes for Run3 MC production](https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun3Analysis#Monte_Carlo).

Feel free to also change `--python_filename` with your own name choice for the configuration file, or change `--filein` with some input file to locally test your configuration.

To generate the Python configuration file,

```
./run_cmsDriver.sh
```

### Test your Python configuration file

Before submitting CRAB jobs, **test your configuration file locally**.

To locally run the configuration provided,

```
cmsRun deepmet_NanoAODv12_130X_cfg.py
```

By default, the configuration file above will run over 10 events when run locally. (See  argument `-n` in the `cmsDriver.py` command, or see `process.maxEvents` in the configuration file. CRAB ignores this when running jobs.)

## CRAB jobs

### Create CRAB configurations

The CRAB configurations can be generated using

```
./make_crabConfigs.py -u <username> -s <storage-site>
```

which uses `template_crabConfig.py` as a base. You can edit the parameters in `make_crabConfigs.py` for your own purposes.

You must pass your own username and a storage site you can write to as arguments. An an example,

```
./make_crabCongigs.py -u alejands -s T3_US_CMU
```

### Submit CRAB jobs

The previous script also generates a script called `submit_all.sh` which you can use to automatically submit all your CRAB jobs.

```
# If you haven't already, run
# voms-proxy-init --voms cms --valid 192:00
./submit_all.sh
```

### Monitoring CRAB jobs

You can monitor your jobs with

```
crab status -d jobs/<crab-job-directory>
```

or for a quick view, look up your username in this [Grafana dashboard](https://monit-grafana.cern.ch/d/15468761344/personal-tasks-monitoring-globalview?from=now-2d&to=now&orgId=11&var-user=All&var-site=All&var-current_url=%2Fd%2FcmsTMDetail%2Fcms_task_monitoring&var-task=All). You can also adjust the time-range and page refresh rate on the top right.

The Grafana page for your username is really handy and I recommend bookmarking it for future projects! (Note: jobs showing up as failed on Grafana does not mean they were not retried or uploaded to DAS successfully. Refer to `crab status` or `crab report` once all your jobs are done running.)

### Job output

Once your jobs are finished running, they will be available on [DAS](https://cmsweb.cern.ch/das/), though it can take a few hours for a finished job to upload its output files. 

You can see the output dataset name, how many events have been uploaded, and a link to the DAS webpage using

```
crab report -d jobs/<crab-job-directory>
```

If you're searching for the dataset on the DAS webpage on your own, be sure to select `prod/phys03` in the dbs instance drop down menu.

If you're using `dasgoclient` on the command line, be sure to add `instance=prod/phys03` to the end (the keyword argument order seems to matter) of your query string. See examples of this in `get_nano_files.sh`.
