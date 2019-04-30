# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:43:12 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
import pandas as pd
import logging
from logging.config import fileConfig
import os
import shutil

class filemove:

    def __init__(self):
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')



    def move(self,filedet,destpath):
        shutil.move(filedet,destpath)


if __name__ == "__main__":
    f = filemove()

""" End -of class """
