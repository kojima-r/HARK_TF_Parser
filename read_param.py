import sys
import zipfile
from xml.etree import ElementTree as et

MIC_FILE="transferFunction/microphones.xml"

# argv check
if len(sys.argv)<2:
	print >>sys.stderr, "Usage: read_param.py <in: tf.zip(HARK2 transfer function file)>"
	quit()
tf_filename=sys.argv[1]

# main
with zipfile.ZipFile(tf_filename, 'r') as zf:
	tree=et.fromstring(zf.open(MIC_FILE).read())
	for el in tree.findall(".//positions"):
		# format check
		if el.get("coordinate")!="cartesian":
			print >>sys.stderr, "WARN: unsupported coordinate:",el.get("coordinate")
		# read positions of microphones
		for el in el.findall(".//position"):
			x=el.get("x")
			y=el.get("y")
			z=el.get("z")
			pos_id=el.get("id")
			print (int(pos_id),float(x),float(y),float(z))

