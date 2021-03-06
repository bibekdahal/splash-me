#!/bin/python3
import requests
import shutil
from os import system, path


directory = path.dirname(path.abspath(__file__))
image_path = path.join(directory, 'wallpaper')
system(f'feh --bg-scale {image_path}')

try:
    url = 'https://source.unsplash.com/1920x1080/?nature'
    r = requests.get(url=url, stream=True)
    with open(image_path, 'wb') as out_file:
        shutil.copyfileobj(r.raw, out_file)
except Exception:
    pass

system(f'feh --bg-scale {image_path}')
