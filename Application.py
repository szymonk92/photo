import exifread
import os
import numpy as np
import matplotlib.pyplot as plt

# path
path = "F:\\MEGA\\Zdjecia\\2016"
path_test = "C:\\Users\\szymo\\Desktop"

# exif strings
focal_length = 'EXIF FocalLength'
iso = 'EXIF ISOSpeedRatings'
f_number = 'EXIF FNumber'
time = 'EXIF ExposureTime'

# acceptable formats
list_of_formats = (".jpg", ".jpeg", ".dng", ".tiff", ".raw", ".nef")  # ,".pef")
full_list_of_formats = list_of_formats + tuple([x.upper() for x in list_of_formats])

# dictionaries
focal_dict = {}
iso_dict = {}
f_dict = {}
time_dict = {}


def open_image():
    f = open(image, 'rb')
    image_exif = exifread.process_file(f)
    return image_exif


def add_or_update_dict(dictionary, value):
    if value in dictionary:
        dictionary[value] += 1
    else:
        dictionary[value] = 1


def calculate(exif_list, k, dictionary, do_round=False, round_value=0):
    if k in exif_list:
        value = ''.join([str(i) for i in exif_list[k].values])
        if do_round:
            value = round(eval(value), round_value)
        add_or_update_dict(dictionary, value)
        #print(k, " ", value)


def plot_histogram(dictionary, name):
    plt.bar(list(dictionary.keys()), list(dictionary.values()), align='center')
    plt.xlabel(name)
    plt.ylabel('Number of photos')
    plt.title(name)
    plt.grid(True)
    plt.show()


def show_in_terminal(dictionary, name):
    print(name, " number of images")
    for key in sorted(dictionary):
        print(key, dictionary[key])


'''Program starts here'''
image_files = [os.path.join(root, name)
               for root, dirs, files in os.walk(path_test)
               for name in files
               if name.endswith(full_list_of_formats)]

for image in image_files:
    tags = open_image()
    calculate(tags, focal_length, focal_dict, True)
    calculate(tags, iso, iso_dict)
    calculate(tags, f_number, iso_dict, True, 1)
    calculate(tags, time, time_dict)

print("#Number of images:", len(image_files))
plot_histogram(focal_dict, focal_length)
