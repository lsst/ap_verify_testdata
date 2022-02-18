.. _ap_verify_testdata-package:

##################
ap_verify_testdata
##################

The ``ap_verify_testdata`` package contains several files from `testdata_lsst <https://github.com/lsst/testdata_lsst/>`_.
The package is intended to test dataset support in :doc:`/modules/lsst.ap.verify/index` code.

.. _ap_verify_testdata-using:

Using ap_verify_testdata
========================

This package provides a minimal valid dataset for testing dataset handling, particularly ingestion.
Because the template is a mock and the reference catalog is not guaranteed to match the data, this dataset is not suitable for full ``ap_verify`` runs.

.. _ap_verify_testdata-contents:

Dataset contents
================

This package provides a number of demonstration files copied from `testdata_lsst <https://github.com/lsst/testdata_lsst/>`_.
See that package for detailed file and provenance information.

The dataset contents include raw ``i`` images and flats, as well as a mock ``goodSeeing`` template covering the raws.
It also has a small Gaia DR1 reference catalog, but it is not guaranteed to overlap with the footprint of the raw data.

.. _ap_verify_testdata-contributing:

Contributing
============

``ap_verify_testdata`` is developed at https://github.com/lsst/ap_verify_testdata.
You can find Jira issues for this module under the `ap_verify <https://jira.lsstcorp.org/issues/?jql=project%20%3D%20DM%20AND%20component%20%3D%20ap_verify%20AND%20text~"testdata">`_ component.

.. If there are topics related to developing this module (rather than using it), link to this from a toctree placed here.

.. .. toctree::
..    :maxdepth: 1
