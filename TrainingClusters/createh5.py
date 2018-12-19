import numpy as np
import h5py
import pcl

dataset = np.zeros(shape=(32,2048,3))
labels = np.zeros(shape=(32,1))

for i in range(0,10):
	x = pcl.io.loadpcd("unidentified_"+str(i)+".pcd")
	z = x.xyz
	offset=2048-z.shape[0]
	x = np.zeros((offset,3))
	dataset2 = np.append(z,x,0)
	dataset[i]=dataset2
	labels[i]=0

for i in range(0,11):
	x = pcl.io.loadpcd("car_"+str(i)+".pcd")
	z = x.xyz
	offset=2048-z.shape[0]
	x = np.zeros((offset,3))
	dataset2 = np.append(z,x,0)
	dataset[i+10]=dataset2
	labels[i+10]=1

for i in range(0,11):
	x = pcl.io.loadpcd("wall_"+str(i)+".pcd")
	z = x.xyz
	offset=2048-z.shape[0]
	x = np.zeros((offset,3))
	dataset2 = np.append(z,x,0)
	dataset[i+21]=dataset2
	labels[i+21]=2

hf = h5py.File('data.h5','w')

hf.create_dataset('data',data=dataset)
hf.create_dataset('label',data=labels)
hf.close()
