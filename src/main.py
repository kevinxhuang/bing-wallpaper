#!/usr/bin/env python3

from bingwallpaper import *
from downloader import *
from wallpaper import *
import os

logger = log.Logger(__file__, '../wallpaper.log')

if __name__ == '__main__':

    images_dir = os.path.join(os.path.dirname(__file__), '../images')

    if not os.path.exists(images_dir):
        os.mkdir(images_dir)

    images = get_images(1, 8)
    count = 0
    for image in images:
        image_path = os.path.join(images_dir, image.name)
        if not os.path.exists(image_path):
            download(image.url, image_path)
            count += 1

    logger.info('Total %d images downloaded.', count)

    downloaded_images = os.listdir(images_dir)
    if len(downloaded_images) > 0:
        downloaded_images = sorted(downloaded_images, reverse=True)
        wallpaper_image = os.path.join(images_dir, downloaded_images[0])
        set_wallpaper(wallpaper_image)
        logger.info('Set %s to be wallpaper', wallpaper_image)





