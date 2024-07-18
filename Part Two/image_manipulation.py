import matplotlib.pyplot as plt

from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
filename2 = path + '/' + 'dingadingading.png'
data = image.imread(filename)
data2 = image.imread(filename2)
# Display image information
print('Image type is: ', type(data))
print('Image shape is: ', data.shape)

print('Image type is: ', type(data2))
print('Image shape is: ', data2.shape)

# Add some color boundaries to modify an image array
plot_data = data.copy()
plot_data2 = data2.copy()
for width in range(data2.shape[1]):
    for height in range(data2.shape[0]):
        plot_data[height][512-264+width] = [
        int(255 * data2[height][width][0]),
        int(255 * data2[height][width][1]),
        int(255 * data2[height][width][2])

        ]
        

        
# Write the modified images
image.imsave(path+'/'+'lenna-mod.jpg', plot_data)
# image.imsave(path + '/' + 'pride_in_flag.png', plot_data2)

# use pyplot to plot the image
#need both imshow and pyplot.show to actually see image
pyplot.imshow(plot_data)
# pyplot.imshow(plot_data2)
pyplot.show()