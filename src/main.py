#!/usr/bin/env python3

from bingwallpaper import *
from downloader import *
from wallpaper import *
import os

logger = log.Logger(__file__, '../wallpaper.log')

if __name__ == '__main__':
    if not os.path.exists('../images'):
        os.mkdir('../images')

    images = get_images(1, 8)
    count = 0
    for image in images:
        image_path = os.path.join('../images', image.name)
        if not os.path.exists(image_path):
            download(image.url, image_path)
            count += 1

    logger.info('Total %d images downloaded.', count)

    downloaded_images = os.listdir('../images/')
    if len(downloaded_images) > 0:
        downloaded_images = sorted(downloaded_images, reverse=True)
        wallpaper_image = os.path.join('../images/', downloaded_images[0])
        set_wallpaper(os.path.abspath(wallpaper_image))
        logger.info('Set %s to be wallpaper', wallpaper_image)





