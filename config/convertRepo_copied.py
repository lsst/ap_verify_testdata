# Config overrides for lsst.obs.base.gen2to3.ConvertRepoTask
# To be used by add_gen3_repo.py to copy-ingest tarred datasets only

config.datasetIncludePatterns = ["ref_cat", "defects"]

config.refCats = ['gaia']
for refcat in config.refCats:
    config.runs[refcat] = "refcats"

# Handled by convertRepo_calibs.py, and must be done only once
config.doRegisterInstrument = False
