import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from PIL import Image

img = Image.open("./flower.jpg")

##creating the matrix of the image
img_mat = np.array(img)

##checking if it is an matrix
type(img_mat)

##showing the ploted img
plt.imshow(img_mat)

img_red = img_mat.copy()
##removing blue colors from all pixels   ":"  means every pixel
img_red[:,:,2] = 0
##removing green
img_red[:,:,1] = 0


##showing red_img
plt.imshow(img_red)