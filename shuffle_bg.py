import sys
import os
import random

try:
    print("User Current Version:-", sys.version)
    # Image path and images
    image_path="/home/ashu3103/Desktop/background_images"
    images = [entry for entry in os.listdir(image_path)]

    # command to calculate number of files in a directory
    cmd1 = f"ls {image_path} | wc -l"
    number_of_images = int(os.popen(cmd1).read())

    # Generating random index
    random_index = random.randint(0,number_of_images-1)

    image = images[random_index]
    image = os.path.join(image_path, image)

    cmd2 = f"gsettings set org.gnome.desktop.background picture-uri file:///{image}"
    os.system(cmd2)
except:
    pass