#!/usr/bin/env python

import xarray as xr
import sys

dataset = xr.open_dataset(sys.argv[1])
df = dataset.to_dataframe()
df.to_csv(sys.argv[2])
