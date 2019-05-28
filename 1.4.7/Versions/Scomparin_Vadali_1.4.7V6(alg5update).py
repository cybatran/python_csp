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

 #https://stackoverflow.com/questions/8110342/overlay-text-on-a-picture-with-pil
'''
def make_global():
    global r
    r = raw_input("What red value do you want as your border? \n")
    global g 
    g = raw_input("What green value do you want as your border? \n")
    global b
    b = raw_input("What blue value do you want as your border? \n")              COMMENTED OUT SO COULD WORK ON ALG_5
    global rows
    rows = raw_input("How many rows do you want the image to be?\n")
    global columns
    columns = raw_input("How many columns do you want the image to be?\n")
'''

def algorithm_5():
    '''
  
    '''
    
    image = Image.open('1.4.7_river.png')
    width, height = image.size
    print (width)
    # initialise the drawing context with
    # the image object as background
     
    draw = ImageDraw.Draw(image)
    
    # create font object with the font file and specify
    # desired size
     
    #THE PART WE WILL APPLY TO ALL IMAGES AT ONCE 
    font = ImageFont.truetype('../Roboto-Bold.ttf', size=int(width/40))
    # starting position of the message
    (x, y) = (width * 0.55, height * 0.95)
    website = "Visit www.natwatdf.org for more info" 
    color = 'rgb(0, 255, 255)' # black color
    draw.text((x, y), website, fill=color, font=font)
    
    
    #THE PART THAT WE WILL ONLY APPLY TO THE FINAL IMAGES ONE BY ONE
    font = ImageFont.truetype('../Roboto-Bold.ttf', size=int(width/28))
    (x, y) = (width * 0.05, height * 0.7)
    statement = raw_input("Enter a short (under 60 char), powerful statement summarizing the image here: ") 
    color = (0, 255, 0)
    if len(statement) < 60:
        draw.text((x, y), statement, fill=color, font=font)
    else:
        font = ImageFont.truetype('../Roboto-Bold.ttf', size=int(width/(40+(0.2*(len(statement)-60)))))
        draw.text((x, y), statement, fill=color, font=font)
    # save the edited image
     
    image.save('texttestimg2_2.png')

    
    
def algorithm_1():
    '''
    This packages all the code for the first manipulating using no parameters 
    and containing 3 functions inside the package in order to get the image, 
    manipulate it and add a border, and finally, alter the image. 
    '''
    
    
    
    def watermark(original_image, alpha, directory = None):
        width,height = original_image.size#gets dimensions of target image
        border = PIL.Image.new("RGBA", (width + 50, height + 50), (66,158,244,255)) #using the .new function with parameters (mode, size, color)
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
        new_directory = os.path.join(directory, 'Algorithm 1.10_logo')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass # if the directory already exists, proceed
        #load all the images
        image_list, file_list = get_images(directory)
        
        #need to write code to change names of images
        logo_file = os.path.join(directory, '1.4.7_Logo.png')
        logo_img = PIL.Image.open(logo_file)
        logo_small = logo_img.resize((89, 87))
        
        fig2, axes2 = plt.subplots(1, 1)
        fig2.savefig('resize_logo.png')
        
        logo_small.save("logo.png")
        
        trash_file = os.path.join(directory, '1.4.7_trashdump.png')
        trash_img = PIL.Image.open(trash_file)
        trash_small = trash_img.resize((860,460))
        
        for image in range(len(image_list)):
            print(len(image_list))
            filename, filetype = os.path.splitext(file_list[image])
            # Round the corners with radius = 30% of short side
            image = image_list[image].convert('RGBA') #converts to same format as red
            new_image = watermark(image,.4)

            new_image.paste(logo_small,(0,0),mask = logo_small)
            #new_image.paste(trash_small, (272,50), mask = trash_small)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename) #saves img
            
        """
        for image in range(len(image_list)):
            print(len(image_list))
            filename, filetype = os.path.splitext(file_list[image])
            new_image = watermark(image_list[image],0.4)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename)
        """
    alter_all_images()
    
