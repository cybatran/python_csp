from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw            
"""
def round_corners_one_image(original_image, percent_of_side=.3): #percent of side is showing the border radius of an image
    ''' Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    '''
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    print (rounded_mask)
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
    # Uncomment the following line to show the mask
    #plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
def get_images(directory=None):
    '''
    Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    '''
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def round_corners_of_all_images(directory=None):
    '''
    Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    '''
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = round_corners_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    
"""  
#5
"""
round_corners_one_image()
get_images()
round_corners_of_all_images()
"""

#6
"""
This function manipulated all the images to have rounded corners as well as 
changing the file to a png format. This is using multiple maskes in order to have 
rounded corners. 
"""

#7

#a
"""
The function round_corners_one_image() was one we made up. It is defined here to 
take 2 arguments.

Argument 1: original_image

Argument  2: percent_of_side

Return value: The new image

"""

#b
"""
white
"""
#c
"""
Object created in line 26: round_mask

Object created in line 27: drawing_layer

"""

#d
"""
0 because taht will make it white
"""

#e
"""
On the left figure, that is created with the lines 41 - 48.
On the right figure, that is created with the lines 33 - 38. 
"""

#f
"""
It will be white because of the a value being 0. 
"""
#g
"""
The color values will be (0,0,0,0)
"""

#8
"""


def get_images(directory=None):
    '''
    Returns PIL.Image objects for all the images in directory.
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a PIL.Image object for each image file in root_directory,     
    and a list with a string filename for each image file in root_directory
    '''

    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified

    image_list=[] # Initialize aggregators
    file_list = []

    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

"""
#a
"""
How many arguments can be passed to the function get_images()? Because a default
value is specified for directory, that argument is optional, so get_images() can
be passed either 0 or 1 arguments.
"""

#b
"""
Two list objects are returned by the function
"""

#c
"""
os.getcwd() 

os.listdir(directory) 

os.path.join(director, entry)

"""

#d
"""
Return a list containing the names of the entries in the directory given by path.
The list is in arbitrary order, and does not include the special entries '.' 
and '..' even if they are present in the directory.
"""

#e
"""
They bipass the errors because if the library has any errors, or if the image 
has errors, you will be able to manipulate the imageeven if there is an error.
"""

#f
"""
This code is used to work even through errors except for the IOError. This is 
showing if there is an error for that line, and if that error isn't present, the
code will be executed. 
"""

#9
"""
def round_corners_of_all_images(directory=None):
    ''' Saves a modified version of each image in directory.

    Uses current directory if no directory is specified. 
    Puts images in subdirectory 'modified', creating it if needed.
    New image files are of type PNG and have transparent rounded corners.
    '''

    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified

    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed 

    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = round_corners_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 
"""

#a
"""
This code is in a try -execpt code because if there is a directory that is named
the original directory, then the file will not be present and the code will not 
be present.  
"""

#b
"""
len(image_list) is present in order to explain how many items are in the directory. 
"""

#c
"""
The role of n is to show the value of images in the list in order to easily 
manipulate a certain image. The n could mean the number of images in the 
image_list. 
"""
def round_corners(original_image, percent_of_side = 0.3):

    """ 
    Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    
    Returns a new PIL.Image with rounded corners, where
    
    0 < percent_of_side < 1
    
    is the corner radius as a portion of the shorter dimension of original_image
        """
    
    #set the radius of the rounded corners
    
    width, height = original_image.size
    
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    
    #create a mask
    
    ###
    
    #start with transparent mask
    
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    
    # The 127 for RGB values was used merely for visualizing the mask
    
    #make the mask of the new eclipse shape
    
    drawing_layer.ellipse((0,0,width, height),
    
    fill=(0,127,127,255)) #top left
    
    # Uncomment the following line to show the mask
    
    #plt.imshow(frame)
    
    # Make the new image, starting with all transparent
    
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    
    result.paste(original_image, (0,0), mask=rounded_mask)
    
    #result.paste(result, (0,0), mask=frame)
    
    frame_mask = PIL.Image.new('RGBA', (width, height), (0, 0, 0, 0))
    
    drawing_layerF = PIL.ImageDraw.Draw(frame_mask)
    
    # Draw hollow eclipse frame
    
    drawing_layerF.ellipse((0,0,width, height),
    
    fill=(240,240,30,255))
    
    drawing_layerF.ellipse((20,20,width-20, height-20),
    
    fill=(0,127,127,0))
    
    result.paste(frame_mask,(0,0),mask=frame_mask)
    
    return result
    
def get_images(directory=None):
    
    """ 
    Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    
    Returns a 2-tuple containing
    
    a list with a PIL.Image object for each image file in root_directory, and
    
    a list with a string filename for each image file in root_directory
    
    """
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        image_list = [] # Initialize aggregaotrs
        file_list = []
        directory_list = os.listdir(directory) # Get list of files
        
        for entry in directory_list:
        
            absolute_filename = os.path.join(directory, entry)
        
        try:
        
            image = PIL.Image.open(absolute_filename)
            
            file_list += [entry]
            
            image_list += [image]
            
        except IOError:
        
            pass # do nothing with errors tying to open non-images
    
    return image_list, file_list
    
    
    
def round_corners_of_all_images(directory=None):
    
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified.
    
    Places images in subdirectory 'modified', creating it if it does not exist.
    
    New image files are of type PNG and have transparent rounded corners.
    
    """
    
    if directory == None:
    
        directory = "/Users/brandonbuchta/Pictures/1.4.5Images"##os.getcwd() # Use working directory if unspecified
        
        print(directory)
        
    # Create a new directory 'modified'
    
    new_directory = os.path.join(directory, 'modified2')
    
    try:
    
        os.mkdir(new_directory)
    
    except OSError:
    
        pass # if the directory already exists, proceed
    
    #load all the images
    
    image_list, file_list = get_images(directory)
    
    
    
    #go through the images and save modified versions
    
    for n in range(len(image_list)):
    
    # Parse the filename
    
        filename, filetype = file_list[n].split('.')
        
        # Round the corners with radius = 30% of short side
        
        new_image = round_corners(image_list[n],.30)
        
        #save the altered image, suing PNG to retain transparency
        
        new_image_filename = os.path.join(new_directory, filename + '.png')
        
        new_image.save(new_image_filename)
        

get_images()
round_corners_of_all_images()
###############################################################################
#                       Conclusion                                            #
###############################################################################

#1

"""
This is possible is creating a mask that has an alpha value to be 0. This means 
that you will be clear image around the mask in order to see the background of 
the icon. This is helpful and allow the image to look neater. 
"""

#2
"""
This allows the code to be used in many images. These functions allow for the 
mask to craetea a rounded edges at the end. This is making the manipulation easier
because this code is allowing to manipulate any image for any data type. 
"""

#3
"""
Alice because if the picture is taken in an old camera, and a new camera, the 
photo quality is different. This is showing how there are different changes in 
the same photo, the data will be different. A camera essential emmulate how the
human eye works because they can't simulate it. 
"""

#4
"""
An image can be distributed and/or sold if you took the image yourself, or if the
image isn't copyrighted. If the image isn't copyright, you are able to copyright
that image with edits and proof of originality, you have the rights to sell or 
distribute that image. 
"""

#5
"""
My partner and I had a good team dynamic. We were able to learn from eachother's 
mistakes. Also, we used two different workspaces in order to see if we recieve 
errors and learn from them. Also, we commented out and explained the code together,
as we learned what the code meant. 
"""