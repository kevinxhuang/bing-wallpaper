#!/usr/bin/env python3

from xml.etree import ElementTree
from urllib import request
import log
from image import Image

BASE_URL = 'http://www.bing.com'
IMAGE_API = '/HPImageArchive.aspx?format=xml&idx=%d&n=%d&mkt=%s'

logger = log.Logger(__file__, '../wallpaper.log')

def get_images(idx=1, n=8, mkt='en-US'):

    images = []

    api_url = (BASE_URL + IMAGE_API) % (idx, n, mkt)
    logger.info('Fetch images...')
    try:
        tree = ElementTree.parse(request.urlopen(api_url))
        root = tree.getroot()
        for element in root.findall('image'):

            name = element.find('startdate').text + '.jpg'
            url = BASE_URL + element.find('url').text
            image = Image(name, url)
            images.append(image)
    except (request.HTTPError, request.URLError) as error:
        logger.error('Can not retrieve the data because %s, URL:%s', error, api_url)
    except ElementTree.ParseError:
        logger.error('The response can not be parse.')
    else:
        logger.info('Fetch images successful.')

    return images







