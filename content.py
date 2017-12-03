#print file
def content(filename):
	with open(filename, mode='r') as f:
		print (f.read())
