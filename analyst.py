"""

Analyst routines

Copyright (C) 2022 Iporã Brito Possantti

References:


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
import numpy as np
import pandas as pd


def shannon_entropy(grd):
    """
    Routine for shannon entropy
    :param grd: numpy nd array
    :return: float of Shannon Entropy
    """
    # convert grid to integer
    grd = grd.astype('uint16')
    # get unique values and counting
    vct_unique, vct_counts = np.unique(grd, return_counts=True)
    # for each unique compute the p
    vct_prob = vct_counts / grd.size
    # compute shannon entropy
    n_shannon = 0.0
    for i in range(len(vct_unique)):
        #print('{:.2f} * {:.2f} = {:.2f}'.format(vct_prob[i], np.log2(vct_prob[i]), vct_prob[i] * np.log2(vct_prob[i])))
        n_shannon = n_shannon + (vct_prob[i] * np.log2(vct_prob[i]))
    return - n_shannon

'''
a = np.array([1, 1, 1, 2, 1])
b = np.array([1, 2, 5, 4, 2])
c = np.random.randint(low=10, high=20, size=10)

se_a = shannon_entropy(grd=a)
print(se_a)
se_b = shannon_entropy(grd=b)
print(se_b)
se_c = shannon_entropy(grd=c)
print(se_c)
'''





