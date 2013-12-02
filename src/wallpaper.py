#!/usr/bin/env python3

import subprocess
import os.path

def set_wallpaper(image_path):
    image_path = os.path.abspath(image_path)
    cmd = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", '"file://{}"'.format(image_path)]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)