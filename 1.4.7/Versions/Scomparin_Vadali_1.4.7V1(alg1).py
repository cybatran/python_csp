from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.Image
import PIL.ImageDraw
 #https://stackoverflow.com/questions/8110342/overlay-text-on-a-picture-with-pil

def algorithm_1():
    '''
    This packages all the code for the first manipulating using no parameters 
    and containing 3 functions inside the package in order to get the image, 
    manipulate it and add a border, and finally, alter the image. 
    '''
    def border(original_image, alpha):
        width,height = original_image.size#gets dimensions of target image
        border = PIL.Image.new("RGBA", (width + 50, height + 50), (101,171,174,150)) 
        #using the .new function with parameters (mode, size, color)
        border.paste(original_image, (25,25), mask = original_image.convert("RGBA"))
        return border
        """
        width,height = original_image.size#gets dimensions of target image
        width = border_thickness * 2
        
        height = border_thickness * 2
        
        border_mask = PIL.Image.new("RGBA", (width, height), (101,171,174,150)) #using the .new function with parameters (mode, size, color)
        
        drawing_layer = PIL.ImageDraw.Draw(border_mask)
        
        drawing_layer.rectangle(((border_thickness, border_thickness),(width-border_thickness, height-border_thickness)), fill = None) 
        
        plt.imshow(mask)
        
        border_mask.paste(original_image, (0,0), mask=drawing_layer)
        
        return border_mask
        """
    def get_images(directory=None): 
        '''
        Gets all images from the directory.
        '''
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        image_list = [] # Initialize aggregaotrs
        file_list = []
        directory_list = os.listdir(directory) # Get list of files
        for entry in directory_list:
            absolute_filename = os.path.join(directory, entry) #gets abs. filename
            try:
                image = PIL.Image.open(absolute_filename) #opens image as PIL
                file_list += [entry] #appends to aggregators
                image_list += [image]
            except IOError:
                pass # do nothing with errors tying to open non-images
        return image_list, file_list
    
    def alter_all_images(directory=None):
        '''
        Calls the modifier on all images.
        '''
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        # Create a new directory 'modified'
        new_directory = os.path.join(directory, 'Algorithm 1.9')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass # if the directory already exists, proceed
        #load all the images
        image_list, file_list = get_images(directory)
        logo_file = os.path.join(directory, '1.4.7_Logo.png')
        logo = PIL.Image.open(logo_file)
        fig2, axes2 = plt.subplots(1, 2)
        axes2[0].imshow(logo)
        
        #need to write code to change names of images
        '''
        for n in range(len(image_list)):
            # Parse the filename
            filename, filetype = file_list[n].split('.')
            # Round the corners with radius = 30% of short side
            image = image_list[n].convert('RGBA') #converts to same format as red
            new_image = border(image,.4)
            #new_image.paste(logo,(100,100),mask = logo)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename) #saves img
        '''
        for image in range(len(image_list)):
            print(len(image_list))
            filename, filetype = os.path.splitext(file_list[image])
            new_image = border(image_list[image],0.4)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename)
    alter_all_images()
    
algorithm_1()
