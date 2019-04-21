# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:09:57 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys,os
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
import util.folder_traverse

class folder_traverse_test:

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')



def main():
    ftt = folder_traverse_test()
    fobj = folder_traverse.folder_traverse('D:\\Live_quotes')
    filedet = fobj.folder_nav_path()

    ftt.log.info(filedet.count)

if __name__ == "__main__":
    main()

""" End -of class """
