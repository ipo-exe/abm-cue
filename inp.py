'''

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

'''
import pandas as pd


def open_df(s_filepath, s_sep=';', s_date_field='', s_mandatory_fields='',):
    """
    general dataframe openner
    :param s_filepath: string to file
    :param s_sep: string separator
    :param s_date_field: string datefield
    :param s_mandatory_fields: concat string of mandatory fields by ' & '
    :return: dict object with Error Report and dataframe
    """
    try:
        # handle date field
        if s_date_field == '':
            df_lcl = pd.read_csv(s_filepath, sep=s_sep, skipinitialspace=True)
        else:
            df_lcl = pd.read_csv(s_filepath, sep=s_sep, parse_dates=[s_date_field], skipinitialspace=True)
        # handle mandatory fields:
        if s_mandatory_fields == '':
            pass
        else:
            lst_fields = s_mandatory_fields.split(' & ')
            for f in lst_fields:
                try:
                    df_aux = df_lcl[f]
                except KeyError:
                    return {'Error Report': 'Invalid formatting.', 'OK Flag': False}
        return {'df': df_lcl, 'Error Report': 'File OK', 'OK Flag': True}
    except FileNotFoundError:
        return {'Error Report': 'File not found', 'OK Flag': False}
    except ValueError:
        return {'Error Report': 'Invalid formatting', 'OK Flag': False}


def import_data_table(s_table_name, s_filepath):
    # import documentation file
    df_iofiles = pd.read_csv('./docs/iofiles.csv', sep=';', skipinitialspace=True)
    # retrieve mandatory fields
    df_file = df_iofiles.query('Name == "{}"'.format(s_table_name))
    s_mandatory_fields = df_file['Mandatory Fields'].values[0]
    # get opening object
    dct_open = open_df(s_filepath=s_filepath, s_sep=';', s_mandatory_fields=s_mandatory_fields)
    return dct_open

