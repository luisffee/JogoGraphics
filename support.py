from csv import reader
from os import walk
from graphics import *


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path, position):
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            img = Image(Point(position[0], position[1]), f'{full_path}')
            surface_list.append(img)
    return surface_list
