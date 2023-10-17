import h5py
import numpy as np

file = h5py.File('/project/cigserver4/export2/Dataset/fastmri_brain_multicoil/file_brain_AXFLAIR_200_6002447.h5', 'r')
print(list(file.keys()))
print(file['kspace'].shape)
print(file['reconstruction_rss'].shape)
print(file['ismrmrd_header'].shape)