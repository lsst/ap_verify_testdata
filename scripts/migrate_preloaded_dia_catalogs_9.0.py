"""Migrate preloaded/dia_catalogs/apdb from sdm_schemas 8.0 to 9.0.
"""

import argparse
import pandas as pd
from glob import glob
import numpy as np
from astropy.time import Time

parser = argparse.ArgumentParser()
parser.add_argument("ap_verify_dataset_path", help="path to ap_verify dataset's base directory")
args = parser.parse_args()

def find_preloaded_parquet(directory):
    return glob(f'{directory}/*/preloaded*.parq')

# 8.0->9.0 consists of changing types from timestamp to double
# all of the columns are also renamed

diaObject_timestamp_cols = {'validityStart': 'validityStartMjdTai', 
                            'validityEnd':'validityEndMjdTai'}

diaSource_timestamp_cols = {'ssObjectReassocTime': 'ssObjectReassocTimeMjdTai', 
                            'time_processed': 'timeProcessedMjdTai',
                            'time_withdrawn': 'timeWithdrawnMjdTai'}

diaForcedSource_timestamp_cols = {'time_processed': 'timeProcessedMjdTai',
                                  'time_withdrawn': 'timeWithdrawnMjdTai'}


def convert_to_MjdTai(datetime):
    if pd.isnull(datetime):
        return None
    return Time(datetime).tai.mjd

def process_file(filename, timestamp_cols):

    df = pd.read_parquet(filename)

    for old_key, new_key in timestamp_cols.items():
        df[new_key] = df[old_key].apply(convert_to_MjdTai) 
        df = df.drop(columns=old_key)

    df.to_parquet(filename)


# diaObject

do_files = find_preloaded_parquet(f'{args.ap_verify_dataset_path}/preloaded/dia_catalogs/apdb/preloaded_dia_object/')

assert(len(do_files))

for filename in do_files:
    process_file(filename, diaObject_timestamp_cols)

# diaSource

ds_files = find_preloaded_parquet(f'{args.ap_verify_dataset_path}/preloaded/dia_catalogs/apdb/preloaded_dia_source/')

assert(len(ds_files))

for filename in ds_files:
    process_file(filename, diaSource_timestamp_cols)

# diaForcedSource

dfs_files = find_preloaded_parquet(f'{args.ap_verify_dataset_path}/preloaded/dia_catalogs/apdb/preloaded_dia_forced_source/')

assert(len(dfs_files))

for filename in dfs_files:
    process_file(filename, diaForcedSource_timestamp_cols)