def algorithm_2():
    """
    """
    def watermark(original_image, alpha, directory = None):
        width,height = original_image.size#gets dimensions of target image
        border = PIL.Image.new("RGBA", (width + 50, height + 50), (101,171,174,150)) #using the .new function with parameters (mode, size, color)
        border.paste(original_image, (25,25), mask = original_image.convert("RGBA"))
        return border
        
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
        '''s
        Calls the modifier on all images.
        '''
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        # Create a new directory 'modified'
        new_directory = os.path.join(directory, 'Algorithm 2.5')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass # if the directory already exists, proceed
        #load all the images
        image_list, file_list = get_images(directory)
        
        #need to write code to change names of images
        logo_file = os.path.join(directory, '1.4.7_Logo.png')
        logo_img = PIL.Image.open(logo_file)
        logo_small = logo_img.resize((89, 87))
        
        fig2, axes2 = plt.subplots(1, 1)
        fig2.savefig('resize_logo.png')
        
        logo_small.save("logo.png")
        
        turtle_file = os.path.join(directory, '1.4.7_turtle.png')
        turtle_img = PIL.Image.open(turtle_file)
        turtle_small = turtle_img.resize((400,266))#keep a similar ratio
        
        fig2, axes2 = plt.subplots(1, 1)
        fig2.savefig('resize_turtle.png')
        
        turtle_small.save("turtle.png")
        
        for image in range(len(image_list)):
            print(len(image_list))
            filename, filetype = os.path.splitext(file_list[image])
            # Round the corners with radius = 30% of short side
            image = image_list[image].convert('RGBA') #converts to same format as red
            new_image = watermark(image,0.5)
            new_image.paste(logo_small,(25,25),mask = logo_small)
            new_image.paste(turtle_small,(110,421),mask = turtle_small)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename) #saves img
        
        
    alter_all_images()

def algorithm_3():
    
    def watermark(original_image, alpha, directory = None):
        width,height = original_image.size#gets dimensions of target image
        border = PIL.Image.new("RGBA", (width + 50, height + 50), (101,171,174,150)) #using the .new function with parameters (mode, size, color)
        border.paste(original_image, (25,25), mask = original_image.convert("RGBA"))
        return border
        
        
    def get_images(directory=None): 
        
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
        new_directory = os.path.join(directory, 'Algorithm 3.7')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass # if the directory already exists, proceed
        #load all the images
        image_list, file_list = get_images(directory)
        
        #need to write code to change names of images
        logo_file = os.path.join(directory, '1.4.7_Logo.png')
        logo_img = PIL.Image.open(logo_file)
        logo_small = logo_img.resize((89, 87))
        
        fig2, axes2 = plt.subplots(1, 1)
        fig2.savefig('resize_logo.png')
        
        logo_small.save("logo.png")
        
        water_file = os.path.join(directory, '1.4.7_dirt_water.png')
        water_img = PIL.Image.open(water_file)
        water_large = water_img.resize((int(float(columns)*1),int(float(rows)*0.75)))
            
        for image in range(1):
            print(len(image_list))
            filename, filetype = os.path.splitext(file_list[image])
            # Round the corners with radius = 30% of short side
            image = image_list[image].convert('RGBA') #converts to same format as red
            
            new_image = watermark(image,.4)
            new_image.paste(logo_small,(25,25),mask = logo_small)
            
            new_image.resize((1000,1699))
            new_image = PIL.Image.open('1.4.7_river.png').convert('LA')
            
            new_image.paste(water_large, (int(float(columns) * 0.75),int(float(rows) * 0.75)), mask = water_large)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename) #saves img
            print(type(rows))
    alter_all_images(1000,1699) 

def algorithm_4():
    def watermark(original_image, alpha, image):
        
        width, height = original_image.size #gets dimensions of target image

        image = image.resize((width, height))
        
    
        result = PIL.Image.blend(original_image, image, alpha) 
    
        final = PIL.Image.new("RGBA", (width + 50, height + 50), (101,171,174,150))
        
        final.paste(result,(25,25),mask=result) 
        
        return final

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
        new_directory = os.path.join(directory, 'Algorithm 4.7')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass # if the directory already exists, proceed
        #load all the images
        image_list, file_list = get_images(directory)
        
        logo_file = os.path.join(directory, '1.4.7_Logo.png')
        logo_img = PIL.Image.open(logo_file)
        logo_small = logo_img.resize((89, 87))
        
        fig2, axes2 = plt.subplots(1, 1)
        fig2.savefig('resize_logo.png')
        
        logo_small.save("logo.png")
        
        blend_image = PIL.Image.open('1.4.7_dolphin_bag.png')
        blend_image = blend_image.convert("RGBA")
        
        #need to write code to change names of images
        
        for image in range(len(image_list)):
            print(len(image_list))
            filename, filetype = os.path.splitext(file_list[image])
            # Round the corners with radius = 30% of short side
            image = image_list[image].convert('RGBA') #converts to same format as red
            new_image = watermark(image,0.5, blend_image)
            new_image.paste(logo_small,(25,25),mask = logo_small)
            algorithm_5()
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename) #saves img
        
        
        
    alter_all_images()
