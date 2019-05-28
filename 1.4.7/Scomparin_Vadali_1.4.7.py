from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path  
import PIL
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from PIL import Image, ImageDraw, ImageFont



def make_global():
    global r
    r = raw_input("What red value do you want as your border? \n")
    global g 
    g = raw_input("What green value do you want as your border? \n")
    global b
    b = raw_input("What blue value do you want as your border? \n")              
    global a
    a = raw_input("What opacity do you want your border to be? \n")

def watermark(original_image, alpha, image):
        """
        This packages the code that adds a border to the image as well as blending
        two images together. Using the parameters of original_img, the original 
        image of the folder, the paramteter image, that is the image that is being
        blended on to, and alpha, for the opacity of the image being blended on to. 
        """
        width, height = original_image.size #gets dimensions of target image

        image = image.resize((width, height)) #resizes the image so the size is equal to the original image
    
        result = PIL.Image.blend(original_image, image, alpha) # blending the image together using the blend function
    
        #final = PIL.Image.new("RGBA", (width + 50, height + 50), (int(r),int(g),int(b),int(a))) # creating a new image as the border that is 25 by 25 
        
        #final.paste(result,(25,25),mask=result) #pasting the blended image onto the border 
        
        return result


    
def algorithm_1():
    '''
    This packages all the code for the first manipulating using no parameters 
    and containing 3 functions inside the package in order to get the image, 
    manipulate it and add a border, and finally, alter the image. 
    '''
    def get_images(directory=None): 
        '''
        Using no paramters, it is fetching the images from the directories in 
        order for them to be manipulated
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
        Packages the functioon in order to manipulate the images and place them 
        under a folder. This is using no parameters and is calling the function 
        watermark in order to blend the images and paste images on the bended 
        images. 
        '''
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        image_list, file_list = get_images(directory)
        
        blend_image = PIL.Image.open('../1.4.7_trash_pile.png') #opening 1.4.7_trash_pile in the variable blend_image
        #blend_image is the image that will be blended to the original images
        blend_image = blend_image.convert("RGBA") #converting a RGB format into a RGBA format
        
        for image in range(1): #a for loop that iterates through the files
            print("Algorithm 1")
            filename, filetype = os.path.splitext(file_list[image])
            new_image = PIL.Image.open("../1.4.7_lake.png")
            image = image_list[image].convert('RGBA') #converts to same format as red
            final = watermark(new_image, 0.5, blend_image)
            final.save('final.png', format = "png")
        
    alter_all_images() #calling the function that alters the images

def algorithm_2():
    """
    Packages the code in order to manipulate the second image using no paramters
    and having two images ontop of eachother. This also uses three functions in 
    order to manipulate the code, watermark(), get_image(), and alter_all_images().
    """
    def get_images(directory=None): 
        '''
        Using no paramters, it is fetching the images from the directories in 
        order for them to be manipulated
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
        Packages the functioon in order to manipulate the images and place them 
        under a folder. This is using no parameters and is calling the function 
        watermark in order to blend the images and paste images on the bended 
        images. 
        '''
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        # Create a new directory 'modified'
        image_list, file_list = get_images(directory)
        
        
        boat_file = os.path.join(directory, '../Algorithm 2.2/1.4.7_underwaterboat.png') 
        boat_img = PIL.Image.open(boat_file).convert("RGBA") #opening the image under the variable logo_img
        
        image = Image.open("../1.4.7_seaoftrash.png").convert("RGBA")
        width, height = image.size #gets dimensions of target image
        image = image.resize((width - 372, height - 200 )) #resizes the image so the size is equal to the original image
        
        #final = image.save('1.4.7_resizedseaoftrash.png')

        image2 = Image.open("../1.4.7_whitebackground.png").convert("RGBA")
        width2, height2 = image2.size #gets dimensions of target image
        image2 = image2.resize((width2 - 326 , height2 - 100)) #resizes the image so the size is equal to the original image
        
        #final2 = image2.save('1.4.7_resizedwhitebackground.png')
        
        image2.paste(boat_img, (0,height-250), mask = boat_img)
        image2.paste(image,(0,0), mask = image)
        
        image2.save('final2.png', format = "png")
        
        print("Algorithm 2")
        
    alter_all_images()

def algorithm_3():
    '''
    Packages the code in order to create and manipulate the images by 
    grayscaling, pasting and creating a border for all my images, using three 
    functions in the code
    '''
    def get_images(directory=None): 
        
        """
        Using no paramters, it is fetching the images from the directories in 
        order for them to be manipulated 
        """
        
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
    
    def alter_all_images(rows,columns, directory=None):
        '''
        Calls the modifier on all images.
        '''
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        # Create a new directory 'modified'
        image_list, file_list = get_images(directory)
        
        
        water_file = os.path.join(directory, '../1.4.7_dirt_water.png')
        water_img = PIL.Image.open(water_file)
        water_large = water_img.resize((int(float(columns)*1),int(float(rows)*1.5)))
        
        for image in range(1):
            print("Algorithm 3")
            filename, filetype = os.path.splitext(file_list[image])
            # Round the corners with radius = 30% of short side
            image = image_list[image].convert('RGBA') #converts to same format as red
            
            new_image = image
           
            new_image.resize((1000,1699))
            new_image = PIL.Image.open('../1.4.7_river.png').convert('LA')
            final = new_image
            final.paste(water_large, (int(float(columns) * 0.75),rows - 700), mask = water_large)
            final.save("final3.png", format = "png") #saves img
            
    alter_all_images(1000,1699) 

def algorithm_4():
    '''
    Blends new images together to create a composite image, and pastes the logo
    and donate images. 
    '''

    def get_images(directory=None): 
        
        """
        Using no paramters, it is fetching the images from the directories in 
        order for them to be manipulated
        """
        
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
        """
        Packages the functioon in order to manipulate the images and place them 
        under a folder. This is using no parameters and is calling the function 
        watermark in order to blend the images and paste images on the bended 
        images. 
        """
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        # Create a new directory 'modified'

        image_list, file_list = get_images(directory)
        
        blend_image = PIL.Image.open('../1.4.7_dolphin_bag.png')
        blend_image = blend_image.convert("RGBA")
        
        #need to write code to change names of images
        
        for image in range(1):
            print("Algorithm 4")
            filename, filetype = os.path.splitext(file_list[image])
            image = image_list[image].convert('RGBA') #converts to same format as red
            new_image = PIL.Image.open("../1.4.7_baginstore.png")
            final = watermark(new_image, 0.5, blend_image)
            final.save('final4.png', format = "png")


    alter_all_images()

algorithm_1()
algorithm_2()
algorithm_3()
algorithm_4()
