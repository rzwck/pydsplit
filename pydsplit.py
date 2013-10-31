import sys,os

# incsplit.py [startoffset] [blocksize] [filename]

startoffset = int(sys.argv[1])
blocksize = int(sys.argv[2])
filename = sys.argv[3]

size = os.path.getsize(filename)

fh = open(filename, "rb")
nameonly = os.path.splitext(filename)[0]
extonly = os.path.splitext(filename)[1]

data = ""
if startoffset > 0:
	data = fh.read(startoffset)

cursor = fh.tell()
while cursor < size:
	data += fh.read(blocksize)
	newname = nameonly + "_" + str(len(data)) + extonly
	cursor = fh.tell()
	
	newfh = open(newname, "wb")
	newfh.write(data)
	newfh.close()

fh.close()
