#!/usr/bin/env python3

from bingwallpaper import *
from downloader import *
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



