from PIL import Image, ImageEnhance
import src.convert_to_jpg
import src.delete_exif
import random
import string
from pystyle import *
import os 

def delete_exif(image_path, output_path, random_name):
    image_path = Image.open(image_path)

    data = list(image_path.getdata())
    image_without_exif = Image.new(image_path.mode, image_path.size)
    image_without_exif.putdata(data)
    image_without_exif.save(output_path)
    print(Center.XCenter(Colors.light_red + "D" + Colors.white + "eleted exif path : " + Colors.light_red + 'input\\' + Colors.white + random_name))

def convert_to_jpg(image_path, output_path):
    im = Image.open(image_path)
    image_size_before_conversion = os.path.getsize(image_path)
    print(Center.XCenter(Colors.light_red + "I" + Colors.white + "mage size before the jpg conversion : " + Colors.light_red + "(" + Colors.white + str(image_size_before_conversion) + Colors.light_red + ")"))
    rgb_im = im.convert("RGB")  

    
    rgb_im.save(output_path)
    image_size_after_conversion = os.path.getsize(output_path)
    print(Center.XCenter(Colors.light_red + "I" + Colors.white + "mage size after the jpg conversion : " + Colors.light_red + "(" + Colors.white + str(image_size_after_conversion) + Colors.light_red + ")"))

os.system("title Random Photo © v1.0.0")
os.system('cls')

logo = """
______                _                ______ _           _        
| ___ \              | |               | ___ \ |         | |       
| |_/ /__ _ _ __   __| | ___  _ __ ___ | |_/ / |__   ___ | |_ ___  
|    // _` | '_ \ / _` |/ _ \| '_ ` _ \|  __/| '_ \ / _ \| __/ _ \ 
| |\ \ (_| | | | | (_| | (_) | | | | | | |   | | | | (_) | || (_) |
\_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_\_|   |_| |_|\___/ \__\___/ 
                                                                                                                                 
"""

print(Colorate.Vertical(Colors.white_to_red, Center.XCenter(logo)))
print(Center.XCenter(Colors.light_red + "                                                 |" + Colors.white + " Created by AfraL" + Colors.light_red + " |     "))

print("\n")

for nom in os.listdir("input"):
    extension=nom.split('.')[-1].lower()
    
    characters = string.ascii_letters + string.digits
    random_name = ''.join(random.choice(characters) for i in range(32))
    
    if not extension == ".jpg" or ".jpeg" or ".jfif":
        convert_to_jpg(image_path=f'input\\{nom}', output_path=f'input\\{random_name}' + '.jpg')
    
    characters = string.ascii_letters + string.digits
    second_random_name = ''.join(random.choice(characters) for i in range(32))
    
    #os.system('pause')
    
    delete_exif(image_path=f'input\\{random_name}' + '.jpg', output_path=f'input\\{second_random_name}' + '.jpg', random_name=second_random_name)
    os.remove(f'input\\{random_name}' + '.jpg')
    
    img = Image.open(f'input\\{second_random_name}' + '.jpg')
    width, height = img.size
    width = int(width) - 1
    height = int(height) - 1
    print(Center.XCenter(Colors.light_red + "I" + Colors.white + "mage size before resizing : " + Colors.light_red + "(" + Colors.white + str(width) + Colors.light_red + "," + Colors.white + str(height) + Colors.light_red + ")"))
    
    img_resized = img.resize((width,height))
    width, height = img_resized.size
    width = int(width) - 1
    height = int(height) - 1

    print(Center.XCenter(Colors.light_red + "I" + Colors.white + "mage size after resizing : " + Colors.light_red + "(" + Colors.white + str(width) + Colors.light_red + "," + Colors.white + str(height) + Colors.light_red + ")"))

    img_resized.save(f'output\\{second_random_name}.{extension}')
    
    os.remove(f'input\\{second_random_name}' + '.jpg')
    print(Colors.reset + "\n")