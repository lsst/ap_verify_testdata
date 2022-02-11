# Config for lsst.pipe.tasks.script.registerSkymap.MakeSkyMapConfig for use
# with butler register-skymap.
# This config sets up a 1-tract, 1-patch skymap centered on this dataset's
# single raw image.

# Image footprint is approx:
#   RA  ~  56.457 --  56.592 degrees
#   Dec ~ -29.393 -- -29.396 degrees

config.name = "test-skymap"
config.skyMap = "discrete"
config.skyMap.active.pixelScale = 2.0 # arcsec/pixel
config.skyMap.active.tractBuilder = "legacy"
config.skyMap.active.tractBuilder["legacy"].patchInnerDimensions = (4000, 4000) # pixels
config.skyMap["discrete"].raList = [56.525] # degrees
config.skyMap["discrete"].decList = [-29.394] # degrees
config.skyMap["discrete"].radiusList = [0.1] # degrees
