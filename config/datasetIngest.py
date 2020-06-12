# Config override for lsst.ap.verify.DatasetIngestTask
import os

from lsst.utils import getPackageDir

obsDir = os.path.join(getPackageDir('obs_lsst'), 'config')

config.dataIngester.load(os.path.join(obsDir, 'ingest.py'))
config.dataIngester.load(os.path.join(obsDir, 'imsim', 'ingest.py'))
config.calibIngester.load(os.path.join(obsDir, 'ingestCalibs.py'))
config.curatedCalibIngester.load(os.path.join(obsDir, 'ingestCuratedCalibs.py'))

config.refcats = {'gaia': 'gaia_example.tar.gz'}
