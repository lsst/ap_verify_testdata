`ap_verify_testdata`
====================

Data from `obs_test` for small-scale tests of `ap_verify` functionality.

The data are uningested, but otherwise identical to the files provided by `obs_test`.
See that package for documentation of the file contents.

Relevant Files and Directories
------------------------------
path                  | description
:---------------------|:-----------------------------
`raw`                 | Raw, compressed fits files from [`obs_test`](https://github.com/lsst/obs_test/tree/master/data) in `g` and `r` band.
`calib`               | Master calibration files from [`obs_test`](https://github.com/lsst/obs_test/tree/master/data) for `g` and `r` band.
`config`              | Dataset-specific configs to help Stack code work with this dataset.
`templates`           | To be populated with `TemplateCoadd` images produced by a compatible version of the LSST pipelines. Must be organized as a filesystem-based Butler repo. Currently empty.
`repo`                | Butler repo into which raw data can be ingested. This should be copied to an appropriate location before ingestion.
`refcats`             | A small Gaia reference catalog.
`dataIds.list`        | List of dataIds in this repo. For use in running Tasks. Currently set to run all Ids.


Git LFS
-------

To clone and use this repository, you'll need Git Large File Storage (LFS).

Our [Developer Guide](http://developer.lsst.io/en/latest/tools/git_lfs.html) explains how to setup Git LFS for LSST development.

