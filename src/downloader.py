#!/usr/bin/env python3

from urllib import request
import log

USER_AGENT = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.160 Safari/537.22'

headers = {}

logger = log.Logger(__file__, '../wallpaper.log')

def download(download_url, path):
    if 'User-Agent' not in headers:
        headers['User-Agent'] = USER_AGENT

    try:
        req = request.Request(url=download_url.replace(' ', '%20'), headers=headers)
        image = request.urlopen(req)
        f = open(path, 'wb+')
        f.write(image.read())
        f.close()
    except (request.HTTPError, request.URLError) as error:
        logger.error('Can not retrieve the data because %s, URL:%s', error, download_url)
    except IOError as error:
        logger.error(error)
    else:
        logger.info('Download %s successful.', path)
