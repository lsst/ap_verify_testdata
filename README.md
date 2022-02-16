`ap_verify_testdata`
====================

Data from `testdata_lsst` for small-scale tests of [`ap_verify`](https://github.com/lsst-dm/ap_verify/) functionality.

The data were originally identical to the files provided by [`testdata_lsst`](https://github.com/lsst/testdata_lsst/).
See that package for documentation of the file contents.

However, [DM-26138](https://jira.lsstcorp.org/browse/DM-26138) updated the filter names used for LSST imSim data to include the throughputs version (e.g. "i" -> "i_sim_1.4").
This affects the headers of both raw and master calibration files, as well as their usual filenames.
These updates have been applied to the files in `ap_verify_testdata`, but not (yet) to the files in `testdata_lsst`.

Relevant Files and Directories
------------------------------
path                  | description
:---------------------|:-----------------------------
`raw`                 | Raw fits files from [`testdata_lsst`](https://github.com/lsst/testdata_lsst/tree/master/data) in `i` band.
`config`              | Dataset-specific configs to help Stack code work with this dataset.
`preloaded`           | A Gen 3 Butler repository containing master calibration files from `lsst-dev:/datasets/DC2/repoRun2.2i` for `i` band, a token `goodSeeing` template, and a small Gaia reference catalog.
`dataIds.list`        | List of dataIds in this repo. For use in running Tasks. Currently set to run all Ids.


Git LFS
-------

To clone and use this repository, you'll need Git Large File Storage (LFS).

Our [Developer Guide](http://developer.lsst.io/en/latest/tools/git_lfs.html) explains how to setup Git LFS for LSST development.

Usage
-----

`ap_verify_testdata` is not included in `lsst_distrib` and is not available through `newinstall.sh`.
However, it can be installed explicitly with the [LSST Software Build Tool](https://developer.lsst.io/stack/lsstsw.html) or by cloning directly:

    git clone https://github.com/lsst/ap_verify_testdata/
    setup -r ap_verify_testdata
