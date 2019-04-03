from PIL import Image
import os
import numpy as np
path1 = 'dctorset/'
path2 = 'data_subset/'

f1 = os.listdir(path1)
f2 = os.listdir(path2)

img = Image.open(path2+f2[0])
a = np.asarray(img)
print(a.shape) 

# for file in f1:
# 	img = Image.open(path1+file).convert('LA')
# 	img.save(path1+file)