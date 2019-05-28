'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib 
matplotlib.use('Agg') #makes it usable in  a non-gui envirnment (toggles it)
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
#7 Woman Subplot is created
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
# Show the figure on the screen
# fig.show()
fig.savefig('women_plot')
"""

#If display error occurs, close the ipython terminal and use a new terminal

"""
The way that we fixed the code by using the code "matplotlib.use('Agg')". 
This is a code makes it so that it is functional in a non-GUI backend. This will property 
display the image in c9. 
"""
#a) (410,260)
"""
#b) Cat subplot is created

# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
#fig.show() Used for a GUI backend

fig.savefig('cat_plot') #saves the figure as in a non-gui environment at cat_plt.png
"""

# I got the coordinates of the tip of the nose to be (470,246)

#8)
#fig is an instance of the class figure. This is the image saved at the end of the code

#ax is an instance of the class AxesSubPlot. This is when there are multiple of axis. 

#b Similarly, in line 25, the method savefig is being called on the object fig. 
# That method is being given one_argument arguments. That method is a method of 
#the class figure.

#9)

""""# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
# Show the figure on the screen
#fig.show() Used for a GUI backend

fig.savefig('two_woman') #saves the figure as in a non-gui environment at cat_plt.png"""

#ii)
"""
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename) 

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 5)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
#fig.show() Used for a GUI backend

fig.savefig('five_cats') #saves the figure as in a non-gui environment at cat_plt.png


#10) 
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation = 'none') # Override the default
ax[1].imshow(img, interpolation = 'none')
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig('leaf_earing')

'''
The interpolation overrides the default code for the imgshow since c9 is a non 
gui interface. Also the xlim and ylim set the limits for both of the images to 
show the leaf earing. This is allows the code to work through the fact that c9 
is a non gui, also allowing c9 to "crop" the image for just the earing.
'''

#11 a)
"""
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename) 

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(5, 2)
# Show the image data in a subplot
ax[0][0].imshow(img, interpolation='none')
ax[1][0].imshow(img, interpolation='none')
ax[2][0].imshow(img, interpolation='none')
ax[3][0].imshow(img, interpolation='none')
ax[4][0].imshow(img, interpolation='none')
ax[0][1].imshow(img, interpolation='none')
ax[1][1].imshow(img, interpolation='none')
ax[2][1].imshow(img, interpolation='none')
ax[3][1].imshow(img, interpolation='none')
ax[4][1].imshow(img, interpolation='none')
ax[0][0].set_xlim(244,614)
ax[1][0].set_xlim(244,614)
ax[2][0].set_xlim(244,614)
ax[3][0].set_xlim(244,614)
ax[4][0].set_xlim(244,614)
ax[0][1].set_xlim(244,614)
ax[1][1].set_xlim(244,614)
ax[2][1].set_xlim(244,614)
ax[3][1].set_xlim(244,614)
ax[4][1].set_xlim(244,614)
ax[0][0].set_ylim(84,325)
ax[1][0].set_ylim(84,325)
ax[2][0].set_ylim(84,325)
ax[3][0].set_ylim(84,325)
ax[4][0].set_ylim(84,325)
ax[0][1].set_ylim(84,325)
ax[1][1].set_ylim(84,325)
ax[2][1].set_ylim(84,325)
ax[3][1].set_ylim(84,325)
ax[4][1].set_ylim(84,325)
ax[0][0].cla()
ax[1][0].cla()
ax[2][0].cla()
ax[3][0].cla()
ax[4][0].cla()
ax[0][1].cla()
ax[1][1].cla()
ax[2][1].cla()
ax[3][1].cla()
ax[4][1].cla()
# Show the figure on the screen
#fig.show() Used for a GUI backend

fig.savefig('experiment') #saves the figure as in a non-gui environment at cat_plt.png

#b
"""
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[2].imshow(img)
ax[0].set_xlim(140, 150)
ax[0].set_ylim(450, 440)
ax[1].set_xlim(155, 165)
ax[1].set_ylim(430, 420)
ax[2].set_xlim(145, 155)
ax[2].set_ylim(470, 460)
# Show the figure on the screen
fig.show()
fig.savefig('three_closeup.png')
"""
#12

"""
#13

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[1].plot(39, 48, 'ro')
ax[1].plot(118, 42, 'ro')
ax[1].plot(141, 41, 'ro')
# Show the figure on the screen
fig.show()
fig.savefig('crazy_mice.png')
"""

"""Conclusion"""
"""
1) A similarity between between absolute filenames and relative filenames and 
relative filenames is the fact that both lead you to a file. For an absolute 
filename, it the contains root directory and all other subdirectories in which a
file or folder is contained. This means that the pathway wil travel through all 
the files and it doesn't matter what file you are currently present in. While the
relative filenames are based on the current working directory. This means that 
the file you are currently in does matter in this pathway. 

"""
"""
2) An object is a part of the class what uses the class code in order to be 
instantialted. This means that the object has states and behaviors in the class.
These objects are used when wanting to use a class and instantiate that code. An
object is a realized version of the class, where the class is manifested in the 
program.
"""

"""
3) The corallation between a method and a property is that a method is instructions
for properties to execute. An example of a method in matplotlib is the xlim(parameters).
This a method in the class in order for a certain code to become functional. 
This allows the code to be presnet in numerous areas and "instantiate" the code.
While properties are a specific value to be called on the method. This means that
the properties are "parameters" of the method. This is the values put in the 
method when intantiating the class and the values. 
"""

"""
4) When you call a method on an object, this will run all the code in the method
on that object. This means that the code a-> has a fixed values for the method
or b-> uses properties in the methd as parameters. This code will be functional
and will be working on the object taht the method is being placed currently on. 
"""

