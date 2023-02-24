from PIL import Image
import os

'''
input_dir="C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310"
output_dir="C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\images_ss"
'''

input_dir="path\\to\\input\\folder"
output_dir="path\\to\\output\\folder"

#use double slash for specifing the path directory so that you won't face issues like unicode error UXXXXXX
#Credits to be given to PIL and OS library in python

def resize_image(input_image_path, output_image_path):
    with Image.open(input_image_path) as image:
        new_image=image.resize((1366,768))
        new_image.save(output_image_path)
        print("Successfull")

for filename in os.listdir(input_dir):
    if filename.endswith('.jpg'):
        input_path=os.path.join(input_dir, filename)
        output_path=os.path.join(output_dir, filename)
        resize_image(input_path, output_path)
        
