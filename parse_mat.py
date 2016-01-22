import sys
import struct
import itertools
import numpy as np

def parse_mat(fp):
	# read header
	head=fp.read(32)
	data_type=fp.read(32)
	dim=struct.unpack("i",fp.read(4))[0]
	# read dim
	n=[]
	for i in xrange(dim):
		n.append(struct.unpack("i",fp.read(4))[0])

	# read data
	mat = []
	for i in itertools.product(*[xrange(n[j]) for j in xrange(dim)]):
		if data_type[0:7]=="complex":
			r_val=struct.unpack("f",fp.read(4))[0]
			i_val=struct.unpack("f",fp.read(4))[0]
			mat.append(r_val+1j*i_val)
		elif data_type[0:7]=="float32":
			val=struct.unpack("f",fp.read(4))[0]
			mat.append(val)
		elif data_type[0:5]=="int32":
			val=struct.unpack("f",fp.read(4))[0]
			mat.append(val)
		else:
			print >>sys.stderr,"ERROR: unknown data type:",data_type
	# convert to numpy obj
	np_mat=np.array(mat)
	np_mat.shape=n
	return np_mat,{"head":head,"data_type":data_type,"dim":dim}

if __name__ == '__main__':
	if len(sys.argv)<3:
		print >>sys.stderr, "Usage: read_param.py <in: tf.zip(HARK2 transfer function file)> <out: mat(.npy)>"
		quit()
	in_filename=sys.argv[1]
	out_filename=sys.argv[2]
	fp=open(in_filename,"rb")
	np_mat,info=parse_mat(fp)
	print info
	print np_mat
	print np_mat.shape
	np.save(out_filename,np_mat)

