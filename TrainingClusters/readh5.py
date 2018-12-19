import numpy as np
import h5py

with h5py.File('data.h5','r') as hdf:
	ls = list(hdf.keys())
	print('list of datasets in this file: \n',ls)

	data = hdf.get('data')
	dataset1 = np.array(data)
	print('shape of data: \n',dataset1.shape)

	data = hdf.get('label')
	dataset1 = np.array(data)
	print('shape of label: \n',dataset1.shape)
	print(dataset1)
