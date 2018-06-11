.. _ap_verify_testdata-package:

##################
ap_verify_testdata
##################

The ``ap_verify_testdata`` package contains several files from `obs_test <https://github.com/lsst/obs_test/>`_.
The package is intended to test dataset support in ``ap_verify`` code.

Project info
============

Repository
   https://github.com/lsst-dm/ap_verify_testdata

.. Datasets do not have their own (or a collective) Jira components; by convention we include them in ap_verify

Jira component
   `ap_verify <https://jira.lsstcorp.org/issues/?jql=project %3D DM %20AND%20 component %3D ap_verify %20AND%20 text ~ "testdata">`_

Dataset Contents
================

This package provides a number of demonstration files copied from `obs_test <https://github.com/lsst/obs_test/>`_.
See that package for detailed file and provenance information.

The dataset contents include raw images, biases, and flats.
The dataset does not provide any image differencing templates.
It does have a small Gaia DR1 reference catalog, but it is not guaranteed to overlap with the footprint of the raw data.

Intended Use
============

This package provides a minimal valid dataset for testing dataset handling, particularly ingestion.
Because there are no templates and the reference catalog is not guaranteed to match the data, this dataset is not suitable for full ``ap_verify`` runs.
