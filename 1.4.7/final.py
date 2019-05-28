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
    global border
    border = raw_input("What type of border would you like: \n round or box or none:")
    global r
    r = raw_input("What red value do you want as your border? (0-255) \n")
    global g 
    g = raw_input("What green value do you want as your border? (0-255) \n")
    global b
    b = raw_input("What blue value do you want as your border? (0-255) \n")              
    global a
    a = raw_input("What opacity do you want your border to be? (0-255) \n")
    global row 
    row = raw_input("How big do you want your image? \n")
    global column 
    column = raw_input("How wide do you want your image? \n")

def watermark_round(original_image, percent_of_side=.3): #percent of side is showing the border radius of an image
    make_global()
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
    result = PIL.Image.new('RGBA', original_image.size, (int(r),int(g),int(b),int(a)))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
def watermark(original_image, alpha, directory = None):
    width,height = original_image.size#gets dimensions of target image
    
    border = PIL.Image.new("RGBA", (width + 50, height + 50), (int(r),int(g),int(b),int(a))) 
    
    #using the .new function with parameters (mode, size, color)
    
    border.paste(original_image, (25,25), mask = original_image.convert("RGBA"))
    
    return border

def algorithm_5():
    make_global()
    '''
    Adds text as defined by the user, starting at a specific location relative to image
    width and height. Also resizes the text to fit within the image borders for 
    standard phrase lengths.
    '''
    ''' 
    image = Image.open('Final_Images/final.py') #opens the image file
    width, height = image.size #determines width and height of image, allowing image to be used as drawing background

    draw = ImageDraw.Draw(image) #allows text to be placed on image
    
    font = ImageFont.truetype("../../Roboto-Bold.ttf", size=int(width/40)) #links to font file 
    # starting position of the message
    (x, y) = (width * 0.1, height * 0.85) #determines location of first letter in text
    website = "Visit www.natwatdf.org for more info" #text to be printed
    color = (255, 255, 255)
    draw.text((x, y), website, fill=color, font=font)#prints text on page
    
    #THE PART THAT WE WILL ONLY APPLY TO THE FINAL IMAGES ONE BY ONE
    font = ImageFont.truetype('../../Roboto-Bold.ttf', size=int(width/28))
    (x, y) = (width * 0.05, height * 0.5)
    statement = raw_input("Enter a short (ideally under 60-80 char), powerful statement summarizing the image here: ") 
    # allows the user to enter whatever text pertains to their goal
    color = (0, 255, 0)
    if len(statement) < 60:
        draw.text((x, y), statement, fill=color, font=font)
    else:
        font = ImageFont.truetype('../../Roboto-Bold.ttf', size=int(width/(40+(0.2*(len(statement)-60)))))
        draw.text((x, y), statement, fill=color, font=font)
        
    font = ImageFont.truetype('../../Roboto-Bold.ttf', size=int(width/28))
    (x, y) = (width * 0.05, height * 0.6)
    statement1 = raw_input("Enter a short (ideally under 60-80 char), powerful statement summarizing your oragnizations's goal regarding the image here: ") 
     # allows the user to enter whatever text pertains to their goal
    color = (0, 255, 0)
    if len(statement1) < 60:
        draw.text((x, y), statement1, fill=color, font=font)
    else:
        font = ImageFont.truetype('../../Roboto-Bold.ttf', size=int(width/(40+(0.2*(len(statement1)-60)))))
        draw.text((x, y), statement1, fill=color, font=font)
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
    
    def alter_all_images(rows, columns, directory=None):
        '''
        Packages the functioon in order to manipulate the images and place them 
        under a folder. This is using no parameters and is calling the function 
        watermark in order to blend the images and paste images on the bended 
        images. 
        '''
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        # Create a new directory what you name it
        folder = raw_input("What do you want to call the folder: ")
        new_directory = os.path.join(directory, folder)
        image_list, file_list = get_images(directory)
        
        logo_file = os.path.join(directory, '../1.4.7_Logo.png') #finding the image
        logo_img = PIL.Image.open(logo_file) #opening the image under the variable logo_img
        logo_small = logo_img.resize((int(float(columns)*0.1),int(float(columns)*0.1)))
        
        donate_file = os.path.join(directory, '../1.4.7_donate.png') #finding the image
        donate_img = PIL.Image.open(donate_file)
        donate_small = donate_img.resize((int(float(columns)*0.6),int(float(rows)*0.3)))
        
        for image in range(len(image_list)): #a for loop that iterates through the files
            print("Running...")
            filename,filetype = os.path.splitext(file_list[image])
            image = image_list[image].convert('RGBA') #converts to same format as red
            
            if border == "round" or border == "Round":
                new_image = watermark_round(image)
            elif border == "box" or border == "Box":
                new_image = watermark(image, 0.5)
            elif border == "none" or border == "None":
                new_image = image
            else:
                print("You didn't choose a border so you will not get a border!")
            new_image.resize((int(columns),int(rows)))
            new_image.paste(logo_small,(100, 100),mask = logo_small)
            #new_image.paste(donate_small, ( int(float(columns)+ 300.0) , int(float(rows) + 300.0)), mask = donate_small)
            new_image.save(filename + "_final.png", format= "png") #saves img
    alter_all_images(row,column) #calling the function that alters the images
algorithm_5()