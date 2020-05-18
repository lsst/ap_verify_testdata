# Config overrides for lsst.obs.base.gen2to3.ConvertRepoTask
# To be used by add_gen3_repo.py to link-ingest calibs only

config.datasetIgnorePatterns.extend(["raw", "*Coadd_skyMap", "ref_cat", "defects"])
