from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
#4
# Both arrays and lists contain data. This allows the data to be easy to access 
#and also ierate through. However, arrays are multidimensional while list are 
# single dimension of values. 

#5
"""
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('women2')

print(img)
print(len(img))
print(len(img[0]))

the image height = the number of rows of pixels = 960
the image width = the number of columns = 584
the green intensity at (5,9) = img[5][9][1]
the red intensity at (4,10) = 62
the red intensity of the 25th pixel in the 50th row = 79
"""

#6
"""
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
height = len(img)
width = len(img[0])
for row in range(420,475):
    for column in range(130, 160):
        img[row][column] = [0, 255, 0] # red + green = yellow
fig.savefig('green_earing')
"""
#7
"""
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
fig.savefig('woman_sky')

a) The algorithm is allowing the fact that if a sum of the rgb is greater than 
500, then taht area will become magenta. This code works because a-> the area 
around the sky is green and dark so it wouldn't be greater than 500, and b -> 
the sky is a light blue, almost white, so alteast two colors need to be full. 
That will be greater than 500. 

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
###
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
height = len(img)
width = len(img[0])
for r in range(422, 467):
    for c in range(135, 162):
        if sum(img[r][c])>400: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
fig.savefig('women_sky_earing.png')

#8

import PIL

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(0, 100, 3):
        for column in range(0, 100, 3):
            if (row+column) < 130 or (row+column) > 150: #(row+column)/stripe_width % 4 == 0: #and (row+column) < 100: 
                if (row+column)/stripe_width % 3 == 0 or (row+column)/stripe_width % 3 == 1:
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                    image[row][column] = [255, 255, 0, 255] # magenta, alpha=255
            
            elif 130 <= (row+column) <= 150:
                for row in range(60, 80, 2):
                     for column in range(60, 80, 2):
                        image[row][column] = [255, 255, 0, 255] # magenta, alpha=255
            
            
            else:
                # Odd stripe
                image[row][column] = [255, 127, 127, 0] # pale red, alpha=0
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask')       
    
    
# 9.

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'women_sky_earing.png')
filename_1 = os.path.join(directory, 'mask.png')
# Read the image data into an array
img = plt.imread(filename)
img_1 = plt.imread(filename_1)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img_1, interpolation = 'none')
# Show the figure on the screen
fig.show()
fig.savefig('woman_and_mask')
"""

"""Conclusion"""

"""
1) The data in a digital image contains is the RGB values for the pixel. 
This means that each pixel as its own rgb value and is stored on that pixel. 
In a multidimensional array, the code will show that there are 3 values in the 
pixel. These values ae the RGB.If the image isaltered and the values change, this
means that the RBG values have changed in the code. 
"""
"""
2) For a light sensative camera, there is no backup code for the picture to be 
saves. However, a digital camera does have the data saved. Also the light 
sensative camera is a printing, causing there to be not functions to zoom in and
out or change the RGB of the picture. However the digital camera has some interpolation
based on the camera, as well has all the functions such as zoom in and out, and 
saving and changing the image. Finally digital cameras can delete their data and
so they can hold an "infinte" amount of pictures.  However, both are the same 
because both take the picture and is easiy seen by the visual and how good the 
image is. 
"""

"""
3) 
    a) The 6 bits are of least significance in the image representation because 
    of the fact that These bits are too tiny to make a noticeable difference in 
    a photo. Since a photo is made up of numerous bits, these 6 bit are so small 
    that they don't affect the image to a large extent. This means that the edits
    will be "naked to the human eye" because of how small it is. 
    
    b)Since bits are coded into binary, 63 is a big enough value. If you place 
    the two, 63 is the maximum the code can count to 63 in a 6 bits code. This 
    means that 63 is the maximum value it can be, and 0 is the minimum. This 
    means that the encoded message will fit the 63 range since that is the 
    maximum value for a 6 bit value in binary. 
    
    c) It is possible if numerous pixels are affected by the 6 bits. This will 
    blow out the encoded code and will be preset. This means that magenta sky is
    just the 6 bits "enlarged" and is present in the image as it is manipulated.
    Also, based on the code, the 6 bitsare only present based on the color, so if
    the color varies to below 500, then you will see different colors. 
"""
"""
4) This a basic agorithm due to the fact that each pixel is it's own seperate 
value. This means that since a pictureis a multidimensional array, then the 
amount of rows multiplied by the number of colomns multipled by 3 because of 
RGB will give  you the amount of seperate values. Also if you use a kernel value
and a feature map, you will be able to get a value for the image as well as map
out he entire image for the values.   
"""