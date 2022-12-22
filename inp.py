"""

CUE 1d input routines

Copyright (C) 2022 Iporã Brito Possantti



************ GNU GENERAL PUBLIC LICENSE ************

https://www.gnu.org/licenses/gpl-3.0.en.html

Permissions:
 - Commercial use
 - Distribution
 - Modification
 - Patent use
 - Private use

Conditions:
 - Disclose source
 - License and copyright notice
 - Same license
 - State changes

Limitations:
 - Liability
 - Warranty

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import pandas as pd
import numpy as np

def open_df(
    s_filepath,
    s_sep=";",
    s_date_field="",
    s_mandatory_fields="",
):
    """
    general dataframe openner
    :param s_filepath: string to file
    :param s_sep: string separator
    :param s_date_field: string date field
    :param s_mandatory_fields: concat string of mandatory fields by ' & '
    :return: dict object with Error Report and dataframe
    """
    try:
        # handle date field
        if s_date_field == "":
            df_lcl = pd.read_csv(s_filepath, sep=s_sep, skipinitialspace=True)
        else:
            df_lcl = pd.read_csv(
                s_filepath, sep=s_sep, parse_dates=[s_date_field], skipinitialspace=True
            )
        # handle mandatory fields:
        if s_mandatory_fields == "":
            pass
        else:
            lst_fields = s_mandatory_fields.split(" & ")
            for f in lst_fields:
                try:
                    df_aux = df_lcl[f]
                except KeyError:
                    return {"Error Report": "Invalid formatting.", "OK Flag": False}
        return {"df": df_lcl, "Error Report": "File OK", "OK Flag": True}
    except FileNotFoundError:
        return {"Error Report": "File not found", "OK Flag": False}
    except ValueError:
        return {"Error Report": "Invalid formatting", "OK Flag": False}


def import_data_table(s_table_name, s_filepath):
    """
    routine to import data table
    :param s_table_name: table standard name
    :type s_table_name: str
    :param s_filepath: file path
    :type s_filepath: str
    :return: dictionary of the opened object
    :rtype: dict
    """
    # import documentation file
    df_iofiles = pd.read_csv("./docs/iofiles.csv", sep=";", skipinitialspace=True)
    # retrieve mandatory fields
    df_file = df_iofiles.query('Name == "{}"'.format(s_table_name))
    s_mandatory_fields = df_file["Mandatory Fields"].values[0]
    # get opening object
    dct_open = open_df(
        s_filepath=s_filepath, s_sep=";", s_mandatory_fields=s_mandatory_fields
    )
    return dct_open


def asc_raster(file, nan=False, dtype='int16'):
    """
    A function to import .ASC raster files
    :param file: string of file path with the '.asc' extension
    :param nan: boolean to convert nan values to np.nan
    :param dtype: string code to data type. Options: 'int16', 'int32', 'float32' etc
    :return: 1) metadata dictionary and 2) numpy 2d array
    """
    def_f = open(file)
    def_lst = def_f.readlines()
    def_f.close()
    #
    # get metadata constructor loop
    meta_lbls = ('ncols', 'nrows', 'xllcorner', 'yllcorner', 'cellsize', 'NODATA_value')
    meta_format = ('int', 'int', 'float', 'float', 'float', 'float')
    meta_dct = dict()
    for i in range(6):
        lcl_lst = def_lst[i].split(' ')
        lcl_meta_str = lcl_lst[len(lcl_lst) - 1].split('\n')[0]
        if meta_format[i] == 'int':
            meta_dct[meta_lbls[i]] = int(lcl_meta_str)
        else:
            meta_dct[meta_lbls[i]] = float(lcl_meta_str)
    #
    # array constructor loop:
    array_lst = list()
    for i in range(6, len(def_lst)):
        lcl_lst = def_lst[i].split(' ')[1:]
        lcl_lst[len(lcl_lst) - 1] = lcl_lst[len(lcl_lst) - 1].split('\n')[0]
        array_lst.append(lcl_lst)
    def_array = np.array(array_lst, dtype=dtype)
    #
    # replace NoData value by np.nan
    if nan:
        ndv = float(meta_dct['NODATA_value'])
        for i in range(len(def_array)):
            lcl_row_sum = np.sum((def_array[i] == ndv) * 1)
            if lcl_row_sum > 0:
                for j in range(len(def_array[i])):
                    if def_array[i][j] == ndv:
                        def_array[i][j] = np.nan
    return meta_dct, def_array
