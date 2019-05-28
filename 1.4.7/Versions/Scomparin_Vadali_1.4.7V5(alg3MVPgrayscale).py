from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import os.path  
import PIL
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from PIL import Image, ImageDraw, ImageFont

 #https://stackoverflow.com/questions/8110342/overlay-text-on-a-picture-with-pil

def make_global():
    global r
    r = raw_input("What red value do you want as your border? \n")
    global g 
    g = raw_input("What green value do you want as your border? \n")
    global b
    b = raw_input("What blue value do you want as your border? \n")


def algorithm_5():
    '''
    image = PIL.Image.open("1.4.7_baginstore.png")
    helvetica = PIL.ImageFont.truetype(filename="Helvetica.ttf", size=40)
    d = PIL.ImageDraw.Draw(image)

    location = (100, 50)
    text_color = (100, 100, 200)
    d.text(location, "Image_Text", font=helvetica, fill=text_color)
    
    image.save("text_test.png")
    '''
    # import required classes
     
     
    # create Image object with the input image
     
    image = Image.open('1.4.7_baginstore.png')
    width, height = image.size
    # initialise the drawing context with
    # the image object as background
     
    draw = ImageDraw.Draw(image)
    
    # create font object with the font file and specify
    # desired size
     
    font = ImageFont.truetype('../Roboto-Bold.ttf', size=15)
     
    # starting position of the message
    (x, y) = (50, 50)
    message = "Visit www.natwatdf.org for more info"
    color = 'rgb(0, 255, 0)' # black color
    draw.text((x, y), message, fill=color, font=font)
    
    (x, y) = (width * 5.5, height * 5.5)
    name = raw_input("Enter a short, powerful statement summarizing the image here: ")
    color = 'rgb(255, 255, 255)' # white color
    draw.text((x, y), name, fill=color, font=font)
     
    # save the edited image
     
    image.save('texttest_7.png')
    
def algorithm_1():
    '''
    This packages all the code for the first manipulating using no parameters 
    and containing 3 functions inside the package in order to get the image, 
    manipulate it and add a border, and finally, alter the image. 
    '''
    #make_global()
    
    def limits():
        if r > 255:
            print("The red value goes only to 255, so we will make it 255")
            r = 255
            return r
        if g > 255:
            print("The green value goes only to 255, so we will make it 255")
            g = 255
            return g
        if b > 255:
            print("The blue value goes only to 255, so we will make it 255")
            b = 255
            return b
            
    def watermark(original_image, alpha, directory = None):
        width,height = original_image.size#gets dimensions of target image
        limits()
        border = PIL.Image.new("RGBA", (width + 50, height + 50), (r, g, b,255)) #using the .new function with parameters (mode, size, color)
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
        
        
        for image in range(len(image_list)):
            print(len(image_list))
            filename, filetype = os.path.splitext(file_list[image])
            # Round the corners with radius = 30% of short side
            image = image_list[image].convert('RGBA') #converts to same format as red
            new_image = watermark(image,.4)
            
            img = PIL.Image.new('RGBA', (columns, rows))
            grayscale_img = new_image.resize(columns, rows)
            img = img.paste(new_image, 0, 0)
            image = np.array(img)
            
            for row in range(len(image[0])):
                for column in range(len(image)):
                    average_rgb = image[row][column][0] + image[row][column][1] + image[row][column][2]
                    average_rgb = average_rgb //3
                    image[rows][column] = (average_rgb, average_rgb, average_rgb, 255)
            
            image = PIL.Image.fromarray(img)

            new_image.paste(logo_small,(0,0),mask = logo_small)
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
    alter_all_images(100, 100)
    
def algorithm_2():
    """
    """
    def watermark(original_image, alpha, directory = None):
        width,height = original_image.size#gets dimensions of target image
        border = PIL.Image.new("RGBA", (width + 50, height + 50), (101,171,174,150)) #using the .new function with parameters (mode, size, color)
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
    
    make_global()
    
    def watermark(original_image, alpha, directory = None):
        width,height = original_image.size#gets dimensions of target image
        border = PIL.Image.new("RGBA", (width + 50, height + 50), (int(r),int(g),int(b),255)) #using the .new function with parameters (mode, size, color)
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
    
    def alter_all_images(rows,columns, directory=None):
        '''
        Calls the modifier on all images.
        '''
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        # Create a new directory 'modified'
        new_directory = os.path.join(directory, 'Algorithm 3.1')
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
        
    
        for n in range(len(image_list)):
            print(len(image_list))
            filename, filetype = os.path.splitext(file_list[n])
            # Round the corners with radius = 30% of short side
            image = image_list[n].convert('RGBA') #converts to same format as red
    
            new_image = watermark(image,.4)
            new_image.paste(logo_small,(25,25),mask = logo_small)
            
            img = PIL.Image.new('RGBA', (columns, rows))
            grayscale_img = new_image.resize((rows, columns))
            img = img.paste(grayscale_img, (0,0), mask = grayscale_img)
            image_2 = np.array(img)
            
            for row in range(len(image[1])):
                for column in range(len(image)):
                    average_rgb = image[row][column][0] + image[row][column][1] + image[row][column][2]
                    average_rgb = average_rgb //3
                    image[rows][column] = (average_rgb, average_rgb, average_rgb, 255)
            
            new_image = PIL.Image.fromarray(img)
            
            water_file = os.path.join(directory, '1.4.7_dirt_water.png')
            water_img = PIL.Image.open(water_file)
            
            new_image.paste(water_img, (rows-(int(rows*0.1)),columns-(int(columns*0.1))), mask = water_img)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename) #saves img
    alter_all_images(100,100) 

def algorithm_4():
    def watermark(original_image, alpha, image):
        """ 
    
        """
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
        
        """
        for image in range(len(image_list)):
            print(len(image_list))
            filename, filetype = os.path.splitext(file_list[image])
            new_image = watermark(image_list[image],0.4,blend_image)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename)
        """
        
        
        
    alter_all_images()
"""
algorithm_5()
algorithm_1()
algorithm_2()
"""
algorithm_3()
"""
algorithm_4()
"""