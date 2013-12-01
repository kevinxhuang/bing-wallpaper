#!/usr/bin/env python3

import subprocess

def set_wallpaper(image_path):
    cmd = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", '"file://{}"'.format(image_path)]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == '__main__':
    image_path = '/home/killua/Workspace/bing-wallpaper/images/20131130.jpg'
    set_wallpaper(image_path)
