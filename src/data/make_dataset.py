# -*- coding: utf-8 -*-
import pandas as pd

#1 Reading data from csv
def read_data(file_path):
    return pd.read_csv(file_path)