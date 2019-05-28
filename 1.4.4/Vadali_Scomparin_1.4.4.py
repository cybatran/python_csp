'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_eye')


#13
"""
    - matplotlib.pyplot: plot the images on coordinate planes
    - numpy: create a array set for the images
    - PIL: manipulate the images by croping images, filtering, and many more. 
"""


#15
#a
"""
Line 19 calls the function subplot from the matplotlib library. The function is 
being called with 2 argument(s): (1, 2). The function returns 2 object(s), 
which is/are being assigned to ax.

"""
#b
"""
Line 20 calls __imshow()_ on ___ax[0]____
Line 23 calls __imshow()_ on ___ax[1]___
Line 24 calls set_xticks  on ____ax[1]__
Line 25 calls set_xlim()  on ____ax[1]__
Line 26 calls set_ylim()  on ____ax[1]__
Line 27 calls savefig()   on ____fig____
"""
#c
"""
(1162,966)
"""

#16
"""
width: 13.125 px
height: 13.125 px
top-left: (202.875,237.75)
bottom-right: (216, 250.875)
"""

#17

#a
"""
Line 30 uses the join() method from the os.path module. It is being passed 2 
arguments. The value it returns is being assigned to the variable earth_file.
"""

#b
"""
In line 31 the open() function of the PIL.Image module returns a new PIL.Image 
object, which is being assigned to the variable earth_img. 
"""

#c
"""
For the outer set of parentheses are for the method. These parentheses hold the 
parameters of the method resize. The inner set of parentheses are the dimension 
of the picture.The inside of the parentheses is (x,y) having the resize values 
you choose. 
"""
#d
"""
The (89,87) is the (x,y) values for the size of the resized image. This is for
image to uderstand how many pixels will be in the new image. 
"""

#e
"""
29 Open, resize, and display earth
30 earth_file = os.path.join(directory, 'earth.png')
31 earth_img = PIL.Image.open(earth_file)
32 earth_small = earth_img.resize((89, 87)) # w and h measured in plt
33 fig2, axes2 = plt.subplots(1, 2)
34 axes2[0].imshow(earth_img)
35 axes2[1].imshow(earth_small)
36 fig2. savefig('resize_earth')

Line 33 calls the function subplot() from the matplotlib library with 2 
argument(s): grid, array. The function returns 2 object(s), which is/are being 
assigned to fig2 and ax2.

Line 34 calls the method imshow() on the object axes[0] with 1 argument(s): earth_img

Line 35 calls the method imshow() on the object ax[1] with 1 argument(s): earth_small

Line 36 calls the function savefig from the PIL library with 1 argument(s): 'resize_earth'. The function returns 1 object(s), which is/are being assigned to fig2.

"""
#f
"""
i)
You can add an other parameter of resize of filter 

ii) The default value for the argument is NEAREST

iii)
Size because it is compressing the image into less bytes and a smaller package 
if using the parameter of size.
"""
#g
"""
The values are representing the width and the height of the new image in order 
for the old image to compress it. 
"""

#h
print(earth_img.size)
print(earth_small.size)
print(earth_img.size[1])
"""
These outpust represent the size of the image, being (x,y). Since you are asking
it with .size, you are asking for the size of the image and if you want, the 
width or heigh. 
"""

#i
"""
You are able to tell the different amount of pixels because of the quality of the
image. If there are more pixels, you will have less pixels and also you will see
a clearer image. This is beneficial and will make btter images.  
"""

#18
"""
For the resize method, the algorithm goes to every pixel and sees what color it 
should be based on the dimensions given. Then for each region, it averages 
all the intensities, saving bytes and shrinking the image.
"""

#19

"""
38 # Paste earth into right eye and display
39 # Uses alpha from mask 
40 student_img.paste(earth_small, (1162, 966), mask=earth_small) 
41 # Display
42 fig3, axes3 = plt.subplots(1, 2)
43 axes3[0].imshow(student_img, interpolation='none')
44 axes3[1].imshow(student_img, interpolation='none')
45 axes3[1].set_xlim(500, 1500)
46 axes3[1].set_ylim(1130, 850)
47 fig3. savefig('earth_eye')
"""

#a 
"""
student_img: The size is 1920 * 2720 * 3 = 15, 667, 200
earth_small: The size is 89   * 87   * 3 = 23, 229
"""

#b
earth_small.save('smallEarth.png')

#c
"""
smallEarth = 87.5 * 85.5 * 100
smallEarth: 748,125
student = 1920 * 2720 * 3
student: 15,667,200
"""
#d
"""
In step a, the values have increased due to the resizing of the images. This is 
changing the values since the image size is different.
"""
#e 
"""
In the paste method, if you add a color, it will set all the pixels to the color
that you want. This will set multiple pixels to the same color, if you add a 
color parameter. 
"""
#f
"""
According to the documentation, the code omitted, a mode is chosen so that all 
information in the image and the palette can be represented without a palette. 
When converting from a colour image to black and white, the library uses the 
ITU-R 601-2 luma transform: L = R * 299/1000 + G * 587/1000 + B * 114/1000. When
converting to a bilevel image (mode1), the source image is first converted to
black and white.
"""

#g
"""
The aurguments are explaining the file of which you want to paste on the old 
image. You also need to explain the location of where you want to add the images.
And finally, the mask is to take the area you are currently in. 
"""
#20 
# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966) ,mask=earth_small) 
student_img.paste(earth_small, (708,944), mask = earth_small)
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_as_eyes')

"""Conclusion"""
#1
"""
In this lesson, you are using tha class of AxesSubplot in order to manipulate the
images. Then you used themethods of savefig(), save(), paste(), etc. These methods
allow the user to insert and manipulate an image in a NON_GUI envirnment. The 
paste aslo allows the user to add other items at a certain location in to edit 
the code. 
"""

#2 
"""
In this activity, we used the abstractions of the the PIL library in order to 
paste images as well as manipulating it. Based on that statemet, it explains that
we are able add multiple items in order to make the code more complex. This is 
important and will make the code better. 
"""