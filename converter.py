import os
import PIL




from PIL import Image


def check_file(filepath):
    N = 4; length = len(f)
    suffix = f[length - N:]
    if suffix == ".png":
        img = Image.open(filepath)
        textArt = png_to_text(img)
        fileName = os.path.basename(filepath)
        save_result_as_file(textArt, fileName)
    elif suffix == ".jpg":
        img = Image.open(filepath)
        textArt = jpg_to_text(img) 
        fileName = os.path.basename(filepath)
        save_result_as_file(textArt, fileName)
        
    pass

def png_to_text(img):
    width = img.width
    height = img.height
    data = img.load()
    print("looping through png with scale of " + str(width) + " by " + str(height))
    textArt = ""
    for y in range(0, height):
        for x in range(0, width):
            pixel = data[x,y]
            R = (pixel[0] + pixel[1] + pixel[2])/3
            if R == 255:
                textArt += " . "
            elif R > 220:
                textArt += "..."
            elif R> 200:
                textArt += "---"
            elif R > 150:
                textArt += "-I-"
            elif R > 125:
                textArt += "I-I"
            elif R > 100:
                textArt += "III"
            elif R > 50:
                textArt += "OOO"
            else:
                textArt += "wmw"
        textArt += "\n"
    return textArt

def save_result_as_file(textArt, name):
    with open("exports" + "\ " + name + ".txt", "w") as f:
        f.write(textArt)
    pass



def jpg_to_text(img):
    width = img.width
    height = img.height
    data = img.load()
    print("looping through jpg with scale of " + str(width) + " by " + str(height))
    textArt = ""
    for y in range(0, height):
        for x in range(0, width):
            pixel = data[x, y]
            G = pixel
            if G > 127:
                textArt += " . "
            else:
                textArt += "WMW"
        textArt += "\n"
    return textArt
        


dirname = os.path.dirname(__file__)
directory = os.path.join(dirname, "images")
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        N = 4; length = len(f)
        suffix = f[length - N:]
        if suffix == ".png" or suffix == ".jpg":
            print(f)
            check_file(f)
        else:
            print("not valid file type")


