#!/usr/bin/env python3

class Image(object):

    def __init__(self, name, url):
        self._name = name
        self._url = url

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value