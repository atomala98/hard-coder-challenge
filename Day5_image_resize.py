import os
import sys
from PIL import Image
from io import BytesIO

setup = {
    "B": {
        "power": 3,
        "divisor": 0
    },
    "kB":{
        "power": 6,
        "divisor": 3
    },
    "MB":{
        "power": 9,
        "divisor": 6
    },
    "GB":{
        "power": 12,
        "divisor": 9
    }
}

used_memory = 0 
saved_memory = 0
for filename in os.listdir('./img'):
    with Image.open('./img/{}'.format(filename)) as image: 
        format = filename.split('.')[1]
        width, height = image.size 
        small_image = image.resize((width//2, height//2))
        img_file = BytesIO()
        image.save(img_file, format)
        bigger_img_size = img_file.tell()
        img_file = BytesIO()
        small_image.save(img_file, format)
        smaller_img_size = img_file.tell()
        used_memory += bigger_img_size
        saved_memory += bigger_img_size - smaller_img_size
        try:
            small_image.save('./smaller/small {}'.format(filename))
        except:
            os.mkdir('./smaller')
            small_image.save('./smaller/small {}'.format(filename))

percentage_memory = 100*saved_memory/used_memory
print("You got {:.2f} lighter files.".format(percentage_memory))

for key, value in setup.items():
    if 10**setup[key]['power'] > saved_memory:
        saved_memory = saved_memory/(10**setup[key]['divisor'])
        print("You got {:.2f}{} free memory after compressing.". format(saved_memory, key))
        break