import numpy as np
import h5py

with h5py.File('ply_data_test0.h5','r') as hdf:
	ls = list(hdf.keys())
	print('list of datasets in this file: \n',ls)
	data = hdf.get('data')
	dataset1 = np.array(data)
	print('shape of data: \n',dataset1.shape)

	data = hdf.get('faceId')
	dataset1 = np.array(data)
	print('shape of faceId: \n',dataset1.shape)

	data = hdf.get('label')
	dataset1 = np.array(data)
	print('shape of label: \n',dataset1.shape)

	data = hdf.get('normal')
	dataset1 = np.array(data)
	print('shape of normal: \n',dataset1.shape)
