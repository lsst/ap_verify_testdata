"""Migrate preloaded/dia_catalogs/apdb from sdm_schemas 7.0 to 8.0.
"""

import argparse
import importlib.util
import sys
import pandas as pd
from glob import glob
import numpy as np
import os

parser = argparse.ArgumentParser()
parser.add_argument("ap_verify_dataset_path", help="path to ap_verify dataset's base directory")
args = parser.parse_args()

migrate_dir = os.getenv('DAX_APDB_MIGRATE_DIR')
assert(len(migrate_dir))

dax_apdb_migration_file = f"{migrate_dir}/migrations/sql/schema/schema_8.0.0.py"

def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# load in a local version of https://github.com/lsst-dm/dax_apdb_migrate/blob/main/migrations/sql/schema/schema_8.0.0.py
dax_migrate = import_from_path('migrate', dax_apdb_migration_file)

def find_preloaded_parquet(directory):
    return glob(f'{directory}/*/preloaded*.parq')


# diaObject

do_files = find_preloaded_parquet(f'{args.ap_verify_dataset_path}/preloaded/dia_catalogs/apdb/preloaded_dia_object/')

assert(len(do_files))

for filename in do_files:
    df = pd.read_parquet(filename)

    drop_cols = list(dax_migrate._dropped_columns['DiaObject'].keys())
    df = df.drop(columns = drop_cols)

    # no renames for DIAObject

    add_cols = list(dax_migrate._added_columns['DiaObject'].keys())
    for col in add_cols:
        # all the additions are nullable float or double
        df[col] = np.nan

    df.to_parquet(filename)

# diaSource

ds_files = find_preloaded_parquet(f'{args.ap_verify_dataset_path}/preloaded/dia_catalogs/apdb/preloaded_dia_source/')

assert(len(ds_files))

for filename in ds_files:
    df = pd.read_parquet(filename)

    drop_cols = list(dax_migrate._dropped_columns['DiaSource'].keys())
    df = df.drop(columns = drop_cols)

    # no renames for DIAObject
    rename_cols = dax_migrate._renamed_columns['DiaSource']
    df = df.rename(columns = rename_cols)

    add_cols = list(dax_migrate._added_columns['DiaSource'].keys())
    for col in add_cols:
        # all the additions are nullable float or double
        df[col] = np.nan

    df.to_parquet(filename)


# no changes to diaForcedSource
