import os
path = 'dctorset/'
files = os.listdir(path)
i = 0
for file in files:
	if(i <= 9):
	    os.rename(os.path.join(path, file), os.path.join(path, 'b01-001-s00-00' + str(i) + '.jpg')) 
	else:
		os.rename(os.path.join(path, file), os.path.join(path, 'b01-001-s00-0' + str(i) + '.jpg')) 
	i = i+1