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


def algorithm_5():
    '''
    Adds text as defined by the user, starting at a specific location relative to image
    width and height. Also resizes the text to fit within the image borders for 
    standard phrase lengths.
    '''
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
    
        final = PIL.Image.new("RGBA", (width + 50, height + 50), (int(r),int(g),int(b),int(a))) # creating a new image as the border that is 25 by 25 
        
        final.paste(result,(25,25),mask=result) #pasting the blended image onto the border 
        
        return final
    
    image = Image.open('1.4.7_boattrashNOTEXT.png') #opens the image file
    width, height = image.size #determines width and height of image, allowing image to be used as drawing background

    draw = ImageDraw.Draw(image) #allows text to be placed on image
    
    font = ImageFont.truetype('../Roboto-Bold.ttf', size=int(width/40)) #links to font file 
    # starting position of the message
    (x, y) = (width * 0.1, height * 0.85) #determines location of first letter in text
    website = "Visit www.natwatdf.org for more info" #text to be printed
    color = (0, 0, 255)
    draw.text((x, y), website, fill=color, font=font)#prints text on page
    
    #THE PART THAT WE WILL ONLY APPLY TO THE FINAL IMAGES ONE BY ONE
    font = ImageFont.truetype('../Roboto-Bold.ttf', size=int(width/28))
    (x, y) = (width * 0.05, height * 0.5)
    statement = raw_input("Enter a short (ideally under 60-80 char), powerful statement summarizing the image here: ") 
    # allows the user to enter whatever text pertains to their goal
    color = (0, 255, 0)
    if len(statement) < 60:
        draw.text((x, y), statement, fill=color, font=font)
    else:
        font = ImageFont.truetype('../Roboto-Bold.ttf', size=int(width/(40+(0.2*(len(statement)-60)))))
        draw.text((x, y), statement, fill=color, font=font)
        
    font = ImageFont.truetype('../Roboto-Bold.ttf', size=int(width/28))
    (x, y) = (width * 0.05, height * 0.6)
    statement1 = raw_input("Enter a short (ideally under 60-80 char), powerful statement summarizing your oragnizations's goal regarding the image here: ") 
     # allows the user to enter whatever text pertains to their goal
    color = (0, 255, 0)
    if len(statement1) < 60:
        draw.text((x, y), statement1, fill=color, font=font)
    else:
        font = ImageFont.truetype('../Roboto-Bold.ttf', size=int(width/(40+(0.2*(len(statement1)-60)))))
        draw.text((x, y), statement1, fill=color, font=font)
    # save the edited image
    
    image.save('1.4.7_boattrashTEXTV2.png')


    
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
        # Create a new directory 'modified'
        new_directory = os.path.join(directory, 'Algorithm 1.14')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass # if the directory already exists, proceed
        #load all the images
        image_list, file_list = get_images(directory)
        
        logo_file = os.path.join(directory, '1.4.7_Logo.png') #finding the image
        logo_img = PIL.Image.open(logo_file) #opening the image under the variable logo_img
        logo_small = logo_img.resize((89, 87)) #resizing the image to be 89 by 87
        
        logo_small.save("logo.png") # save the image under a image called logo.png
        
        donate_file = os.path.join(directory, '1.4.7_donate.png') #finding the image
        donate_img = PIL.Image.open(donate_file)
        donate_small = donate_img.resize((200,68))
        
        blend_image = PIL.Image.open('1.4.7_trash_pile.png') #opening 1.4.7_trash_pile in the variable blend_image
        #blend_image is the image that will be blended to the original images
        blend_image = blend_image.convert("RGBA") #converting a RGB format into a RGBA format
        
        for image in range(1): #a for loop that iterates through the files
            print("Algorithm 1")
            filename, filetype = os.path.splitext(file_list[image])
            new_image = PIL.Image.open("1.4.7_lake.png")
            image = image_list[image].convert('RGBA') #converts to same format as red
            new_image = image.PIL.Image.blend("1.4.7_lake.png", blend_image, 0.4) #creating an image that is blended
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename) #saves img
        
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
        new_directory = os.path.join(directory, 'Algorithm 1.14')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass # if the directory already exists, proceed
        #load all the images
        image_list, file_list = get_images(directory)
        
        
        boat_file = os.path.join(directory, 'Algorithm 2.2/1.4.7_underwaterboat.png') 
        boat_img = PIL.Image.open(boat_file).convert("RGBA") #opening the image under the variable logo_img
        
        image = Image.open("1.4.7_seaoftrash.png").convert("RGBA")
        width, height = image.size #gets dimensions of target image
        image = image.resize((width - 372, height - 200 )) #resizes the image so the size is equal to the original image
        
        #final = image.save('1.4.7_resizedseaoftrash.png')

        image2 = Image.open("1.4.7_whitebackground.png").convert("RGBA")
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
        new_directory = os.path.join(directory, 'Algorithm 3.9')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass # if the directory already exists, proceed
        #load all the images
        image_list, file_list = get_images(directory)
        
        #need to write code to change names of images
        logo_file = os.path.join(directory, '1.4.7_Logo.png')
        logo_img = PIL.Image.open(logo_file)
        logo_small = logo_img.resize((int(float(columns)*0.1),int(float(rows)*0.1)))
        
        fig2, axes2 = plt.subplots(1, 1)
        fig2.savefig('resize_logo.png')
        
        logo_small.save("logo.png")
        
        water_file = os.path.join(directory, '1.4.7_dirt_water.png')
        water_img = PIL.Image.open(water_file)
        water_large = water_img.resize((int(float(columns)*1),int(float(rows)*1.5)))
        
        donate_file = os.path.join(directory, '1.4.7_donate.png') #finding the image
        donate_img = PIL.Image.open(donate_file)
        donate_small = donate_img.resize((int(float(columns)*0.4),int(float(rows)*0.3)))
        
        for image in range(1):
            print("Algorithm 3")
            filename, filetype = os.path.splitext(file_list[image])
            # Round the corners with radius = 30% of short side
            image = image_list[image].convert('RGBA') #converts to same format as red
            
            new_image = image
           
            new_image.resize((1000,1699))
            new_image = PIL.Image.open('1.4.7_river.png').convert('LA')
            final = new_image
            final.paste(water_large, (int(float(columns) * 0.75),rows - 700), mask = water_large)
            final.paste(logo_small,(25,25),mask = logo_small)
            final.paste(donate_small, (columns + 200 , rows + 450), mask = donate_small)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            final.save(new_image_filename) #saves img
            
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
        new_directory = os.path.join(directory, 'Algorithm 4.8')
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
        
        donate_file = os.path.join(directory, '1.4.7_donate.png') #finding the image
        donate_img = PIL.Image.open(donate_file)
        donate_small = donate_img.resize((200,68))
        
        blend_image = PIL.Image.open('1.4.7_dolphin_bag.png')
        blend_image = blend_image.convert("RGBA")
        
        #need to write code to change names of images
        
        for image in range(1):
            print("Algorithm 4")
            filename, filetype = os.path.splitext(file_list[image])
            # Round the corners with radius = 30% of short side
            image = image_list[image].convert('RGBA') #converts to same format as red
            new_image = image
            new_image = image.blend(new_image, blend_image, 0.4)
            new_image_filename = os.path.join(new_directory, filename + '.png')
            new_image.save(new_image_filename) #saves img
        

    alter_all_images()


algorithm_1()
algorithm_2()
algorithm_3()
algorithm_4()