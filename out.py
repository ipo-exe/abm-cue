"""

File Output routines source code

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

import os
import numpy as np


def export_gif(dir_output, dir_images, nm_gif="animation", kind="png", suf=""):
    """
    export gif animation
    :param dir_images: directory path of images
    :param nm_gif: name of gif file
    :param kind: kind of image format
    :param suf: string suffix
    :return: gif file path
    """
    import imageio

    # empty list
    lst_images = []
    for file_name in sorted(os.listdir(dir_images)):
        if suf != "":
            if file_name.endswith(".{}".format(kind)) and file_name.startswith(suf):
                file_path = os.path.join(dir_images, file_name)
                lst_images.append(imageio.imread(file_path))
        else:
            if file_name.endswith(".{}".format(kind)):
                file_path = os.path.join(dir_images, file_name)
                lst_images.append(imageio.imread(file_path))
    # gif name
    fpath = dir_output + "/{}.gif".format(nm_gif)
    # save gif
    imageio.mimsave(fpath, lst_images)
    return fpath


def asc_raster(array, meta, folder, filename, dtype='float32'):
    """
    Function for exporting an .ASC raster file.
    :param array: 2d numpy array
    :param meta: dicitonary of metadata. Example:

    {'ncols': 366,
     'nrows': 434,
      'xllcorner': 559493.087150689564,
       'yllcorner': 6704832.279550871812,
        'cellsize': 28.854232957826,
        'NODATA_value': -9999}

    :param folder: string of directory path
    :param filename: string of file without extension
    :param dtype: string code of data type
    :return: full file name (path and extension) string
    """
    meta_lbls = ('ncols', 'nrows', 'xllcorner', 'yllcorner', 'cellsize', 'NODATA_value')
    ndv = float(meta['NODATA_value'])
    exp_lst = list()
    for i in range(len(meta_lbls)):
        line = '{}    {}\n'.format(meta_lbls[i], meta[meta_lbls[i]])
        exp_lst.append(line)
    # print(exp_lst)
    #
    # data constructor loop:
    def_array = np.array(array, dtype=dtype)
    for i in range(len(def_array)):
        # replace np.nan to no data values
        lcl_row_sum = np.sum((np.isnan(def_array[i])) * 1)
        if lcl_row_sum > 0:
            #print('Yeas')
            for j in range(len(def_array[i])):
                if np.isnan(def_array[i][j]):
                    def_array[i][j] = int(ndv)
        str_join = ' ' + ' '.join(np.array(def_array[i], dtype='str')) + '\n'
        exp_lst.append(str_join)

    flenm = folder + '/' + filename + '.asc'
    fle = open(flenm, 'w+')
    fle.writelines(exp_lst)
    fle.close()
    return flenm