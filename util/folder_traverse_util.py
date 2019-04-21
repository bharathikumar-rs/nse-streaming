# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:07:25 2019

@author: ArchuBharathi
"""

import os
import logging
from logging.config import fileConfig

# =============================================================================
#  Get folder path and returns all files path in a list
# =============================================================================
class folder_traverse:

    def __init__(self):
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')


    def folder_nav_path(self, path):
        self.log.debug('folder nav Path reached ')
        files = []
        for file in os.listdir(path):
            current = os.path.join(path, file)
            self.log.debug("current file/path :" + current)
            if os.path.isfile(current):
              #  data = open(current, "rb")
              #   print(len(data.read()))
                files.append(current)
             # print (files.count)

        return files
